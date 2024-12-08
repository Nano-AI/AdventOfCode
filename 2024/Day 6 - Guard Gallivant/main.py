import math

f = open("input.txt")
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
    steps = 0
    while in_range(x0, 0, width) and in_range(y0, 0, height):
        if steps > width * height:
            return -1
        dx, dy = get_dir(angle0)
        x1, y1 = x0 + dx, y0 + dy
        if in_range(x1, 0, width) and in_range(y1, 0, height):
            if m0[y1][x1] == '#':
                angle0 -= 90
                continue
            if m0[y0][x0] == '.':
                walked += 1
                m0[y0][x0] = 'X'
        steps += 1
        x0, y0 = x1, y1
    walked += 2
    return walked

def part_2(m0, x, y, angle0):
    # this is actually some of the worst code i've ever written
    x0, y0 = x, y
    xi, yi = x0, y0
    blocks = 0
    dx, dy = get_dir(angle0)
    for j in range(0, height):
        for i in range(0, width):
            if m0[j][i] == '#' or (j == yi and i == xi):
                continue
            m0[j][i] = '#'
            if part_1(m0, x, y, angle0) < 0:
                blocks += 1 
            m0[j][i] = '.'
    
    return blocks

print("Part 1: " + str(part_1([row[:] for row in m], x, y, angle)))
print("Part 2: " + str(part_2([row[:] for row in m], x, y, angle)))
