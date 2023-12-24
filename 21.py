import useful
from time import time

lines = useful.get_lines("21.txt")

def get_count(start, delta, even):
    sr, sc = start
    count = 0
    for r in range(max(0, sr-delta), min(sr+delta+1, len(lines))):
        for c in range(max(0, sc-delta), min(sc+delta+1, len(lines[0]))):
            dist = abs(sr-r)+abs(sc-c)
            if dist <= delta:
                if lines[r][c] != '#' and dist % 2 == (0 if even else 1):
                    try:
                        if not (lines[r-1][c] == lines[r][c-1] == lines[r+1][c] == lines[r][c+1] == '#'):
                            count += 1
                    except IndexError: # Was lazy
                        count += 1
    return count

def silverstar():
    return get_count((65, 65), 64, True)

def goldstar():
    n = 202300
    return ((n*(n-2)+1)*get_count((65, 65), 1000, False) +
                    n*n*get_count((65, 65), 1000, True) +
                        get_count((0, 65), 130, True) +
                        get_count((130, 65), 130, True) +
                        get_count((65, 0), 130, True) +
                        get_count((65, 130), 130, True) +
                  (n-1)*get_count((0, 0), 195, False) +
                  (n-1)*get_count((130, 130), 195, False) +
                  (n-1)*get_count((0, 130), 195, False) +
                  (n-1)*get_count((130, 0), 195, False) +
                      n*get_count((0, 0), 64, True) +
                      n*get_count((130, 130), 64, True) +
                      n*get_count((0, 130), 64, True) +
                      n*get_count((130, 0), 64, True))


if __name__ == '__main__':
    t1 = time()
    print(f"Silver star: {silverstar()}")
    print(f"Gold star: {goldstar()}")
    t2 = time()
    print(f'took {round((t2-t1)*1000)} ms')