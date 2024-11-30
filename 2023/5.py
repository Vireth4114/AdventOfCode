import useful
import re
# from multiprocessing import Process

lines = useful.get_lines("5.txt")

def get_corr(seeds, seedmap):
    soils = []
    for seed in seeds:
        soil = seed
        for seedentry in seedmap:
            if seed in range(seedentry[1], seedentry[1]+seedentry[2]):
                soil = seed-seedentry[1]+seedentry[0]
                break
        soils.append(soil)
    return soils

def silver(seeds):
    # indexmin = min(seeds)
    seedmap = []
    intermap = []

    for line in lines[3:]:
        if re.search('\d', line) == None:
            if intermap != []:
                seedmap.append(intermap)
            intermap = []
            continue
        else:
            intermap.append(list(map(int, line.split(' '))))

    if intermap != []:
        seedmap.append(intermap)

    for seedinter in seedmap:
        seeds = get_corr(seeds, seedinter)

    # val, idx = min((val, idx) for (idx, val) in enumerate(seeds))
    # print(tuple((indexmin, indexmin+idx, val)))

    return min(seeds)

if __name__ == '__main__':
    seedlist = list(map(int, lines[0].split(' ')[1:]))
    print(f'Silver star : {silver(seedlist)}')

    # Gold Star was obtained through semi-bruteforce
    # I'd scan every 10000 of the ranges, then all 1000 of the best ones, then 100, and so on...
    # Wtf is this day 5
    # 
    # procs = []
    # for seedint in range(0, len(seedlist), 2):
    #     seed = seedlist[seedint]
    #     seeds = list(range(0, seed, seed+seedlist[seedint+1], 10000))
    #     proc = Process(target=silver, args=(seeds,))
    #     proc.start()
    #     procs.append(proc)
    # for index, proc in enumerate(procs):
    #     proc.join()
    