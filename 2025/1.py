import useful

lines = useful.get_list_lines("1")

silver, gold = 0, 0
pos = 50
for line in lines:
    num = int(''.join(line[1:]))
    if line[0] == 'L':
        if pos == 0:
            gold -= 1
        pos -= num
        gold += (pos // -100) + 1
    else:
        pos += num
        gold += pos // 100
    pos %= 100
    if pos == 0:
        silver += 1

print(silver)
print(gold)