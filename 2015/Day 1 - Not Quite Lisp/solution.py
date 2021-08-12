f = open("input.txt")
inp = f.read()
f.close()


def part_1():
    floor = 0
    for x in range(len(inp)):
        if inp[x] == "(":
            floor += 1
        elif inp[x] == ")":
            floor -= 1
    return floor


def part_2():
    floor = 0
    for x in range(len(inp)):
        if inp[x] == "(":
            floor += 1
        elif inp[x] == ")":
            floor -= 1
        if floor == -1:
            return x + 1
    return floor


print(part_1())
print(part_2())
