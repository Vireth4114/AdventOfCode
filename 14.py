import useful
from copy import deepcopy

lines = useful.get_list_lines("14.txt")

def do_gravity(lines, dir):
    match dir:
        case 'N':
            for idxline, line in enumerate(lines[1:], 1):
                for idxchar, char in enumerate(line):
                    if char == 'O':
                        for i in range(1, 1000):
                            if idxline-i >= 0 and lines[idxline-i][idxchar] == '.':
                                continue
                            else:
                                lines[idxline][idxchar] = '.'
                                lines[idxline-i+1][idxchar] = 'O'
                                break
        case 'S':
            for idxline, line in reversed(list(enumerate(lines[:-1]))):
                for idxchar, char in enumerate(line):
                    if char == 'O':
                        for i in range(1, 1000):
                            if idxline+i < len(lines) and lines[idxline+i][idxchar] == '.':
                                continue
                            else:
                                lines[idxline][idxchar] = '.'
                                lines[idxline+i-1][idxchar] = 'O'
                                break
        case 'W':
            for idxline, line in enumerate(lines):
                for idxchar, char in enumerate(line[1:], 1):
                    if char == 'O':
                        for i in range(1, 1000):
                            if idxchar-i >= 0 and lines[idxline][idxchar-i] == '.':
                                continue
                            else:
                                lines[idxline][idxchar] = '.'
                                lines[idxline][idxchar-i+1] = 'O'
                                break
        case 'E':
            for idxline, line in enumerate(lines):
                for idxchar, char in reversed(list(enumerate(line[:-1]))):
                    if char == 'O':
                        for i in range(1, 1000):
                            if idxchar+i < len(line) and lines[idxline][idxchar+i] == '.':
                                continue
                            else:
                                lines[idxline][idxchar] = '.'
                                lines[idxline][idxchar+i-1] = 'O'
                                break

def silverstar():
    do_gravity(lines, 'N')

    sumation = 0
    for idxline, line in enumerate(lines):
        sumation += (len(lines)-idxline)*line.count('O')
    return sumation

def goldstar():
    # Probably doesn't work for all input
    # If not working, increase those two constants
    MAX_CYCLE = 300
    CYCLING_FROM = 150

    testvalues = []
    for i in range(1, MAX_CYCLE):
        do_gravity(lines, 'N')
        do_gravity(lines, 'W')
        do_gravity(lines, 'S')
        do_gravity(lines, 'E')

        sumation = 0
        for idxline, line in enumerate(lines):
            sumation += (len(lines)-idxline)*line.count('O')
        if i >= CYCLING_FROM:
            testvalues.append(sumation)

    for c in range(2, len(testvalues)):
        if testvalues[:c] == testvalues[c:2*c]:
            return testvalues[1_000_000_000%c - CYCLING_FROM%c]

if __name__ == '__main__':
    print(f"Silver star: {silverstar()}")
    print(f"Gold star: {goldstar()}")