import useful

lines = [useful.get_numbers(line) for line in useful.get_lines("2")]

def check(line):
    diffs = [j-i for i, j in zip(line[:-1], line[1:])]
    return all(-3 <= diff <= 3 for diff in diffs) and not min(diffs) < 0 < max(diffs)

def silverstar(): 
    return len([line for line in lines if check(line)])

def goldstar():
    return len([line for line in lines if check(line) or any(check(line[:i] + line[i+1:]) for i in range(len(line)))])
        
if __name__ == "__main__":
    print(silverstar())
    print(goldstar())