import re
import heapq as hq
from collections import defaultdict

def get_lines_pure(filename):
    with open(f'input/{filename}', 'r') as file:
        lines = file.read()
    return lines

def get_lines(filename):
    with open(f'input/{filename}', 'r') as file:
        lines = file.read().splitlines()
    return lines

def get_list_lines(filename):
    with open(f'input/{filename}', 'r') as file:
        lines = file.read().splitlines()
    return [list(line) for line in lines]

def get_tuple_lines(filename):
    with open(f'input/{filename}', 'r') as file:
        lines = file.read().splitlines()
    return tuple(tuple(line) for line in lines)

def get_lines_with_newline(filename):
    with open(f'input/{filename}', 'r') as file:
        lines = file.readlines()
    return lines

def get_numbers(line):
    return list(map(int, re.findall(r"-?\d+", line)))


def dijkstra(get_neighbors, start):
    previous = defaultdict(set)
    distances = {}
    heap = [(0, start)]
    while heap:
        dist, node = hq.heappop(heap)
        if node in distances:
            continue
        distances[node] = dist 
        for neighbor, weight in get_neighbors(node).items():
            if neighbor not in distances:
                previous[neighbor].add(node)
                hq.heappush(heap, (dist + weight, neighbor))
    return distances, previous
    
def get_neighbors(grid, r, c):
    neighbors = {}
    rows, cols = len(grid), len(grid[0])
    for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        nr, nc = r + dr, c + dc
        if 0 <= nr < rows and 0 <= nc < cols:
            neighbors[(nr, nc)] = grid[nr][nc]
    return neighbors

def get_with_diag_neighbors(grid, r, c):
    neighbors = {}
    rows, cols = len(grid), len(grid[0])
    for dr in [-1, 0, 1]:
        for dc in [-1, 0, 1]:
            if dr == 0 and dc == 0:
                continue
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols:
                neighbors[(nr, nc)] = grid[nr][nc]
    return neighbors