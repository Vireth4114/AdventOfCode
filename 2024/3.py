import useful
import re

lines = useful.get_lines("3")

def silverstar():
    return sum(int(m.group(1)) * int(m.group(2)) for line in lines for m in re.finditer(r"mul\((\d+),(\d+)\)", line))

def goldstar():
    return sum(int(m.group(1)) * int(m.group(2)) for line in lines for m in re.finditer(r"\)(\d+),(\d+)\(lum(?=(.(?!\)\(t'nod))*(\)\(od.*\)\(t'nod.*)*$)", line[::-1]))

if __name__ == "__main__":
    print(silverstar())
    print(goldstar())