import useful
from functools import cache

patterns, designs = useful.get_lines_pure('19').split('\n\n')

patterns = patterns.split(', ')
designs = designs.splitlines()

@cache
def silver(design, pointer=0):
    if pointer == len(design):
        return True
    for pattern in patterns:
        if design[pointer:].startswith(pattern):
            if silver(design, pointer + len(pattern)):
                return True
    return False

@cache
def gold(design, pointer=0):
    if pointer == len(design):
        return 1
    res = 0
    for pattern in patterns:
        if design[pointer:].startswith(pattern):
            res += gold(design, pointer + len(pattern))
    return res

print(sum(silver(design) for design in designs))
print(sum(gold(design) for design in designs))

