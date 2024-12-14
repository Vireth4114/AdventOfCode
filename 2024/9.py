import useful

line = useful.get_list_lines('9')[0]

def silverstar():
    decoded = [idx//2 if idx % 2 == 0 else -1 for idx, c in enumerate(line) for _ in range(int(c))]
    pointer = len(decoded) - 1
    while pointer > 0:
        last = decoded[pointer]
        pointer -= 1
        if last == -1:
            continue
        for idx, c in enumerate(decoded):
            if idx == pointer+1:
                break
            if c == -1:
                decoded[idx] = last
                decoded[pointer+1] = -1
                break

    return sum(int(c)*idx for idx, c in enumerate(decoded) if c != -1)

def goldstar():
    decoded = [idx//2 if idx % 2 == 0 else -1 for idx, c in enumerate(line) for _ in range(int(c))]
    pointer = len(decoded) - 1
    while pointer > 0:
        length = 0
        last = decoded[pointer]
        while decoded[pointer] == last:
            pointer -= 1
            length += 1
        free_length = 0
        if last == -1 or pointer == -1:
            continue
        for idx, c in enumerate(decoded):
            if idx == pointer+1:
                break
            if c == -1:
                free_length += 1
                if free_length == length:
                    for i in range(pointer+1, pointer+length+1):
                        decoded[i] = -1
                    for i in range(length):
                        decoded[idx - i] = last
                    break
            else:
                free_length = 0

    return sum(int(c)*idx for idx, c in enumerate(decoded) if c != -1)

print(silverstar())