import useful
from math import prod
import re

lines = [line+' #' for line in useful.get_lines("6")]

silver_numbers = list(zip(*[useful.get_numbers(line) for line in lines[:4]]))

ptr = 0
gold_numbers = []
while ptr < len(lines[0]) - 2:
    col_num = []
    while lines[4][ptr+1] == ' ':
        col_num.append(int(''.join(line[ptr] for line in lines[:4])))
        ptr += 1
    gold_numbers.append(col_num)
    ptr += 1

ops = [sum if i == '+' else prod for i in re.findall(r'[+*]', lines[4])]

print(sum(ops[idx](silver_numbers[idx]) for idx in range(len(ops))))
print(sum(ops[idx](gold_numbers[idx]) for idx in range(len(ops))))