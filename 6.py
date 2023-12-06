import useful

lines_file = useful.get_lines("6.txt")

def silverstar(lines=lines_file):
    dict_distance = dict(zip(useful.get_numbers(lines[0]), useful.get_numbers(lines[1])))
    mult = 1
    for duration in dict_distance:
        min = 0
        max = 0
        for held in range(duration+1):
            if (duration-held)*held > dict_distance[duration]:
                if min == 0:
                    min = held
            elif min != 0:
                max = held
                break
        mult *= max-min
    return mult

# Very slow because python
def goldstar():
    return silverstar([line.replace(' ', '') for line in lines_file])


if __name__ == '__main__':
    print(f"Silver star : {silverstar()}")
    print(f"Gold star : {goldstar()}")