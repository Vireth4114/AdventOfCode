import useful
from itertools import product
from functools import reduce
from operator import add, mul

lines = [useful.get_numbers(line) for line in useful.get_lines('7')]
concat = lambda x, y: int(str(x) + str(y))
print(sum(line[0] for line in lines if any(reduce(lambda x, y: next(ops)(x, y), line[1:]) == line[0] for ops in [iter(ops) for ops in product((add, mul), repeat=len(line) - 2)])))
print(sum(line[0] for line in lines if any(reduce(lambda x, y: next(ops)(x, y), line[1:]) == line[0] for ops in [iter(ops) for ops in product((add, mul, concat), repeat=len(line) - 2)])))