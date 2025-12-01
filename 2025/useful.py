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
    
