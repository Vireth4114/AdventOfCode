import useful
lines = useful.get_lines("7.txt")

def silverstar():
    listhands = [[], [], [], [], [], [], []]
    dict_bid = dict()
    for line in lines:
        hand = line.split(' ')[0].replace('A', 'E').replace('K', 'D').replace('Q', 'C').replace('J', 'B').replace('T', 'A')
        dict_bid[hand] = int(line.split(' ')[1])
        countcard = []

        for c in (set(hand)):
            countcard.append(hand.count(c))
        sortedvalues = sorted(countcard, reverse=True)[:2]

        for idx, value in enumerate(([5], [4, 1], [3, 2], [3, 1], [2, 2], [2, 1], [1, 1])):
            if sortedvalues == value:
                listhands[idx].append(hand)
                break

    truelist = []
    for entry in reversed(listhands):
        truelist += sorted(entry)
    
    return sum((index+1)*dict_bid[entry] for index, entry in enumerate(truelist))

def goldstar():
    listhands = [[], [], [], [], [], [], []]
    dict_bid = dict()
    for line in lines:
        hand = line.split(' ')[0].replace('A', 'D').replace('K', 'C').replace('Q', 'B').replace('T', 'A').replace('J', '1')
        dict_bid[hand] = int(line.split(' ')[1])
        countcard = []

        for c in (set(hand)):
            if c != '1':
                countcard.append(hand.count(c))
        sortedvalues = sorted(countcard, reverse=True)[:2]

        if len(sortedvalues) == 0:
            sortedvalues = [5]
        else:
            sortedvalues[0] += hand.count('1')

        for idx, value in enumerate(([5], [4, 1], [3, 2], [3, 1], [2, 2], [2, 1], [1, 1])):
            if sortedvalues == value:
                listhands[idx].append(hand)
                break

    truelist = []
    for entry in reversed(listhands):
        truelist += sorted(entry)
    
    return sum((index+1)*dict_bid[entry] for index, entry in enumerate(truelist))


if __name__ == '__main__':
    print(f"Silver star: {silverstar()}")
    print(f"Gold star: {goldstar()}")