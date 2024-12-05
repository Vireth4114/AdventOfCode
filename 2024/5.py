import useful
from collections import defaultdict
import random

rules, updates = useful.get_lines_pure('5').split('\n\n')

rules = [useful.get_numbers(rule) for rule in rules.splitlines()]
updates = [useful.get_numbers(line) for line in updates.splitlines()]

tree = defaultdict(list)
for rule in rules:
    tree[rule[0]].append(rule[1])

falsy = set()
for idx_update, update in enumerate(updates):
    size = len(update)
    for idx in range(size):
        for cmp in range(idx+1, size):
            while True:
                if update[idx] not in tree[update[cmp]]:
                    break
                falsy.add(idx_update)
                rand = random.randrange(idx+1, size) # :3
                update[idx], update[rand] = update[rand], update[idx]

print(sum(res[len(res)//2] for idx, res in enumerate(updates) if idx not in falsy))
print(sum(res[len(res)//2] for idx, res in enumerate(updates) if idx in falsy))