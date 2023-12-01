import useful
lines = useful.get_lines("1.txt")

def silverstar():
    nums = []

    for line in lines:
        chars = [int(c) for c in line if ord(c) <= ord('9')]
        nums.append(chars[0]*10 + chars[-1])
    
    # 54708 for this input
    print(sum(nums))


def goldstar():
    nums = []
    digits = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

    for line in lines:
        # Find the first letter digit
        first_real_idx = 1000
        for index, digit in enumerate(digits):
            idx = line.find(digit)
            if idx < first_real_idx and idx != -1:
                first_real = index+1
                first_real_idx = idx
        
        # Find the last letter digit if there are letter digits in the line
        if first_real_idx != 1000:
            last_real_idx = first_real_idx
            last_real = first_real
            for index, digit in enumerate(digits):
                idx = line.rfind(digit)
                if idx > last_real_idx and idx != -1:
                    last_real = index+1
                    last_real_idx = idx
        else:
            last_real_idx = -1


        # Check if there are more extremes digits than the one arleady found
        for idx, c in enumerate(line):
            if ord(c) <= ord('9'):
                if idx < first_real_idx:
                    first_real = int(c)
                    first_real_idx = idx
                if idx > last_real_idx:
                    last_real = int(c)
                    last_real_idx = idx
        
        # Safe check if first and last are the same
        if first_real_idx == last_real_idx:
            last_real = first_real

        nums.append(first_real*10 + last_real)

    # 54087 for this input
    print(sum(nums))

if __name__ == '__main__':
    silverstar()