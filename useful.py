import re

def get_lines(filename):
    with open(f'input/{filename}', 'r') as file:
        lines = file.read().splitlines()
    return lines

def get_lines_with_newline(filename):
    with open(f'input/{filename}', 'r') as file:
        lines = file.readlines()
    return lines

def product(iterable):
    a = 1
    for element in iterable:
        a *= element
    return a

def get_numbers(line):
    return list(map(int, re.findall("\d+", line)))