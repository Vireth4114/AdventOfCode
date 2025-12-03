import useful

lines = useful.get_lines("3")

def process_lines(lines, n_value):
    res = 0
    for line in lines:
        n = n_value
        start_idx = 0
        str_num = ''
        while n > 0:
            n -= 1
            subline = line[start_idx:(-n or None)]
            next_idx, next_digit = max(enumerate(subline), key=lambda x: x[1])
            start_idx += next_idx + 1
            str_num += next_digit
        res += int(str_num)
    return res
    
print(process_lines(lines, 2))
print(process_lines(lines, 12))

