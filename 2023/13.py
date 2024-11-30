import useful
from itertools import groupby

lineslist = [list(group) for k, group in groupby(useful.get_lines("13.txt"), bool) if k]

def is_smudged(list1, list2):
    if len(list1) == 0:
        return False
    line1 = ''.join(list1)
    line2 = ''.join(list2)
    total = 0
    for c in range(len(line1)):
        if line1[c] != line2[c]:
            total += 1
    return total == 1

def process(lines, multiplier, smudge):
    stack = []
    for idx, line in enumerate(lines):
        if idx > 0:
            minlen = min(len(stack), len(lines)-idx)

            if not smudge and stack[-1:-1-minlen:-1] == lines[idx:idx+minlen]:
                return idx*multiplier
            
            if smudge and is_smudged(stack[-1:-1-minlen:-1], lines[idx:idx+minlen]):
                return idx*multiplier

        stack.append(line)
    return 0

def star(smudge):
    result = 0
    for idxlist, lines in enumerate(lineslist):
        result += process(lines, 100, smudge)
        
        columns = [''.join(i) for i in zip(*[list(line) for line in lines])]
        result += process(columns, 1, smudge)
    return result

if __name__ == '__main__':
    print(f"Silver star: {star(False)}")
    print(f"Gold star: {star(True)}")