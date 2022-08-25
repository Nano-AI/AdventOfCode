import re

f = open('input.txt')
inp = f.read()
f.close()
strings = inp.split('\n')


def is_nice_1(s: str) -> bool:
    return re.search(r'([aeiou].*){3,}', s) and re.search(r'(.)\1', s) and not re.search(r'ab|cd|pq|xy', s)


def is_nice_2(s: str) -> bool:
    return re.search(r'(..).*\1', s) and re.search(r'(.).\1', s)


def part_1(func=is_nice_1):
    nice_strings = 0
    for word in strings:
        if func(word):
            nice_strings += 1
    return nice_strings


def part_2():
    return part_1(is_nice_2)


print(part_1())
print(part_2())
