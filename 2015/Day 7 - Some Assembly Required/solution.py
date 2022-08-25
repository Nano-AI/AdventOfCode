f = open("input.txt")
inp = f.read().split('\n')
f.close()

calc = dict()
results = dict()


def reset_results():
    global calc
    global results
    calc = dict()
    results = dict()
    for c in inp:
        op, res = c.split('->')
        calc[res.strip()] = op.strip().split(' ')


def calculate(name):
    try:
        return int(name)
    except ValueError:
        pass
    if name not in results:
        o = calc[name]
        if len(o) == 1:
            res = calculate(o[0])
        else:
            op = o[-2]
            if op == 'AND':
                res = calculate(o[0]) & calculate(o[2])
            elif op == 'OR':
                res = calculate(o[0]) | calculate(o[2])
            elif op == 'NOT':
                res = ~calculate(o[1]) & 0xffff
            elif op == 'RSHIFT':
                res = calculate(o[0]) >> calculate(o[2])
            elif op == 'LSHIFT':
                res = calculate(o[0]) << calculate(o[2])
        results[name] = res
    return results[name]


def part_1():
    reset_results()
    return calculate('a')


def part_2():
    reset_results()
    a_value = part_1()
    reset_results()
    results['b'] = a_value
    return calculate('a')


print(part_1())
print(part_2())
