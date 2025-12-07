import useful
from collections import defaultdict

lines = useful.get_list_lines("7")

first_beam = (1, lines[0].index('S'))
beams = {first_beam}
muls = {first_beam: 1}

res = 0

while next(iter(beams))[0] < len(lines) - 1:
    next_beams = set()
    next_muls = defaultdict(int)
    for beam in beams:
        mul = muls[beam]
        if lines[beam[0] + 1][beam[1]] == '^':
            next_beams.add((beam[0] + 1, beam[1] - 1))
            next_muls[(beam[0] + 1, beam[1] - 1)] += mul
            next_beams.add((beam[0] + 1, beam[1] + 1))
            next_muls[(beam[0] + 1, beam[1] + 1)] += mul
            res += 1
        else:
            next_beams.add((beam[0] + 1, beam[1]))
            next_muls[(beam[0] + 1, beam[1])] += mul
    beams = next_beams
    muls = next_muls

print(res)
print(sum(muls.values()))