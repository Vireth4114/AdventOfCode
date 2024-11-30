import useful
from functools import cache

lines = useful.get_lines("12.txt")

@cache
def getcomb(seq, nums):
    if seq == "":
        return 1 if nums == () else 0
    if nums == ():
        return 1 if '#' not in seq else 0
    result = 0
    if seq[0] == '.' or seq[0] == '?':
        result += getcomb(seq[1:], nums)
    if seq[0] == '?' or seq[0] == '#':
        if nums[0] <= len(seq) and '.' not in seq[:nums[0]] and (nums[0] == len(seq) or seq[nums[0]] != '#'):
            result += getcomb(seq[nums[0]+1:], nums[1:])
    return result

def silverstar():
    sum1 = 0
    for i in range(len(lines)):
        seq = lines[i].split(' ')[0]
        nums = useful.get_numbers(lines[i])
        sum1 += getcomb(seq, tuple(nums))
    return sum1

def goldstar():
    sum1 = 0
    for i in range(len(lines)):
        seq = '?'.join([lines[i].split(' ')[0]]*5)
        nums = useful.get_numbers(lines[i])*5
        sum1 += getcomb(seq, tuple(nums))
    return sum1

if __name__ == '__main__':
    print(f"Silver star: {silverstar()}")
    print(f"Gold star: {goldstar()}")