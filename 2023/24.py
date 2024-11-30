import useful
from sympy import solve
from sympy.abc import x, y, z, u, v, w, i, j, k
from time import time

lines = useful.get_lines("24.txt")

hailstones = []

for line in lines:
    hailstones.append(useful.get_numbers(line))

def silverstar():
    result = 0
    for i in range(len(hailstones)):
        for j in range(i+1, len(hailstones)):
            x1, y1, z1, vx1, vy1, vz1 = hailstones[i]
            x2, y2, z2, vx2, vy2, vz2 = hailstones[j]
            try:
                y = (x1-x2 - (vx1/vy1)*y1+(vx2/vy2)*y2)/((vx2/vy2)-(vx1/vy1))
                t = (y-y1)/vy1
                t2 = (y-y2)/vy2
                x = (vx1*t+x1)
                
                if 200000000000000 <= x <= 400000000000000 and 200000000000000 <= y <= 400000000000000 and t >= 0 and t2 >= 0:
                    result += 1
            except ZeroDivisionError:
                continue
    return result

def goldstar():
    to_solve = []
    time = [i, j, k]
    for idx, (a, b, c, va, vb, vc) in enumerate(hailstones[:3]):
        to_solve += [a + (va - u)*time[idx] - x, b + (vb - v)*time[idx] - y, c + (vc - w)*time[idx] - z]
    sol = solve(to_solve, [u, v, w, x, y, z, i, j, k], dict=True)[0]
    return sum((sol[x], sol[y], sol[z]))

if __name__ == '__main__':
    t1 = time()
    print(f"Silver star: {silverstar()}")
    print(f"Gold star: {goldstar()}")
    t2 = time()
    print(f'took {round((t2-t1)*1000)} ms')