import useful

lines = useful.get_list_lines("4")
silver, gold = 0, 0
loop = True
first_loop = True

while loop:
    loop = False
    next_lines = [list(line) for line in lines]

    for r, line in enumerate(lines):
        for c, case in enumerate(line):
            if case != '@':
                continue
            if list(useful.get_with_diag_neighbors(lines, r, c).values()).count('@') < 4:
                gold += 1
                if first_loop:
                    silver += 1
                loop = True
                next_lines[r][c] = '.'

    first_loop = False
    lines = [line for line in next_lines]

print(silver, gold)