import useful

lines = [[useful.get_numbers(line) for line in splitted.splitlines()] for splitted in useful.get_lines_pure('13').split('\n\n')]

def silverstar():
    res = 0
    for machine in lines:
        (xa, ya), (xb, yb), (xgoal, ygoal) = machine
        if (xa*yb - ya*xb) == 0:
            continue
        a = (xgoal*yb - ygoal*xb)/(xa*yb - ya*xb)
        b = (ygoal*xa - xgoal*ya)/(xa*yb - ya*xb)
        if a.is_integer() and b.is_integer():
            res += int(a*3 + b)
    return res

def goldstar():
    res = 0
    for machine in lines:
        (xa, ya), (xb, yb), (xgoal, ygoal) = machine
        xgoal, ygoal = xgoal+10_000_000_000_000, ygoal+10_000_000_000_000
        if (xa*yb - ya*xb) == 0:
            continue
        a = (xgoal*yb - ygoal*xb)/(xa*yb - ya*xb)
        b = (ygoal*xa - xgoal*ya)/(xa*yb - ya*xb)
        if a.is_integer() and b.is_integer():
            res += int(a*3 + b)
    return res

print(silverstar())
print(goldstar())
