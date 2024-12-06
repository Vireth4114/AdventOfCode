import useful
import time

start = time.time()

file_lines = useful.get_list_lines('6')

def get_guard(lines):
    for line_idx, line in enumerate(lines):
        for idx, c in enumerate(line):
            if c == '^':
                return (idx, line_idx)

# Return the number of visited blocks and if it finished
def visit(lines):
    visited = set()
    visited_dir = set()
    guard = get_guard(lines)
    dir = (0, -1)
    while True:
        visited.add(guard)
        if (guard, dir) in visited_dir:
            return visited, False
        visited_dir.add((guard, dir))
        new_pos = (guard[0] + dir[0], guard[1] + dir[1])
        if not (0 <= new_pos[0] < len(lines[0]) and 0 <= new_pos[1] < len(lines)):
            return visited, True
        while lines[new_pos[1]][new_pos[0]] == '#':
            match dir:
                case (-1, 0):
                    dir = (0, -1)
                case (0, 1):
                    dir = (-1, 0)
                case (1, 0):
                    dir = (0, 1)
                case (0, -1):
                    dir = (1, 0)
            
            new_pos = (guard[0] + dir[0], guard[1] + dir[1])
            if not (0 <= new_pos[0] < len(lines[0]) and 0 <= new_pos[1] < len(lines)):
                return visited, True
        guard = new_pos

visited, _ = visit(file_lines)
print(len(visited))

res = 0
for idx, line in enumerate(file_lines):
    for idx2, c in enumerate(line):
        if (idx2, idx) not in visited or c == '^':
            continue
        lines = [list(line) for line in file_lines]
        lines[idx][idx2] = '#'
        if not visit(lines)[1]:
            res += 1

print(res)
print(f"took {time.time() - start:.3}s")