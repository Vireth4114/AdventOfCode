from operator import sub
from itertools import product, permutations, islice
import useful
import time

def translate_digit(code):
    code_tab = [(2, 1)]
    for c in code:
        if c == 'A':
            code_tab.append((3, 2))
        elif c == '0':
            code_tab.append((3, 1))
        else:
            code_tab.append((3 - (ord(c) - 46)//3, (ord(c) - 46)%3))
    return code_tab

def translate_arrow(code):
    code_tab = [(0, 2)]
    for c in code:
        match c:
            case '^':
                code_tab.append((0, 1))
            case 'v':
                code_tab.append((1, 1))
            case '<':
                code_tab.append((1, 0))
            case '>':
                code_tab.append((1, 2))
            case 'A':
                code_tab.append((0, 2))
    return code_tab

def some_conversion(new_code):
    str = []
    for idx, digit in enumerate(new_code[:-1]):
        next_digit = new_code[(idx + 1)]
        delta_digit = tuple(map(sub, next_digit, digit))
        inputs = []
        if delta_digit[1] > 0:
            inputs.extend(['>'] * abs(delta_digit[1]))
        if delta_digit[0] < 0:
            inputs.extend(['^'] * abs(delta_digit[0]))
        if delta_digit[0] > 0:
            inputs.extend(['v'] * abs(delta_digit[0]))
        if delta_digit[1] < 0:
            inputs.extend(['<'] * abs(delta_digit[1]))
        str.append(tuple(''.join(p) for p in set(permutations(inputs))))
    my_set = {'A'.join(s) + 'A' for s in product(*str)}
    min_len = min(len(s) for s in my_set)
    return {s for s in my_set if len(s) == min_len}

start = time.time()

code_file = useful.get_lines('21')
res = 0
for code in code_file:
    codes = some_conversion(translate_digit(code))
    for _ in range(4):
        codes2 = set()
        for code2 in codes:
            codes2.update(some_conversion(translate_arrow(code2)))
        min_len = min(len(s) for s in codes2)
        codes = {s for s in codes2 if len(s) == min_len}
        print(next(iter(codes)))
        print(len(next(iter(codes))))
    val = len(next(iter(codes)))
    res += val * int(code[:-1])
print(res)
print(f'Time: {time.time() - start}s')

"""
<AA>A<<vA>^A>Av<AA>^Av<A>A^A
<v<A>^>AAvA^A<v<AA>A^>AvA<^A>AvA^A<vA<A>^>AAvA<^A>A<vA<A>^>AvA^A<A>A
"""