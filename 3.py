import useful

lines = useful.get_lines_with_newline("3.txt")

def silverstar():
    allnums = []

    for indexline, line in enumerate(lines):
        check = False
        numstr = ''
        for indexchar, char in enumerate(line):
            # Continue à lire le nombre
            if char.isdigit():
                numstr += char
                for l in range(max(indexline-1, 0), min(indexline+2, len(lines))):
                    for c in range(max(indexchar-1, 0), min(indexchar+2, len(line))):
                        if not (lines[l][c].isdigit() or lines[l][c] == '.'):
                            check = True
            
            # Traite le nombre après sa fin
            else:
                if check:
                    allnums.append(int(numstr))
                check = False
                numstr = ''

    return sum(allnums)

def goldstar():
    dict_star = dict()

    for indexline, line in enumerate(lines):
        stars = []
        check = False
        numstr = ''
        for indexchar, char in enumerate(line):
            # Continue à lire le nombre
            if char.isdigit():
                numstr += char
                for l in range(max(indexline-1, 0), min(indexline+2, len(lines))):
                    for c in range(max(indexchar-1, 0), min(indexchar+2, len(line))):
                        if (lines[l][c] == '*'):
                            if [l, c] not in stars:
                                stars.append([l, c])
                            check = True
            
            # Traite toutes les étoiles voisines trouvées
            else:
                if check and len(stars) != 0:
                    for star in stars:
                        if tuple(star) not in dict_star.keys():
                            dict_star[tuple(star)] = []
                        dict_star[tuple(star)].append(int(numstr))
                check = False
                numstr = ''
                stars = []

    return sum([useful.product(star) for star in dict_star.values() if len(star) == 2])

if __name__ == '__main__':
    print(f"Silver star : {silverstar()}")
    print(f"Gold star : {goldstar()}")