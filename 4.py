import useful

lines = useful.get_lines("4.txt")

def silverstar():
    sum = 0
    for line in lines:
        line = line.split(': ')[1]
        winning = line.split(' | ')[0].replace('  ', ' ').split(' ')
        yours = line.split(' | ')[1].replace('  ', ' ').split(' ')

        matches = 0

        for num in yours:
            if num in winning:
                if matches == 0:
                    matches = 1
                else:
                    matches *= 2
        sum += matches

    return sum

def goldstar():
    numlines = [1]*len(lines)
    for index, line in enumerate(lines):
        newline = line.split(': ')[1]
        winning = newline.split(' | ')[0].replace('  ', ' ').split(' ')
        yours = newline.split(' | ')[1].replace('  ', ' ').split(' ')

        matches = 0
        for num in yours:
            if num in winning:
                matches += 1
            
        for card in range(index+1, index+matches+1):
            numlines[card] += numlines[index]

    return sum(numlines)

if __name__ == '__main__':
    print(f"Silver star : {silverstar()}")
    print(f"Gold star : {goldstar()}")