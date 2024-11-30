import useful
from math import lcm
from time import time

lines = useful.get_lines('20.txt')

if __name__ == '__main__':
    t1 = time()
    desc_value = dict()

    for line in lines:
        value, dest = line.split(' -> ')
        if value[0] == '%':
            desc_value[value[1:]] = ['%', "off", dest.split(', ')]
        elif value[0] == '&':
            desc_value[value[1:]] = ['&', [], dest.split(', ')]
        else:
            broadcasting = dest.split(', ')

    for con in [key for key, value in desc_value.items() if value[0] == '&']:
        desc_value[con][1] = {key: 'low' for key, value in desc_value.items() if con in value[-1]}

    lower_sig = {key: 0 for key in desc_value['ql'][1].keys()}

    count_high = 0
    count_low = 0
    for i in range(1, 5000):
        count_low += 1
        to_handle = [['broadcaster', target, "low"] for target in broadcasting]
        while to_handle:
            origin, target, signal = to_handle.pop(0)

            if signal == "low":
                count_low += 1
            else:
                count_high += 1
            
            if target == 'rx':
                continue

            if target == 'ql' and signal == 'high':
                if lower_sig[origin] == 0:
                    lower_sig[origin] = i

            type, state, dest = desc_value[target]

            if type == '%':
                if signal == "low":
                    desc_value[target][1] = 'on' if state == 'off' else 'off'
                    next_sig = 'high' if desc_value[target][1] == 'on' else 'low'
                    for value in dest:
                        to_handle.append([target, value, next_sig])
            else:
                desc_value[target][1][origin] = signal
                next_sig = 'low' if all(x == 'high' for x in desc_value[target][1].values()) else 'high'
                for value in dest:
                    to_handle.append([target, value, next_sig])
        if i == 1000:
            print(f"Silver star: {count_high*count_low}")

    print(f"Gold star: {lcm(*[int(value) for value in lower_sig.values()])}")
    t2 = time()
    print(f'took {round((t2-t1)*1000)} ms')