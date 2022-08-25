import re
import json

f = open("input.txt")
inp = f.read()
f.close()

obj = json.loads(inp)


def part_1():
    # lazy one liner using regex
    return sum([int(d) for d in re.findall(r'-?\d+', inp)])


def part_1_recursive(o=obj):
    # recursive method
    if type(o) is int:
        return o
    if type(o) is list:
        return sum(map(part_1_recursive, o))
    if type(o) is dict:
        return sum(map(part_1_recursive, o.values()))
    return 0


def part_2(o=obj):
    if type(o) is int:
        return o
    if type(o) is list:
        return sum(map(part_2, o))
    if type(o) is dict:
        v = o.values()
        if 'red' in v:
            return 0
        return sum(map(part_2, v))
    return 0


print(part_1())
print(part_1_recursive())
print(part_2())
