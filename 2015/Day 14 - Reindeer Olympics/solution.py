import re

f = open("input.txt")
inp = f.read().split('\n')
f.close()


def part_1():
    deers = dict()
    for line in inp:
        deers[re.findall(r'^([\w\-]+)', line)[0]] = re.findall(r'\d+', inp)
    print(deers)


def part_2():
    pass


print(part_1())
print(part_2())
