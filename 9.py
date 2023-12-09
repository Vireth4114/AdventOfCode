import useful

lines = useful.get_lines("9.txt")

def silverstar():
    sumvalue = 0
    for line in lines:
        numbers = useful.get_numbers(line)
        sumvalue += numbers[-1]
        while set(numbers) != {0}:
            numbers = [numbers[i+1]-numbers[i] for i in range(len(numbers)-1)]
            sumvalue += numbers[-1]
    return sumvalue

def goldstar():
    sumvalue = 0
    for line in lines:
        numbers = useful.get_numbers(line)
        str_numbers = str(numbers[0])
        while set(numbers) != {0}:
            numbers = [numbers[i+1]-numbers[i] for i in range(len(numbers)-1)]
            str_numbers += f"-({numbers[0]}"
        str_numbers += ')'*str_numbers.count('(')
        sumvalue += eval(str_numbers)
    return sumvalue

if __name__ == '__main__':
    print(f"Silver star: {silverstar()}")
    print(f"Gold star: {goldstar()}")