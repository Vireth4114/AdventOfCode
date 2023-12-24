import useful
from time import time

lines = useful.get_lines("22.txt")

blocks = []
for line in lines:
    blocks.append([list(map(int, coord.split(','))) for coord in line.split('~')])

board = []


def silverstar():
    to_remove = [True for _ in range(len(board))]
    for blocks in sustained:
        if len(blocks) == 1:
            to_remove[blocks[0]] = False
    return to_remove.count(True)

def goldstar():
    result = 0
    for i in range(len(board)):
        sus_num = sustained_num.copy()
        currents = [i]
        while currents:
            current = currents.pop(0)
            for next_block in sustaining[current]:
                sus_num[next_block] -= 1
                if sus_num[next_block] == 0:
                    result += 1
                    currents.append(next_block)
    return result

if __name__ == '__main__':
    t1 = time()
    for start, end in blocks:
        trueblock = []
        for x in range(start[0], end[0]+1):
            for y in range(start[1], end[1]+1):
                for z in range(start[2], end[2]+1):
                    trueblock.append([x, y, z])
        board.append(trueblock)

    board.sort(key=lambda tile: min(z[-1] for z in tile))

    for idxblock in range(len(board)):
        block = board[idxblock]
        newblock = block
        to_change = 100000
        ground = True
        if 1 in [tile[-1] for tile in block]:
            continue
        for block_cmp in board[idxblock::-1]:
            if block_cmp == block:
                continue
            if any(tile[:2] in [tile2[:2] for tile2 in block_cmp] for tile in block):
                to_change = min(min([tile[-1] for tile in block]) - max([tile[-1] for tile in block_cmp]) - 1, to_change)
                newblock = [tile[:2] + [tile[2]-to_change] for tile in block]
                ground = False
        if ground:
            newblock = [tile[:2] + [tile[2]-min([tile[-1] for tile in block])+1] for tile in block]
        board.pop(idxblock)
        board.insert(idxblock, newblock)

    sustained = [[] for _ in range(len(board))]
    sustained_num = [1 for _ in range(len(board))]
    sustaining = [[] for _ in range(len(board))]

    for idxblock, block in enumerate(board):
        count = 0
        for idx_cmp, block_cmp in enumerate(board):
            if block == block_cmp:
                continue
            if any(tile[:2] + [tile[2]-1] in block_cmp for tile in block):
                sustained[idxblock].append(idx_cmp)
                count += 1
            if any(tile[:2] + [tile[2]+1] in block_cmp for tile in block):
                sustaining[idxblock].append(idx_cmp)
        if 1 in [tile[-1] for tile in block]:
            sustained_num[idxblock] = 1
        else:
            sustained_num[idxblock] = count
    print(f"Silver star: {silverstar()}")
    print(f"Gold star: {goldstar()}")
    t2 = time()
    print(f'took {round((t2-t1)*1000)} ms')