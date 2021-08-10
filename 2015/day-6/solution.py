import re

f = open("input.txt")
inp = f.read()
f.close()
instructions = re.findall(
    r'(toggle|turn on|turn off)\s(\d*),(\d*)\sthrough\s(\d*),(\d*)', inp)

actions = {
    'toggle': lambda x: x + 1 if x == 0 else x - 1,
    'turn on': lambda x: x + 1 if x == 0 else x,
    'turn off': lambda x: x - 1 if x > 0 else x
}


def part_1():
    lights = [[0 for i in range(1000)] for j in range(1000)]
    for action, fx, fy, tx, ty in instructions:
        for x in range(int(fx), int(tx) + 1):
            for y in range(int(fy), int(ty) + 1):
                lights[x][y] = actions[action](lights[x][y])
    return sum([v for s in lights for v in s])


print(part_1())
