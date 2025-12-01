import useful
import heapq as hq

lines = useful.get_list_lines('20')
SIZE = 20

def dijkstra_from(start):
    def get_neighbors(node):
        x, y = node
        for i, j in ((0, 1), (1, 0), (0, -1), (-1, 0)):
            if 0 <= x+i < len(lines) and 0 <= y+j < len(lines[0]):
                if lines[x+i][y+j] in '.ES':
                    yield (x+i, y+j)

    distances = {}
    heap = [(0, start)]
    while heap:
        dist, node = hq.heappop(heap)
        if node in distances:
            continue
        distances[node] = dist
        for neighbor in get_neighbors(node):
            if neighbor not in distances:
                hq.heappush(heap, (dist + 1, neighbor))
    return distances

for idx, line in enumerate(lines):
    for idx2, c in enumerate(line):
        if c == 'S':
            start = (idx, idx2)
        if c == 'E':
            end = (idx, idx2)

dist_start = dijkstra_from(start)
dist_end = dijkstra_from(end)
no_cheat = dist_start[end]
res = 0

for idx, line in enumerate(lines):
    for idx2, c in enumerate(line):
        if c == '#': continue
        for idx3, line2 in enumerate(lines[max(0, idx - SIZE):min(idx + SIZE + 1, len(lines))], max(0, idx - SIZE)):
            smolsize = SIZE - abs(idx - idx3)
            for idx4, c2 in enumerate(line2[max(0, idx2 - smolsize):min(idx2 + smolsize + 1, len(line2))], max(0, idx2 - smolsize)):
                if c2 == '#': continue
                abs_dist = abs(idx-idx3) + abs(idx2-idx4)
                if abs_dist > SIZE: continue
                dist = dist_start[(idx, idx2)] + dist_end[(idx3, idx4)] + abs_dist
                if no_cheat - dist >= 100:
                    res += 1

print(res)

