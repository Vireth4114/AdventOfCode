import useful
import re

lines = useful.get_lines("2.txt")

def silverstar():
    otherlines = lines.copy()
    for line in lines:
        maxs = {'red': 12, 'green': 13, 'blue': 14}
        for batch in re.findall("\d+ green|\d+ blue|\d+ red", line):
            value, color = batch.split(' ')
            if int(value) > maxs[color]:
                otherlines.remove(line)
                break
    return sum(int(re.search('\d+', line)[0]) for line in otherlines)

def goldstar():
    powers = []
    for line in lines:
        mins = {'red': 0, 'green': 0, 'blue': 0}
        for batch in re.findall("\d+ green|\d+ blue|\d+ red", line):
            value, color = batch.split(' ')
            if int(value) > mins[color]:
                mins[color] = int(value)
        powers.append(useful.product(mins.values()))
    return sum(powers)

if __name__ == '__main__':
    print(f"Silver star : {silverstar()}")
    print(f"Gold star : {goldstar()}")