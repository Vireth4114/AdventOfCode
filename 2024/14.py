import useful

robots = [useful.get_numbers(line) for line in useful.get_lines('14')]

width = 101
height = 103

for _ in range(100):
    for robot in robots:
        robot[0] = (robot[0] + robot[2]) % width
        robot[1] = (robot[1] + robot[3]) % height

print(len([robot for robot in robots if robot[0] < width//2 and robot[1] < height//2])*
      len([robot for robot in robots if robot[0] > width//2 and robot[1] < height//2])*
      len([robot for robot in robots if robot[0] < width//2 and robot[1] > height//2])*
      len([robot for robot in robots if robot[0] > width//2 and robot[1] > height//2]))


robots = [useful.get_numbers(line) for line in useful.get_lines('14')]
best_deviation = 10**9
i = 0
while True:
    for robot in robots:
        robot[0] = (robot[0] + robot[2]) % width
        robot[1] = (robot[1] + robot[3]) % height
    average_x = sum(robot[0] for robot in robots) / len(robots)
    deviation_x = sum(abs(robot[0] - average_x) for robot in robots) / len(robots)
    average_y = sum(robot[1] for robot in robots) / len(robots)
    deviation_y = sum(abs(robot[1] - average_y) for robot in robots) / len(robots)
    deviation = deviation_x * deviation_y
    i += 1
    if deviation < 200:
        print(i)
        break