import heapq as hq
import useful
import time

SIZE = 70

start_time = time.time()

i = 1024
start = (0, 0)
end = (SIZE, SIZE)
bytes = [tuple(useful.get_numbers(line)) for line in useful.get_lines('18')]
inf = 1024
sup = len(bytes)

def get_neighbors(node, lines):
    x, y = node
    for i, j in ((1, 0), (0, 1), (-1, 0), (0, -1)):
        if 0 <= x+i <= SIZE and 0 <= y+j <= SIZE:
            if (x+i, y+j) not in lines:
                yield (x+i, y+j)

while True:
    lines = set(bytes[:i])
    res = 0
    distances = {}
    heap = [(0, start)]
    while heap:
        dist, node = hq.heappop(heap)
        if node in distances:
            continue
        distances[node] = dist
        for neighbor in get_neighbors(node, lines):
            if neighbor not in distances:
                res += 1
                hq.heappush(heap, (dist + 1, neighbor))
    if i == 1024:
        print(distances[end])
    
    if end in distances:
        inf = i
    else:
        sup = i

    if inf == sup-1 or inf == sup:
        break

    i = (sup+inf)//2

print(','.join(str(c) for c in bytes[i-1]))
print(f"{(time.time() - start_time)*1000:.3f}ms")