import useful
from math import sqrt, ceil, floor

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

def fastersilver(lines=lines_file):
    races = zip(useful.get_numbers(lines[0]), useful.get_numbers(lines[1]))
    mult = 1
    for entry in races:
        min = (entry[0]-sqrt(entry[0]*entry[0]-4*entry[1]))/2
        max = (entry[0]+sqrt(entry[0]*entry[0]-4*entry[1]))/2
        min = min+1 if min.is_integer() else ceil(min)
        max = max-1 if max.is_integer() else floor(max)
        mult *= max-min+1
    return int(mult)


# Very slow because python
def goldstar():
    return silverstar([line.replace(' ', '') for line in lines_file])

def fastergold():
    return fastersilver([line.replace(' ', '') for line in lines_file])

if __name__ == '__main__':
    print(f"Silver star : {silverstar()}")
    print(f"Gold star : {fastergold()}")