import useful
import re
import math
from time import time

lines = useful.get_lines("19.txt")

workflows = dict()
shapes = []

finished = False
for line in lines:
    if line == '':
        finished = True
        continue

    if not finished:
        label, value = line[:-1].split('{')
        workflows[label] = [re.findall('[<>]?\w+', entry) for entry in value.split(',')]
    else:
        shapedict = dict()
        for entry in line[1:-1].split(','):
            label, value = entry.split('=')
            shapedict[label] = value
        shapes.append(shapedict)

def silverstar():
    result = 0
    for shape in shapes:
        curr_workflow = 'in'
        while curr_workflow not in ('R', 'A'):
            for rule in workflows[curr_workflow]:
                if len(rule) == 3:
                    if eval(shape[rule[0]]+rule[1]):
                        curr_workflow = rule[2]
                        break
                else:
                    curr_workflow = rule[0]
        if curr_workflow == 'A':
            result += sum(map(int, shape.values()))
    return result

def invert(cond):
    if cond[0] == '<':
        return '>' + str(int(cond[1:])-1)
    return '<' + str(int(cond[1:])+1)

def simplify(conditions):
    all_values = []
    for type in "xmas":
        minval = 0
        maxval = 4001
        for entry in [cond[1:] for cond in conditions if cond[0] == type]:
            if entry[0] == '<':
                maxval = min(maxval, int(entry[1:]))
            else:
                minval = max(minval, int(entry[1:]))
        all_values.append(max(0, maxval-minval-1))
    return math.prod(all_values)

def goldstar(curr_workflow='in', conditions=[]):
    if curr_workflow == 'R':
        return 0
    if curr_workflow == 'A':
        return simplify(conditions)
    
    result = 0
    nbappend = 0
    for rule in workflows[curr_workflow]:
        if len(rule) == 3:
            nbappend += 1
            conditions.append(rule[0]+rule[1])
            result += goldstar(rule[2], conditions)
            conditions.remove(rule[0]+rule[1])
            conditions.append(rule[0]+invert(rule[1]))
        else:
            result += goldstar(rule[0], conditions)
    del conditions[-nbappend:]
    return result

if __name__ == '__main__':
    t1 = time()
    print(f"Silver star: {silverstar()}")
    print(f"Gold star: {goldstar()}")
    t2 = time()
    print(f'took {round((t2-t1)*1000)} ms')