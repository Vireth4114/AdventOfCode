import useful
from operator import add
from itertools import chain
import time
import curses

lines, moves = useful.get_lines_pure('15').split('\n\n')

lines = [list(l.replace('#', '##').replace('O', '[]').replace('.', '..').replace('@', '@.')) for l in lines.splitlines()]
moves = list(chain(*moves.splitlines()))

for idx, line in enumerate(lines):
    for idx2, char in enumerate(line):
        if char == '@':
            robot = (idx, idx2)

stdscr = curses.initscr()
curses.start_color()
curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_WHITE)
curses.init_pair(2, curses.COLOR_BLUE, curses.COLOR_BLUE)
curses.init_pair(3, curses.COLOR_RED, curses.COLOR_RED)
curses.init_pair(4, curses.COLOR_BLACK, curses.COLOR_BLACK)

def display_board():
    for idx, line in enumerate(lines):
        for idx2, c in enumerate(line):
            match c:
                case '@':
                    palette = 1
                case '[':
                    palette = 2
                case ']':
                    palette = 2
                case '#':
                    palette = 3
                case '.':
                    palette = 4
            stdscr.addch(idx, idx2, c, curses.color_pair(palette))
    stdscr.refresh()

for idx, move in enumerate(moves):
    if idx % 5 == 0:
        display_board()
    # time.sleep(0.05)
    to_move = []
    match move:
        case '<':
            direction = (0, -1)
        case '>':
            direction = (0, 1)
        case '^':
            direction = (-1, 0)
        case 'v':
            direction = (1, 0)
    to_move.append(robot)
    new_poss = [tuple(map(add, robot, direction))]
    while not any(lines[new_pos[0]][new_pos[1]] == '#' for new_pos in new_poss) and not all(lines[new_pos[0]][new_pos[1]] == '.' for new_pos in new_poss):
        new_poss2 = new_poss.copy()
        new_poss = []
        for new_pos in new_poss2:
            if lines[new_pos[0]][new_pos[1]] == '[':
                np_adj = tuple(map(add, new_pos, (0, 1)))
            elif lines[new_pos[0]][new_pos[1]] == ']':
                np_adj = tuple(map(add, new_pos, (0, -1)))
            else:
                continue
            np_dir = tuple(map(add, new_pos, direction))
            np_adj_dir = tuple(map(add, np_adj, direction))
            if new_pos not in to_move:
                to_move.append(new_pos)
            if np_adj not in to_move:
                to_move.append(np_adj)
            if np_adj_dir not in new_poss:
                new_poss.append(np_adj_dir)
            if np_dir != np_adj and np_dir not in new_poss:
                new_poss.append(np_dir)
    if any(lines[new_pos[0]][new_pos[1]] == '#' for new_pos in new_poss):
        continue
    for pos in to_move[::-1]:
        new_pos = tuple(map(add, pos, direction))
        lines[new_pos[0]][new_pos[1]] = lines[pos[0]][pos[1]]
        lines[pos[0]][pos[1]] = '.'
    robot = tuple(map(add, robot, direction))
    
res = 0
for idx, line in enumerate(lines):
    for idx2, char in enumerate(line):
        if char == '[':
            res += idx*100 + idx2

display_board()
time.sleep(1)
curses.endwin()
print(res)