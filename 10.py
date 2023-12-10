import useful
import sys

sys.setrecursionlimit(100000)

lines = useful.get_lines("10.txt")

dict_neighbor = {'|': [(-1, 0), (1, 0)],
                 '-': [(0, -1), (0, 1)],
                 'L': [(-1, 0), (0, 1)],
                 'J': [(-1, 0), (0, -1)],
                 '7': [(1, 0), (0, -1)],
                 'F': [(1, 0), (0, 1)],
                 'S': [(1, 0), (0, 1), (-1, 0), (0, -1)]}


loop = set()
inside = set()

def loop_through(rev_param):
    for idx, line in enumerate(lines):
        if 'S' in line:
            start_pos = tuple([idx, line.index('S')])
            break
    while True:
        loop.add(start_pos)
        for neighbor in dict_neighbor[lines[start_pos[0]][start_pos[1]]]:
            true_pos = tuple([start_pos[0]+neighbor[0], start_pos[1]+neighbor[1]])
            if not (0 <= true_pos[0] < len(lines) and 0 <= true_pos[1] < len(lines[0])):
                continue
            if lines[true_pos[0]][true_pos[1]] == '.':
                continue
            if lines[true_pos[0]][true_pos[1]] == 'S' and len(loop) > 2:
                return loop
            if (-1*neighbor[0], -1*neighbor[1]) not in dict_neighbor[lines[true_pos[0]][true_pos[1]]]:
                continue
            if true_pos in loop:
                continue
            if rev_param:
                match neighbor:
                    case (0, 1):
                        inside.add((true_pos[0]+1, true_pos[1]-1))
                        inside.add((true_pos[0]+1, true_pos[1]))
                    case (0, -1):
                        inside.add((true_pos[0]-1, true_pos[1]+1))
                        inside.add((true_pos[0]-1, true_pos[1]))
                    case (1, 0):
                        inside.add((true_pos[0]-1, true_pos[1]-1))
                        inside.add((true_pos[0], true_pos[1]-1))
                    case (-1, 0):
                        inside.add((true_pos[0]+1, true_pos[1]+1))
                        inside.add((true_pos[0], true_pos[1]+1))
            else:
                match neighbor:
                    case (0, 1):
                        inside.add((true_pos[0]-1, true_pos[1]-1))
                        inside.add((true_pos[0]-1, true_pos[1]))
                    case (0, -1):
                        inside.add((true_pos[0]+1, true_pos[1]+1))
                        inside.add((true_pos[0]+1, true_pos[1]))
                    case (1, 0):
                        inside.add((true_pos[0]-1, true_pos[1]+1))
                        inside.add((true_pos[0], true_pos[1]+1))
                    case (-1, 0):
                        inside.add((true_pos[0]+1, true_pos[1]-1))
                        inside.add((true_pos[0], true_pos[1]-1))

            start_pos = true_pos
            break

def find_inside(value):
    inside.add(value)
    for neighbor in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
        true_pos = tuple([value[0]+neighbor[0], value[1]+neighbor[1]])
        if not (-1 <= true_pos[0] < len(lines)+1 and -1 <= true_pos[1] < len(lines[0])+1):
            continue
        if true_pos not in loop and true_pos not in inside:
            find_inside(true_pos)


if __name__ == '__main__':
    print(f'Silver star: {len(loop_through(False))//2}')
    inside = inside.difference(loop)
    for value in inside.copy():
        find_inside(value)
    print(f'Gold star: {len(inside)}')