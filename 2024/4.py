import useful
from itertools import product

lines = useful.get_lines('4')

def silverstar():
    res = 0
    for idx, line in enumerate(lines):
        for idx2, c in enumerate(line):
            if c != 'S':
                continue
            
            for xfact, yfact in product([-1, 0, 1], repeat=2):
                if (xfact, yfact) == (0, 0):
                    continue

                if not (0 <= idx+xfact*3 < len(lines) and 0 <= idx2+yfact*3 < len(lines)):
                    continue
                
                if ''.join(lines[idx+i*xfact][idx2+i*yfact] for i in range(3, 0, -1)) == 'XMA':
                    res += 1
    return res

def goldstar():
    res = 0
    for idx, line in enumerate(lines[1:-1], 1):
        for idx2, c in enumerate(line[1:-1], 1):
            if c != 'A':
                continue

            diag1 = lines[idx-1][idx2-1] + c + lines[idx+1][idx2+1]
            diag2 = lines[idx+1][idx2-1] + c + lines[idx-1][idx2+1]

            if diag1 in ('MAS', 'SAM') and diag2 in ('MAS', 'SAM'):
                res += 1
    return res

if __name__ == '__main__':
    print(silverstar())
    print(goldstar())