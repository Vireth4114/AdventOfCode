import useful

dirs = [UP := (-1, 0), DOWN := (1, 0), LEFT := (0, -1), RIGHT := (0, 1)]

def rev_dir(dir):
    return (-dir[0], -dir[1])

lines = useful.get_list_lines("10.txt")

neighbors = {'|': [UP, DOWN],
             '-': [LEFT, RIGHT],
             'L': [UP, RIGHT],
             'J': [UP, LEFT],
             '7': [DOWN, LEFT],
             'F': [DOWN, RIGHT]}

loop = []
new_lines = []

def silverstar():
    global new_lines
    loop = []

    x, y = [(idx, line.index('S')) for idx, line in enumerate(lines) if 'S' in line][0]
    s_dirs = [dir for dir in dirs if rev_dir(dir) in neighbors[lines[x+dir[0]][y+dir[1]]]]

    new_dir = s_dirs[0]
    while lines[x+new_dir[0]][y+new_dir[1]] != 'S':
        loop.append((x, y))
        neighbors_new = neighbors[lines[x+new_dir[0]][y+new_dir[1]]]
        x, y = x+new_dir[0], y+new_dir[1]
        new_dir = neighbors_new[neighbors_new.index(rev_dir(new_dir))-1]

    loop.append((x, y))

    lines[loop[0][0]][loop[0][1]] = list(neighbors.keys())[list(neighbors.values()).index(s_dirs)]

    new_lines = [[' ' for _ in range(len(lines[0]))] for _ in range(len(lines))]
    for (l, c) in loop:
        new_lines[l][c] = lines[l][c]
    return len(loop)//2

def goldstar():
    count_inside = 0
    for l in range(len(new_lines)):
        is_inside = False
        for c in range(len(new_lines[0])):
            if new_lines[l][c] == '|' or (new_lines[l][c] in ('7', 'J') and last_first == ('7', 'J').index(new_lines[l][c])):
                is_inside = not is_inside
            elif new_lines[l][c] in ('L', 'F'):
                last_first = ('L', 'F').index(new_lines[l][c])
            elif is_inside and new_lines[l][c] == ' ':
                new_lines[l][c] = '#'
                count_inside += 1
    return count_inside

if __name__ == '__main__':
    print(f"Silver star: {silverstar()}")
    print(f"Gold star: {goldstar()}")