import useful
program = useful.get_numbers(useful.get_lines_pure('17').split('\n\n')[1])

feurs6 = [bin(a)[2:].rjust(4, '0') for a in [0, 8]]
feurs5 = [bin(a)[2:].rjust(4, '0') for a in [0, 1, 2]]
feurs4 = [bin(a)[2:].rjust(4, '0') for a in [5, 12, 15]]
feurs3 = [bin(a)[2:].rjust(4, '0') for a in [2, 10, 14, 15]]
feurs2 = ['1110', '1111']
feur1 = '0111110100'
a = set()
for i in range(2**32):
    for feur5 in feurs5:
        for feur6 in feurs6:
            for feur4 in feurs4:
                for feur3 in feurs3:
                    for feur2 in feurs2:
                        feur = feur6+feur5+feur4+feur3+feur2+feur1
                        A = i * 2**len(feur) + int(feur or '0', 2)
                        iterator = iter(program)
                        j = 0
                        while A != 0:
                            if (A >> (A & 7 ^ 2) ^ A ^ 1) & 7 != next(iterator):
                                break
                            A >>= 3
                            j += 1
                        val = i * 2**len(feur) + int(feur or '0', 2)
                        if j >= 13:
                            print(bin(val)[2:].rjust(40, '0'))
                            print(val)
                            print(j)
                            a.add(i & 15)
                            print(a)

exit()

registers, program = useful.get_lines_pure('17').split('\n\n')
A, B, C = [useful.get_numbers(register)[0] for register in registers.splitlines()]
program = useful.get_numbers(program)
feur = ''
for i in range(2**32):
    pointer = 0
    A = i * 2**len(feur) + int(feur or '0', 2)
    B = 0
    C = 0
    to_print = []
    while pointer < len(program):
        opcode, literal = program[pointer:pointer+2]
        combo = [0, 1, 2, 3, A, B, C, None][literal]
        pointer += 2
        match opcode:
            case 0:
                A //= 2**combo
            case 1:
                B ^= literal
            case 2:
                B = combo % 8
            case 3:
                if A != 0:
                    pointer = literal
            case 4:
                B ^= C
            case 5:
                to_print.append(combo % 8)
            case 6:
                B = A//2**combo
            case 7:
                C = A//2**combo
    if to_print[:4] == program[:4]:
        print(to_print)
        print(program)
        val = i * 2**len(feur) + int(feur or '0', 2)
        print(bin(val)[2:].rjust(40, '0'))
        print(val)