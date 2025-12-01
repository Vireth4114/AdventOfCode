import useful
from itertools import product
from collections import defaultdict

secrets = useful.get_numbers(useful.get_lines_pure('22'))

def get_next(secret):
    secret = (secret ^ secret<<6) & ((1 << 24) - 1)
    secret = (secret ^ secret>>5) & ((1 << 24) - 1)
    secret = (secret ^ secret<<11) & ((1 << 24) - 1)
    return secret

res = 0
datas = defaultdict(int)
for idx, secret in enumerate(secrets):
    seen = set()
    prevs = (None, None, None, None)
    true_prevs = (None, None, None, secret % 10)
    for i in range(2000):
        secret = get_next(secret)
        prevs = prevs[1:] + (secret % 10 - true_prevs[-1],)
        true_prevs = true_prevs[1:] + (secret % 10,)
        if i >= 3 and prevs not in seen:
            datas[prevs] += secret % 10
            seen.add(prevs)
    res += secret

print(res)
print(max(datas.items(), key=lambda x: x[1])[1])

