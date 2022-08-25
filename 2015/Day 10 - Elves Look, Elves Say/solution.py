f = open("input.txt")
inp = f.read()
f.close()


def part_1(repeat=40):
    s = inp

    def calcualte(s):
        out = ''
        last = s[0]
        count = 1
        for char in s[1:]:
            if char != last:
                out += str(count)+last
                last = char
                count = 1
            else:
                count += 1
        out += str(count)+last
        return out
    for i in range(repeat):
        s = calcualte(s)
    return len(s)


def part_2():
    return part_1(50)


print(part_1())
print(part_2())
