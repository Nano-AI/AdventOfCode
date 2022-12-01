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

    print(m)

def part_2():
    sums = []
    s = 0
    for line in data.split("\n"):
        if line == "":
            sums.append(s) 
            s = 0 
        else:
            s += int(line)
    print(sum(sorted(sums)[-3:]))

part_1()
part_2()