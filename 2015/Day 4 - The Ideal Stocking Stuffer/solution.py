import hashlib

f = open('input.txt')
inp = f.read()
f.close()


def part_1(zeroes=5) -> int:
    x = 0
    while True:
        e = hashlib.md5((inp + str(x)).encode('utf-8')).hexdigest()
        if e[0:zeroes] == '0' * zeroes:
            print(e)
            return x
        x += 1


def part_2():
    return part_1(6)


print(part_1())
print(part_2())
