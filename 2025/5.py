import useful

ranges, nums = useful.get_lines_pure("5").split('\n\n')

ranges = [list(map(int, line.split('-'))) for line in ranges.split('\n')]
nums = list(map(int, nums.split('\n')))

def in_range(n, r):
    return r[0] <= n <= r[1]

print(sum(1 for n in nums if any(in_range(n, r) for r in ranges)))

gold = 0

for idx, r in enumerate(ranges):
    nums_to_add = r[1] - r[0] + 1
    for idx2, r2 in enumerate(ranges[:idx]):
        if in_range(r[0], r2) and in_range(r[1], r2):
            nums_to_add = 0
            ranges[idx] = [-1, -1]
            break
        elif in_range(r[0], r2):
            nums_to_add -= r2[1] - r[0] + 1
            ranges[idx][0] = r2[1] + 1
        elif in_range(r[1], r2):
            nums_to_add -= r[1] - r2[0] + 1
            ranges[idx][1] = r2[0] - 1
        elif r2[0] > r[0] and r2[1] < r[1]:
            nums_to_add -= r2[1] - r2[0] + 1
    gold += nums_to_add

print(gold)