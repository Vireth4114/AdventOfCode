import useful

lines = useful.get_list_lines('12')

region = set()
regions = set()
seen = set()
seen2 = set()

def get_neighbors(x, y):
    char = lines[x][y]
    for i, j in ((0, 1), (1, 0), (0, -1), (-1, 0)):
        if not (0 <= x+i < len(lines) and 0 <= y+j < len(lines[0])):
            cond = False
        else:
            cond = lines[x+i][y+j] == char
            if cond and (x+i, y+j) in seen:
                continue
        yield x+i, y+j, cond

def add_to_seen2(xrel, yrel, x, y, perimeters):
    seen2.add((xrel, yrel, x, y))
    for i, j in ((0, 1), (1, 0), (0, -1), (-1, 0)):
        if (xrel, yrel, x+i, y+j) in perimeters and (xrel, yrel, x+i, y+j) not in seen2:
            add_to_seen2(xrel, yrel, x+i, y+j, perimeters)

def add_to_region(idx, idx2):
    region.add((idx, idx2))
    seen.add((idx, idx2))
    perimeters = []
    for x, y, equal in get_neighbors(idx, idx2):
        if equal:
            perimeters.extend(add_to_region(x, y))
        else:
            perimeters.append((idx-x, idx2-y, x, y))
    return perimeters

res = 0
for idx, line in enumerate(lines):
    for idx2, c in enumerate(line):
        if (idx, idx2) in seen:
            continue
        region = set()
        seen2 = set()
        perimeters = add_to_region(idx, idx2)
        peri = 0
        for xrel, yrel, x, y in perimeters:
            if (xrel, yrel, x, y) in seen2:
                continue
            add_to_seen2(xrel, yrel, x, y, perimeters)
            peri += 1
        res += len(region)*peri
print(res)