import useful
lines = useful.get_lines("7.txt")

def silverstar():
    listhands = [[], [], [], [], [], [], []]
    order = "23456789TJQKA"
    dict_bid = dict()
    for line in lines:
        hand = line.split(' ')[0]
        dict_bid[hand] = int(line.split(' ')[1])
        sortedvalues = sorted([hand.count(card) for card in set(hand)], reverse=True)[:2]

        for idx, value in enumerate(([5], [4, 1], [3, 2], [3, 1], [2, 2], [2, 1], [1, 1])):
            if sortedvalues == value:
                listhands[idx].append(hand)
                break

    truelist = []
    for entry in reversed(listhands):
        truelist += sorted(entry, key=lambda entry: [order.index(card) for card in entry])
    
    return sum((index+1)*dict_bid[entry] for index, entry in enumerate(truelist))

def goldstar():
    listhands = [[], [], [], [], [], [], []]
    order = "J23456789TQKA"
    dict_bid = dict()
    for line in lines:
        hand = line.split(' ')[0]
        dict_bid[hand] = int(line.split(' ')[1])
        sortedvalues = sorted([hand.count(card) for card in set(hand) if card != 'J'], reverse=True)[:2]

        if len(sortedvalues) == 0:
            sortedvalues = [5]
        else:
            sortedvalues[0] += hand.count('J')

        for idx, value in enumerate(([5], [4, 1], [3, 2], [3, 1], [2, 2], [2, 1], [1, 1])):
            if sortedvalues == value:
                listhands[idx].append(hand)
                break

    truelist = []
    for entry in reversed(listhands):
        truelist += sorted(entry, key=lambda entry: [order.index(card) for card in entry])
    
    return sum((index+1)*dict_bid[entry] for index, entry in enumerate(truelist))


if __name__ == '__main__':
    print(f"Silver star: {silverstar()}")
    print(f"Gold star: {goldstar()}")