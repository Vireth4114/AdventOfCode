import useful
from heapq import heappush, heappop
from time import time

lines = useful.get_lines('17.txt')

def silverstar():
    tovisit = [(0, 0, 0, 0, 0, 0)]
    visited = set()
    while tovisit:
        current = heappop(tovisit)
        if current[1:3] == (len(lines)-1, len(lines[0])-1):
            return current[0]
        if current[1:] in visited:
            continue
        visited.add(current[1:])
        
        streak = current[-1]

        if streak < 3 and (0 <= current[1]+current[3] < len(lines) and 0 <= current[2]+current[4] < len(lines[0])):
            newstreak = current[-1]+1
            value = current[0] + int(lines[current[1]+current[3]][current[2]+current[4]])
            neighbor = (value, current[1]+current[3], current[2]+current[4], current[3], current[4], newstreak)
            heappush(tovisit, neighbor)

        for dir in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            if not (0 <= current[1]+dir[0] < len(lines) and 0 <= current[2]+dir[1] < len(lines[0])):
                continue
            if current[3] == dir[0] and current[4] == dir[1]:
                continue
            if current[3] == -dir[0] and current[4] == -dir[1]:
                continue
            value = current[0] + int(lines[current[1]+dir[0]][current[2]+dir[1]])
            neighbor = (value, current[1]+dir[0], current[2]+dir[1], dir[0], dir[1], 1)
            heappush(tovisit, neighbor)

def goldstar():
    tovisit = [(0, 0, 0, 0, 0, 0)]
    visited = set()
    while tovisit:
        current = heappop(tovisit)
        if current[1:3] == (len(lines)-1, len(lines[0])-1):
            return current[0]
        if current[1:] in visited:
            continue
        visited.add(current[1:])
        
        streak = current[-1]

        if streak < 10 and (0 <= current[1]+current[3] < len(lines) and 0 <= current[2]+current[4] < len(lines[0])):
            newstreak = current[-1]+1
            value = current[0] + int(lines[current[1]+current[3]][current[2]+current[4]])
            neighbor = (value, current[1]+current[3], current[2]+current[4], current[3], current[4], newstreak)
            heappush(tovisit, neighbor)

        if streak >= 4 or current[1:3] == (0, 0):
            for dir in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                if not (0 <= current[1]+dir[0] < len(lines) and 0 <= current[2]+dir[1] < len(lines[0])):
                    continue
                if current[3] == dir[0] and current[4] == dir[1]:
                    continue
                if current[3] == -dir[0] and current[4] == -dir[1]:
                    continue
                value = current[0] + int(lines[current[1]+dir[0]][current[2]+dir[1]])
                neighbor = (value, current[1]+dir[0], current[2]+dir[1], dir[0], dir[1], 1)
                heappush(tovisit, neighbor)

if __name__ == '__main__':
    t1 = time()
    print(f"Silver star: {silverstar()}")
    print(f"Gold star: {goldstar()}")
    t2 = time()
    print(f'took {round((t2-t1)*1000)} ms')