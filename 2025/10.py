import useful
import re
from itertools import combinations_with_replacement, product
import sympy as sp

lines = [re.match(r'(\[.*\]) (\(.*\) )*(\{.*\})', line).groups() for line in useful.get_lines("10")]

def press_button(template, button):
    for num in button:
        template[num] ^= 1
    return template


def press_button2(template, button):
    for num in button:
        template[num] += 1
    return template

def find_lowest_numbers_button(template, buttons, target_template):
    i = 0
    while True:
        i += 1
        for comb in combinations_with_replacement(buttons, i):
            template = [0] * len(target_template)
            for button in comb:
                template = press_button(template, button)
            if template == target_template:
                return i

res = 0
for idx, line in enumerate(lines):
    target_template, buttons, voltages = line
    target_template = [0 if i == '.' else 1 for i in target_template.replace('[', '').replace(']', '')]
    buttons = [useful.get_numbers(wire) for wire in buttons.split(')') if wire]
    buttons = [b for b in buttons if b]
    voltages = useful.get_numbers(voltages)
    variables = sp.symbols(f'x0:{len(buttons)}')
    to_solve = []
    for i, volt in enumerate(voltages):
        var_volt = sum(variables[idx] for idx, b in enumerate(buttons) if i in b) - volt
        to_solve.append(var_volt)
    for j in range(11):
        sol = sp.solve(to_solve, [k for i, k in enumerate(variables) if i != j], dict=True, integer=True) or [None]
        print(sol)
        if sol[0] and all('/' not in str(v) for v in sol[0].values()):
            break
    else:
        print("jsp")
        exit()
    sol = sol[0]
    free_symbols = set()
    for s in sol.values():
        free_symbols.update(s.free_symbols)
    free_symbols = list(free_symbols)

    idx_free_symbol = [int(str(s).removeprefix('x')) for s in free_symbols]

    lambdas = {k: sp.lambdify(free_symbols, v, "math") for k, v in sol.items()}

    min_sum = float('inf')
    for combo in product(range(100), repeat=len(free_symbols)):
        vals = {k: f(*combo) for k, f in lambdas.items()}
        if all(v >= 0 for v in vals.values()):
            total = int(sum(vals.values()) + sum(combo))
            if total < min_sum:
                alls = [0] * len(buttons)
                for k, v in vals.items():
                    alls[int(str(k).removeprefix('x'))] = v
                for c_idx, c in enumerate(combo):
                    alls[idx_free_symbol[c_idx]] = c
                voltage_check = [0] * len(voltages)
                for c_idx, c in enumerate(alls):
                    for _ in range(c):
                        voltage_check = press_button2(voltage_check, buttons[c_idx])
                
                if voltage_check == voltages:
                    min_sum = total
    print(idx, min_sum)
    res += min_sum

print(res)