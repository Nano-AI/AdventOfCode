f = open("input.txt")
inp = f.read()
f.close()

dim_s = inp.split('\n')


def part_1():
    total = 0

    for dim in dim_s:
        l, w, h = dim.split('x')
        l, w, h = int(l), int(w), int(h)
        s1, s2, s3 = l*w, l*h, w*h
        extra = min(s1, s2, s3)
        total += 2*s1 + 2*s2 + 2*s3 + extra

    return total


def part_2():
    total = 0

    for dim in dim_s:
        l, w, h = dim.split('x')
        l, w, h = int(l), int(w), int(h)
        ribbon = min(2*l + 2*w, 2*l + 2*h, 2*w + 2*h)
        bow = l * w * h
        total += ribbon + bow

    return total


print(part_1())
print(part_2())
