"""
This is a brute force answer and is very slow.
This one is way faster and shorter and uses regex:
https://www.reddit.com/r/adventofcode/comments/3wbzyv/day_11_solutions/cxv7xvm?utm_source=share&utm_medium=web2x&context=3
"""

f = open("input.txt")
inp = f.read()
f.close()


def valid_password(password: str):
    if 'i' in password or 'o' in password or 'l' in password:
        return False
    prev = ord(password[0])
    nums = []
    three = False
    copy_count = 0
    for x in range(len(password)):
        if x < len(password) - 2 and ord(password[x+1])-ord(password[x]) == 1 and ord(password[x+2])-ord(password[x+1]) == 1:
            three = True
        if x < len(password) - 1 and password[x] == password[x+1]:
            copy_count += 1
    if not three or copy_count < 2:
        return False
    return True


def generate(s):
    if ord(s[-1]) - 96 == 26:
        return generate(s[:-1])+'a'
    return s[:-1]+chr(ord(s[-1])+1)


def part_1():
    password = inp
    found = False
    while not found:
        password = generate(password)
        if valid_password(password):
            return password


print(part_1())
