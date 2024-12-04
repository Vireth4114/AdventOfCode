import useful
import re

lines = useful.get_lines("3")

def apply_regex(regex, lines=lines):
    return sum(int(m.group(1)) * int(m.group(2)) for line in lines for m in re.finditer(regex, line[::-1]))


if __name__ == "__main__":
    print(apply_regex(r"mul\((\d+),(\d+)\)"))
    print(apply_regex(r"\)(\d+),(\d+)\(lum(?=(.(?!\)\(t'nod))*(\)\(od.*\)\(t'nod.*)*$)"))