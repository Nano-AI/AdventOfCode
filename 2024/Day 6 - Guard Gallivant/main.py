import math

f = open("./2024/Day 6 - Guard Gallivant/input.txt")
i = f.read()
f.close()

m = [ [ c for c in line ] for line in i.split("\n") ]

height = len(m)
width = len(m[0])

angle = 0

found = False

def get_dir(angle):
    angle = angle % 360
    if angle == 0:
        return (1, 0)
    if angle == 90:
        return (0, -1)
    if angle == 180:
        return (-1, 0)
    if angle == 270:
        return (0, 1)


def in_range(val, min, max):
    return val >= min and val < max

for j in range(0, height):
    if found:
        break
    for i in range(0, width):
        c = m[j][i]
        if c in ['>', '<', '^']:
            y = j
            x = i
            if c == '>':
                angle = 0
            if c == '^':
                angle = 90
            if c == '<':
                angle = 180
            m[j][i] = 'X'
            found = True
            break

def part_1(m0, x0, y0, angle0):
    walked = 0
    while in_range(x0, 0, width) and in_range(y0, 0, height):
        dx, dy = get_dir(angle0)
        x1, y1 = x0 + dx, y0 + dy
        if in_range(x1, 0, width) and in_range(y1, 0, height):
            if m[y1][x1] == '#':
                angle0 -= 90
                continue
            if m[y0][x0] == '.':
                walked += 1
                m[y0][x0] = 'X'
        x0, y0 = x1, y1
    walked += 1
    return walked

def part_2(m0, x0, y0, angle0):
    directions = [(0, 0) * width] * height
    xi, yi = x0, y0
    blocks = 0
    dx, dy = get_dir(angle0)
    for i in range(0, height):
        for j in range(0, width):
            if m[j][i] == '#' or (i == yi and j == xi):
                continue

            m0[j][i] = '#'

            while in_range(x0, 0, width) and in_range(y0, 0, height):
                dx, dy = get_dir(angle0)
                if m[y][x] == 'X' and (dx, dy) == directions[y][x]:
                    blocks += 1
                    break
                x1, y1 = x0 + dx, y0 + dy
                if in_range(x1, 0, width) and in_range(y1, 0, height):
                    if m[y1][x1] == '#':
                        angle0 -= 90
                        continue
                    if m[y0][x0] == '.':
                        m[y0][x0] = 'X'
                        directions[y0][x0] = (dx, dy)

                x0, y0 = x1, y1

                print("\n".join([ "".join(a) for a in m ]))

            m[j][i] = '.'
    
    return blocks

print("Part 1: " + str(part_1(m, x, y, angle)))
print("Part 2: " + str(part_2(m, x, y, angle)))
