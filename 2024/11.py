import useful
from functools import cache

numbers = useful.get_numbers(useful.get_lines('11')[0])

@cache
def backtrack(number, depth=0):
    if depth == 75:
        return 1
    if number == 0:
        return backtrack(1, depth+1)
    string = str(number)
    if len(string) % 2 == 0:
        return backtrack(int(string[:len(string)//2]), depth+1) + \
               backtrack(int(string[len(string)//2:]), depth+1)
    else:
        return backtrack(number*2024, depth+1)

print(sum(backtrack(num) for num in numbers))