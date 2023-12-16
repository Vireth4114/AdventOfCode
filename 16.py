import useful
from copy import deepcopy
from time import time

lines = useful.get_list_lines("16.txt")

def star(mode):
    if mode == 'gold':
        beginning = [tuple([c, -1, (0, 1)]) for c in range(len(lines))]+\
                    [tuple([c, len(lines[0]), (0, -1)]) for c in range(len(lines))]+\
                    [tuple([-1, c, (1, 0)]) for c in range(len(lines[0]))]+\
                    [tuple([len(lines), c, (-1, 0)]) for c in range(len(lines[0]))]
    else:
        beginning = [(0, -1, (0, 1))]

    max_result = -1
    for start in beginning:
        set_all = set()
        cache = set()
        currents = set([start])
        while currents != set():
            for current in currents.copy():
                dir = current[2]
                currents.remove(current)
                set_all.add(tuple((current[0], current[1])))
                cache.add(current)
                if not (0 <= current[0]+dir[0] < len(lines) and 0 <= current[1]+dir[1] < len(lines[0])):
                    break

                thing_to_add = []
                mirror = lines[current[0]+dir[0]][current[1]+dir[1]]
                match mirror:
                    case '.':
                        thing_to_add.append(dir)
                    case '/':
                        thing_to_add.append((-1*dir[1], -1*dir[0]))
                    case '\\':
                        thing_to_add.append((dir[1], dir[0]))
                    case '|':
                        if dir[0] == 0:
                            thing_to_add.append((1, 0))
                            thing_to_add.append((-1, 0))
                        else:
                            thing_to_add.append(dir)
                    case '-':
                        if dir[1] == 0:
                            thing_to_add.append((0, 1))
                            thing_to_add.append((0, -1))
                        else:
                            thing_to_add.append(dir)
                
                for thing in thing_to_add:
                    addition = tuple((current[0]+dir[0], current[1]+dir[1], thing))
                    if addition not in cache:
                        currents.add(addition)
        set_all.remove(tuple((start[0], start[1])))

        if len(set_all) > max_result:
            max_result = len(set_all)

    return max_result

if __name__ == '__main__':
    t1 = time()
    print(f"Silver star: {star('silver')}")
    print(f"Gold star: {star('gold')}")
    t2 = time()
    print(f'took {round((t2-t1)*1000)} ms')