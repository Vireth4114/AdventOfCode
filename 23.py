import useful
from time import time
from sys import setrecursionlimit
setrecursionlimit(10000)

lines = useful.get_lines("23.txt")

slopes = {'<': (0, -1), '^': (-1, 0), '>': (0, 1), 'v': (1, 0)}

start = (0, lines[0].index('.'))
end = (len(lines)-1, lines[len(lines)-1].index('.'))

def get_neighbors_silver(position, visited):
    r, c = position
    for nr, nc in ((r-1, c), (r, c-1), (r+1, c), (r, c+1)):
        if not (0 <= nr < len(lines) and 0 <= nc < len(lines[0])):
            continue
        elif lines[nr][nc] in slopes and (nr, nc) not in visited:
            dr, dc = slopes[lines[nr][nc]]
            yield ((nr+dr, nc+dc), 2)
        elif lines[nr][nc] == '.' and (nr, nc) not in visited:
            yield ((nr, nc), 1)

def get_neighbors_gold(position, visited):
    r, c = position
    neighbors = []
    for nr, nc in ((r-1, c), (r, c-1), (r+1, c), (r, c+1)):
        if not (0 <= nr < len(lines) and 0 <= nc < len(lines[0])):
            continue
        elif lines[nr][nc] != '#' and (nr, nc) not in visited:
            neighbors.append((nr, nc))
    return neighbors

def silverstar(current=start, visited = []):
    if current == end:
        return 0
    
    visited.append(current)
    max_num = 0
    for neighbor, count in get_neighbors_silver(current, visited):
        if neighbor not in visited:
            max_num = max(max_num, silverstar(neighbor)+count)
    visited.remove(current)
    return max_num

def goldstar():
    vertices = [start, end]

    for r in range(len(lines)):
        for c in range(len(lines[0])):
            if lines[r][c] != '#':
                if len(get_neighbors_gold((r, c), ())) >= 3:
                    vertices.append((r, c))

    graph = {vertex: {} for vertex in vertices}

    for r, c in vertices:
        currents = [((r, c), 0)]
        visited = []

        while currents:
            current, count = currents.pop(0)
            if count != 0 and current in vertices:
                graph[(r, c)][current] = count
                continue
            visited.append(current)
            for neighbor in get_neighbors_gold(current, visited):
                currents.append((neighbor, count+1))
        
    seen = set()

    def get_longest(current):
        if current == end:
            return 0
        
        seen.add(current)
        result = 0
        for neighbor, value in graph[current].items():
            if neighbor not in seen:
                result = max(result, get_longest(neighbor)+value)
        seen.remove(current)
        return result

    return get_longest(start)

if __name__ == '__main__':
    t1 = time()
    print(f"Silver star: {silverstar()}")
    print(f"Gold star: {goldstar()}")
    t2 = time()
    print(f'took {round((t2-t1)*1000)} ms')