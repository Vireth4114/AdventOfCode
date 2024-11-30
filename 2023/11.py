import useful
from itertools import combinations

lines = useful.get_lines("11.txt")

def process(value=2):
    list_galaxies = [[l, c] for c in range(len(lines[0])) for l in range(len(lines)) if lines[l][c] == '#']

    line_to_insert = [idx for idx, line in enumerate(lines) if line.count('#') == 0]
    col_to_insert = [col for col in range(len(lines[0])) if [line[col] for line in lines].count('#') == 0]

    for idx in reversed(col_to_insert):
        for galaxy in list_galaxies:
            if galaxy[1] > idx:
                galaxy[1] += value-1

    for idx in reversed(line_to_insert):
        for galaxy in list_galaxies:
            if galaxy[0] > idx:
                galaxy[0] += value-1

    return sum(abs(galaxy2[0]-galaxy1[0])+abs(galaxy2[1]-galaxy1[1]) for galaxy1, galaxy2 in combinations(list_galaxies, 2))

if __name__ == '__main__':
    print(f"Silver star : {process()}")
    print(f"Gold star : {process(1_000_000)}")