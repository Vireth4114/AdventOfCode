import useful
from time import time
from functools import cache

lines = useful.get_tuple_lines("14.txt")

@cache
def do_gravity(lines, dir):
    lines = [list(line) for line in lines]
    match dir:
        case 'N':
            for idxline, line in enumerate(lines[1:], 1):
                for idxchar, char in enumerate(line):
                    if char == 'O':
                        i = 1
                        while idxline-i >= 0 and lines[idxline-i][idxchar] == '.':
                            i += 1
                        lines[idxline][idxchar] = '.'
                        lines[idxline-i+1][idxchar] = 'O'
        case 'S':
            for idxline, line in reversed(list(enumerate(lines[:-1]))):
                for idxchar, char in enumerate(line):
                    if char == 'O':
                        i = 1
                        while idxline+i < len(lines) and lines[idxline+i][idxchar] == '.':
                            i += 1
                        lines[idxline][idxchar] = '.'
                        lines[idxline+i-1][idxchar] = 'O'
        case 'W':
            for idxline, line in enumerate(lines):
                for idxchar, char in enumerate(line[1:], 1):
                    if char == 'O':
                        i = 1
                        while idxchar-i >= 0 and lines[idxline][idxchar-i] == '.':
                            i += 1
                        lines[idxline][idxchar] = '.'
                        lines[idxline][idxchar-i+1] = 'O'
        case 'E':
            for idxline, line in enumerate(lines):
                for idxchar, char in reversed(list(enumerate(line[:-1]))):
                    if char == 'O':
                        i = 1
                        while idxchar+i < len(line) and lines[idxline][idxchar+i] == '.':
                            i += 1
                        lines[idxline][idxchar] = '.'
                        lines[idxline][idxchar+i-1] = 'O'
    sumation = 0
    for idxline, line in enumerate(lines):
        sumation += (len(lines)-idxline)*line.count('O')
    return tuple(tuple(line) for line in lines), sumation

def silverstar():
    return do_gravity(lines, 'N')[1]

def goldstar():
    # Probably doesn't work for all input
    # If not working, increase those two constants
    MAX_CYCLE = 1000
    CYCLING_FROM = 500

    testvalues = []
    newline = lines
    for i in range(1, MAX_CYCLE):
        newline = do_gravity(newline, 'N')[0]
        newline = do_gravity(newline, 'W')[0]
        newline = do_gravity(newline, 'S')[0]
        newline, sumation = do_gravity(newline, 'E')

        if i >= CYCLING_FROM:
            testvalues.append(sumation)
            
    for c in range(2, len(testvalues)):
        if testvalues[:c] == testvalues[c:2*c]:
            return testvalues[1_000_000_000%c - CYCLING_FROM%c]

if __name__ == '__main__':
    t1 = time()
    print(f"Silver star: {silverstar()}")
    print(f"Gold star: {goldstar()}")
    t2 = time()
    print(f'took {round((t2-t1)*1000)} ms')