import useful
import heapq
from collections import Counter
from math import prod

points = [useful.get_numbers(line) for line in useful.get_lines("8")]

def get_comp_distance(a, b):
    return (a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2 + (a[2] - b[2]) ** 2

table = {i: i for i in range(len(points))}

dist = dict()
for idx, point in enumerate(points):
    for idx2, point2 in enumerate(points):
        if idx != idx2:
            dist[frozenset((idx, idx2))] = get_comp_distance(point, point2)

sorted_dist = sorted(dist.items(), key=lambda x: x[1])

i = 0
while len(set(table.values())) > 1:
    min_idx, min_idx2 = sorted_dist[i][0]
    dest, src = table[min_idx], table[min_idx2]
    for key, value in table.items():
        if value == src:
            table[key] = dest
    i += 1
    if i == 1000:
        print(prod(heapq.nlargest(3, Counter(table.values()).values())))

idx, idx2 = sorted_dist[i - 1][0]
print(points[idx][0] * points[idx2][0])