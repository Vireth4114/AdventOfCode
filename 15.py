import useful
import re

lines = useful.get_lines("15.txt")[0].split(',')

def silverstar(lines=lines):
    sumation = 0
    for entry in lines:
        current = 0
        for c in entry:
            current += ord(c)
            current *= 17
            current %= 256
        sumation += current
    return sumation

def goldstar(lines=lines):
    boxes = [[] for _ in range(256)]
    parselines = [[re.split('[-=]', line), re.findall('[-=]', line)[0]] for line in lines]
    sumation = 0
    for entry in parselines:
        current = 0
        for c in entry[0][0]:
            current += ord(c)
            current *= 17
            current %= 256

        wheretoadd = len(boxes[current])
        if entry[0][0] in [e[0] for e in boxes[current]]:
            wheretoadd = [e[0] for e in boxes[current]].index(entry[0][0])
            boxes[current].pop(wheretoadd)
        if entry[1] == '=':
            boxes[current].insert(wheretoadd, entry[0])
        
    for idxbox, box in enumerate(boxes, 1):
        for idx, entry in enumerate(box, 1):
            sumation += idxbox*idx*int(entry[1])
    return sumation

if __name__ == '__main__':
    print(f"Silver star: {silverstar()}")
    print(f"Gold star: {goldstar()}")