f = open("input.txt")
inp = f.read()
f.close()


def part_1():
    s = 0
    for i in inp.split('\n'):
        s += len(eval(i))
    return len(inp.replace('\n', '')) - s


def part_2():
    s = 0
    for i in inp.split('\n'):
        s += len(i.replace('\\', '\\\\').replace('"', '\\"')) + 2
    return s - len(inp.replace('\n', ''))


print(part_1())
print(part_2())
