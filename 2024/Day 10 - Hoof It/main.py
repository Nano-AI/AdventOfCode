from colorama import Fore, Back, Style

f = open("./2024/Day 10 - Hoof It/input.txt")
raw_input = f.read()
f.close()

data = [ [int(c) if c != '.' else -1 for c in line] for line in raw_input.split("\n") ]

def in_range(val, min, max):
    return val >= min and val < max

def print_map(input, x, y):
    global data

    for y in range(len(input)):
        line = input[y]
        printthing = ""
        for x in range(len(line)):
            c1 = input[y][x]
            c0 = data[y][x]
            if c1 < 0:
                printthing += Fore.RED + str(c0) + Style.RESET_ALL
            else:
                printthing += str(c0)
        print(printthing)
    
    print()

def solve_1(input, x, y, trail_path):
    global data
    directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]
    s = 0
    is_nine = False
    if input[y][x] == 9:
        input[y][x] = -1
        is_nine = True
    print_map(input, x, y)
    if is_nine:
        return 1
    for dx, dy in directions:
        x1, y1 = x + dx, y + dy
        if not in_range(x1, 0, len(input[y])) or not in_range(y1, 0, len(input)):
            continue
        if input[y1][x1] == input[y][x] + 1 and input[y1][x1] > 0:
            input[y][x] = -1
            s += solve_1(input, x1, y1, trail_path + [(x, y)])
    if s == 0:
        for px, py in trail_path:
            input[py][px] = data[py][px]
    return s

def part_1(input):
    s = 0
    for y in range(0, len(input)):
        line = input[y]
        for x in range(0, len(line)):
            if line[x] == 0:
                print(f"Starting at {x} {y}")
                s += solve_1(input, x, y, [(x, y)])
    return s

print(f"Part 1: {part_1([ line[:] for line in data ])}")