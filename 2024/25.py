import useful

lines = [list(zip(*l.splitlines())) for l in useful.get_lines_pure('25').split('\n\n')]

keys = []
locks = []

for idx_kl, key_lock in enumerate(lines):
    pins = [line.count('#') - 1 for line in key_lock]
    if key_lock[0][0] == '.':
        keys.append(pins)
    else:
        locks.append(pins)
res = 0
for key in keys:
    for lock in locks:
        if all(k+l <= 5 for k, l in zip(key, lock)):
            res += 1
print(res)