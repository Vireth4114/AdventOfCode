import useful

points = [useful.get_numbers(line) for line in useful.get_lines("9")]

max_area = 0

def line_in_rect(line_p1, line_p2, rect_p1, rect_p2):
    minx, maxx = sorted((rect_p1[0], rect_p2[0]))
    miny, maxy = sorted((rect_p1[1], rect_p2[1]))
    minlinex, maxlinex = sorted((line_p1[0], line_p2[0]))
    minliney, maxliney = sorted((line_p1[1], line_p2[1]))

    if minlinex == maxlinex:
        return minx < minlinex < maxx and maxliney > miny and minliney < maxy
    
    return miny < minliney < maxy and maxlinex > minx and minlinex < maxx

def rect_in_polygon(point, point2):
    middle_point = ((point[0] + point2[0]) / 2, (point[1] + point2[1]) / 2)
    num_crossings = 0
    for idx4, point4 in enumerate(points):
        next_point = points[(idx4 + 1) % len(points)]
        if point4[0] > middle_point[0] and min(point4[1], next_point[1]) < middle_point[1] < max(point4[1], next_point[1]):
            num_crossings += 1
    return num_crossings % 2 == 1

for idx, point in enumerate(points):
    print(idx)
    for idx2, point2 in enumerate(points):
        if idx2 <= idx:
            continue
        if abs(point[0] - point2[0]) < 2 or abs(point[1] - point2[1]) < 2:
            continue
        area = (abs(point[0] - point2[0]) + 1) * (abs(point[1] - point2[1]) + 1)
        if area <= max_area:
            continue
        for idx3, point3 in enumerate(points):
            next_point = points[(idx3 + 1) % len(points)]
            if line_in_rect(point3, next_point, point, point2):
                break
        else:
            if rect_in_polygon(point, point2) and area > max_area:
                max_area = area

print(max_area)

