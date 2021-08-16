from itertools import permutations
import re

f = open("input.txt")
inp = f.read().replace('would', '').replace(
    'happiness units by sitting next to', '').replace('.', '').split('\n')
f.close()


def part_1():
    seating = dict()
    people = list()
    for i in inp:
        p1, g, n, p2 = i.split()
        seating[f'{p1}->{p2}'] = -1*int(n) if g == 'lose' else int(n)
        if p1 not in people:
            people.append(p1)
        if p2 not in people:
            people.append(p2)
    best_score = 0
    for seats in permutations(people):
        s = list(seats)
        score = seating[f'{s[0]}->{s[-1]}'] + seating[f'{s[-1]}->{s[0]}']
        for x in range(len(s)-1):
            score += seating[f'{s[x]}->{s[x+1]}'] + \
                seating[f'{s[x+1]}->{s[x]}']
        if score > best_score:
            best_score = score
    return best_score


def part_2():
    seating = dict()
    people = ['Me']
    for i in inp:
        p1, g, n, p2 = i.split()
        seating[f'{p1}->{p2}'] = -1*int(n) if g == 'lose' else int(n)
        if p1 not in people:
            people.append(p1)
        if p2 not in people:
            people.append(p2)
    # Only thing that changed is adding 'Me' to the dict
    for p in people:
        seating[f'{p}->Me'] = 0
        seating[f'Me->{p}'] = 0
    best_score = 0
    for seats in permutations(people):
        s = list(seats)
        score = seating[f'{s[0]}->{s[-1]}'] + seating[f'{s[-1]}->{s[0]}']
        for x in range(len(s)-1):
            score += seating[f'{s[x]}->{s[x+1]}'] + \
                seating[f'{s[x+1]}->{s[x]}']
        if score > best_score:
            best_score = score
    return best_score


print(part_1())
print(part_2())
