import math

f = open("2024/Day 5 - Print Queue/input.txt")
i = f.read()
f.close()

lines = i.split("\n")

instructions = {}
tests = []
swapped = False

for line in lines:
    if line == "":
        swapped = True
        continue
    if not swapped:
        i1, i2 = line.split("|")
        # i1 must go before i2
        # therefor it's wrong if i2 went before i1
        if i2 not in instructions:
            instructions[i2] = [i1]
        else:
            instructions[i2].append(i1)
    else:
        tests.append(line.split(","))

def is_valid(sequence):
    size = len(sequence)
    for i in range(0, size):
        at = sequence[i]
        if at not in instructions:
            continue
        for j in range(i + 1, size):
            next = sequence[j]
            if next in instructions[at]:
                return (False, i, j)
    return (True, -1, -1)

def part_1():
    count = 0
    for test in tests:
        valid, _, _ = is_valid(test)
        if valid:
            count += int(test[math.floor(len(test) / 2)])
    return count

def part_2():
    count = 0
    for test in tests:
        size = len(test)
        t = test
        valid, _, _ = is_valid(t)
        if valid:
            continue 
        while not valid:
            valid, i, j = is_valid(t)
            temp = t[i]
            t[i] = t[j]
            t[j] = temp
        count += int(t[math.floor(len(t) / 2)])

    return count

print("Part 1: " + str(part_1()))
print("Part 2: " + str(part_2()))