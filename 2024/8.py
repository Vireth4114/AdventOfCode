import useful
from collections import defaultdict
from itertools import combinations, permutations

lines = useful.get_list_lines('8')
assert len(lines) == len(lines[0])
SIZE = len(lines)

antennas = defaultdict(set)
for idx, line in enumerate(lines):
    for idx2, c in enumerate(line):
        if c != '.':
            antennas[c].add((idx, idx2))

def silverstar():
    antinodes = set()
    for places in antennas.values():
        for (x1, y1), (x2, y2) in permutations(places, 2):
            x, y = x1-2*(x1-x2), y1-2*(y1-y2)
            if 0 <= x < SIZE and 0 <= y < SIZE:
                antinodes.add((x, y))
    return len(antinodes)

def goldstar():
    antinodes = set()
    for places in antennas.values():
        for (x1, y1), (x2, y2) in combinations(places, 2):
            for i in range(-SIZE, SIZE):
                x, y = x1+i*(x1-x2), y1+i*(y1-y2)
                if 0 <= x < SIZE and 0 <= y < SIZE:
                    antinodes.add((x, y))
    return len(antinodes)

print(silverstar())
print(goldstar())