import useful
import re
from math import lcm

lines = useful.get_lines("8.txt")

sequence = lines[0]
dict_node = dict()
for i in range(2, len(lines)):
    nodes = re.findall('[0-9A-Z]+', lines[i])
    dict_node[nodes[0]] = nodes[1:]

def process(currents):
    counts = []
    for i in range(len(currents)):
        count = 0
        while currents[i][-1] != 'Z':
            for c in sequence:
                if c == 'R':
                    currents[i] = dict_node[currents[i]][1]
                else:
                    currents[i] = dict_node[currents[i]][0]
                count += 1
                if currents[i][-1] == 'Z':
                    counts.append(count)
                    break
    return lcm(*counts)

if __name__ == '__main__':
    print(f"Silver star: {process(['AAA'])}")
    print(f"Gold star: {process([node for node in dict_node if node[-1] == 'A'])}")