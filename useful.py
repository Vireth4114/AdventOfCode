def get_lines(filename):
    with open(f'input/{filename}', 'r') as file:
        lines = [i[:-1] for i in file.readlines()]
    return lines

def product(iterable):
    a = 1
    for element in iterable:
        a *= element
    return a