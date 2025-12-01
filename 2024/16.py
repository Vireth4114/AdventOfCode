import useful
from operator import add, sub
from collections import defaultdict
import heapq as hq

lines = useful.get_list_lines('16')

nodes = set()

def get_neighbors(x, y, nodes=nodes):
    neighbors = dict()
    for i, j in ((0, 1), (0, -1), (1, 0), (-1, 0)):
        pos = (x+i, y+j)
        a = 0
        while lines[pos[0]][pos[1]] != '#':
            a += 1
            pos = tuple(map(add, pos, (i, j)))
            if pos in nodes:
                neighbors[pos] = a+1
    return neighbors

def sign(x):
    if x == 0:
        return 0
    return x//abs(x)

def star():
    for idx, line in enumerate(lines):
        for idx2, c in enumerate(line):
            if c == '#':
                continue
            if c == 'S':
                start = (idx, idx2)
                nodes.add((idx, idx2))
            if c == 'E':
                end = (idx, idx2)
                nodes.add((idx, idx2))
            neighbors = [lines[idx+1][idx2], lines[idx-1][idx2], lines[idx][idx2+1], lines[idx][idx2-1]]
            if neighbors.count('.') > 2:
                nodes.add((idx, idx2))
            if neighbors[:2] != ['.', '.'] and neighbors[2:] != ['.', '.']:
                nodes.add((idx, idx2))

    tree = dict()

    for idx, line in enumerate(lines):
        for idx2, line2 in enumerate(line):
            if (idx, idx2) in nodes:
                tree[(idx, idx2)] = get_neighbors(idx, idx2)
    previous = defaultdict(set)
    distances = {}
    heap = [(0, start)]
    while heap:
        dist, node = hq.heappop(heap)
        if node in distances:
            continue
        distances[node] = dist 
        for neighbor, weight in tree[node].items():
            if neighbor not in distances:
                previous[neighbor].add(node)
                hq.heappush(heap, (dist + weight + 1000, neighbor))

    print(distances[end])

    normal_end = end

    prev_res = 0
    while True:
        end = normal_end
        while end != start:
            if len(previous[end]) > 1:
                prev = next(iter(previous[end]))
                previous[end].remove(prev)
            else:
                prev = next(iter(previous[end]))
            dir = (sign(end[0] - prev[0]), sign(end[1] - prev[1]))
            pos = end
            while pos != prev:
                lines[pos[0]][pos[1]] = 'X'
                pos = tuple(map(sub, pos, dir))
            end = prev
        lines[start[0]][start[1]] = 'X'
        res = 0
        for line in lines:
            for c in line:
                if c == 'X':
                    res += 1
        if res == prev_res:
            print(res)
            break
        prev_res = res

star()