import useful
from time import time

lines = useful.get_lines("18.txt")

def star(type):
    current = [1, 1]
    corners = [current]
    totalext = 0

    for line in lines:
        dir, value, hex = line.split(' ')
        value = int(value)
        if type == 'gold':
            dir = ['R', 'D', 'L', 'U'][int(hex[-2])]
            value = int(hex[2:-2], 16)
        
        totalext += value

        match dir:
            case 'R':
                truedir = [0*value, 1*value]
            case 'D':
                truedir = [1*value, 0*value]
            case 'L':
                truedir = [0*value, -1*value]
            case 'U':
                truedir = [-1*value, 0*value]
        
        current[1] += truedir[1]
        current[0] += truedir[0]
        corners.append(current.copy())

    count = 0
    for idxcorn, corner in enumerate(corners[:-1]):
        nextcorner = corners[idxcorn+1]
        count += corner[0]*nextcorner[1]-corner[1]*nextcorner[0]

    return abs(count//2)+totalext//2+1


if __name__ == '__main__':
    t1 = time()
    print(f"Silver star: {star('silver')}")
    print(f"Gold star: {star('gold')}")
    t2 = time()
    print(f'took {round((t2-t1)*1000)} ms')