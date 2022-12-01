f = open("input.txt")
data = f.read()

def part_1():
    s = 0
    m = 0
    for line in data.split("\n"):
        if line == "":
            if s > m:
                m = s
            s = 0 
        else:
            s += int(line)
    return m

def part_2():
    sums = []
    s = 0
    for line in data.split("\n"):
        if line == "":
            sums.append(s) 
            s = 0 
        else:
            s += int(line)
    return sum(sorted(sums)[-3:])

print("Part 1:", part_1())
print("Part 2:", part_2())