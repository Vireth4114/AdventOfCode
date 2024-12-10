import useful
from itertools import chain

lines = useful.get_list_lines('10')

trailheads = {(idx, idx2) for idx, line in enumerate(lines)
                          for idx2, c in enumerate(line) if c == '0'}

def get_neighbors(x, y):
    neighbors = []
    for i, j in ((0, 1), (1, 0), (-1, 0), (0, -1)):
        if not (0 <= x+i < len(lines) and 0 <= y+j < len(lines[0])):
            continue
        if int(lines[x+i][y+j]) != int(lines[x][y])+1:
            continue
        neighbors.append((x+i, y+j))
    return neighbors

def backtrack_silver(x, y):
    if lines[x][y] == '9':
        return [(x, y)]
    return set(chain(*[backtrack_silver(*neighbor) for neighbor in get_neighbors(x, y)]))

def backtrack_gold(x, y):
    if lines[x][y] == '9':
        return [(x, y)]
    return list(chain(*[backtrack_gold(*neighbor) for neighbor in get_neighbors(x, y)]))

print(sum(len(backtrack_silver(x, y)) for x, y in trailheads))
print(sum(len(backtrack_gold(x, y)) for x, y in trailheads))