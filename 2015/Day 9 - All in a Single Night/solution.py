import sys
from itertools import permutations

f = open("input.txt")
inp = f.read().split('\n')
f.close()

m = dict()
places = list()


def setup_places():
    for p in inp:
        (p1, _, p2, _, d) = p.split()
        m[f'{p1} -> {p2}'] = d
        m[f'{p2} -> {p1}'] = d
        if p1 not in places:
            places.append(p1)
        if p2 not in places:
            places.append(p2)


def part_1():
    shortest = sys.maxsize
    for path in permutations(places):
        distance = 0
        for i in range(len(path) - 1):
            distance += int(m[f'{path[i]} -> {path[i+1]}'])
        if distance < shortest:
            shortest = distance
    return shortest


def part_2():
    longest = 0
    for path in permutations(places):
        distance = 0
        for i in range(len(path) - 1):
            distance += int(m[f'{path[i]} -> {path[i+1]}'])
        if distance > longest:
            longest = distance
    return longest


setup_places()
print(part_1())
print(part_2())
