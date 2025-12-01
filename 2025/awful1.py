import useful

lines = useful.get_list_lines("1")

silver, gold = 0, 0
pos = 50
for line in lines:
    num = int(''.join(line[1:]))
    for i in range(num):
        if line[0] == 'L':
            pos -= 1
        else:
            pos += 1
        pos %= 100
        if pos == 0:
            gold += 1
    if pos == 0:
        silver += 1

print(silver)
print(gold)