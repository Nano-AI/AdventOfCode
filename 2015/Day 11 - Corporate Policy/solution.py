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
    x = 0
    while x < len(password)-1:
        if password[x] == password[x+1]:
            copy_count += 1
            x += 1
        x += 1
    for x in range(len(password)-2):
        if ord(password[x+1])-ord(password[x]) == 1 and ord(password[x+2])-ord(password[x+1]) == 1:
            three = True
            break
    if not three or copy_count < 2:
        return False
    return True


def generate(s):
    if ord(s[-1]) - 96 == 26:
        return generate(s[:-1])+'a'
    return s[:-1]+chr(ord(s[-1])+1)


def part_1(skip=[]):
    found = False
    password = inp
    while not found:
        password = generate(password)
        if valid_password(password) and password not in skip:
            return password


def part_2():
    p1 = part_1()
    return part_1(p1)


print(part_1())
print(part_2())
