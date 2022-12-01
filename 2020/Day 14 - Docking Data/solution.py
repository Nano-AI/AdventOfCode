import re
from itertools import product

indexReg = r"(?<=\[)[^][]*(?=])"
valueReg = r"[^=]+$"

class Combos:
    values = []
    def __init__(self):
        self.values = []
    def combos(self, string, index):
        if index == len(string):
            self.values.append(''.join(string))
            return
        if string[index] == 'X':
            string[index] = '0'
            val1 = self.combos(string, index + 1)
    
            string[index] = '1'
            val2 = self.combos(string, index + 1)

            string[index] = 'X'
        else:
            self.combos(string, index + 1)

def part2():
    memory = dict()
    f = open("input.txt", "r")
    i = f.read()
    mask = list() 
    masklen = len(mask)
    for line in i.split("\n")[:-1]:
        value = re.search(valueReg, line).group()
        if line.startswith("mem"):
            index = re.search(indexReg, line).group()
            binary = list(
                    bin(int(index))[2:].zfill(masklen)
            )
            for x in range(masklen):
                if mask[x] != "0":
                    binary[x] = mask[x]

            values = Combos()
            values.combos(binary, 0)
            for b in values.values:
                memory[int(b, 2)] = value
        else:
            mask = list(value)
            masklen = len(mask)
    
    s = 0
    for address in memory:
        s += int(memory[address])
    print("Part 2:", s)

def part1():
    memory = dict()
    f = open("input.txt", "r")
    i = f.read()
    mask = list() 
    masklen = len(mask)
    for line in i.split("\n")[:-1]:
        value = re.search(valueReg, line).group()
        if line.startswith("mem"):
            index = re.search(indexReg, line).group()
            binary = list(
                    bin(int(value))[2:].zfill(masklen)
            )
            for x in range(masklen):
                if mask[x] != "X":
                    binary[x] = mask[x]
            memory[index] = "".join(binary)
        else:
            mask = list(value)
            masklen = len(mask)
    
    s = 0
    for address in memory:
        s += int(memory[address], 2)
    print("Part 1:", s)

part1()
# part2()

