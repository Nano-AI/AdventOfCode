from math import floor

f = open('input.txt')
inp = f.read()
f.close()

index_data = {
    '^': (0, 1),
    'v': (0, -1),
    '>': (1, 0),
    '<': (-1, 0),
}


def part_1():
    houses = 0
    x, y = 0, 0
    visited = []
    for direction in inp:
        if (x, y) not in visited:
            houses += 1
            visited.append((x, y))
        dx, dy = index_data[direction]
        x += dx
        y += dy
    return houses


def part_2():
    houses = 0
    visited = []
    sx, sy = 0, 0
    rx, ry = 0, 0
    for i, direction in enumerate(inp):
        dx, dy = index_data[direction]
        if i % 2 == 0:
            sx += dx
            sy += dy
            if (sx, sy) not in visited:
                houses += 1
                visited.append((sx, sy))
        elif i % 2 != 0:
            rx += dx
            ry += dy
            if (rx, ry) not in visited:
                houses += 1
                visited.append((rx, ry))
    return houses


print(part_1())
print(part_2())
