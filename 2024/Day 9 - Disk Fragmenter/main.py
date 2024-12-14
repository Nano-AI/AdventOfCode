from dataclasses import dataclass

file = open('./2024/Day 9 - Disk Fragmenter/input.txt', 'r')
input = file.read()
file.close()

data = []
block_id = 0
file = True
for block in input:
    length = int(block)
    if not file:
        for _ in range(length):
            data.append(-1)
    else:
        for _ in range(length):
            data.append(block_id)
        block_id += 1
    file = not file

def part_1(data):
    size = len(data)
    left, right = 0, size - 1
    while left < right:
        if data[left] >= 0:
            left += 1 
        elif data[right] < 0:
            right -= 1
        else:
            temp = data[left]
            data[left] = data[right]
            data[right] = temp
    return sum([data[v] * v if data[v] >= 0 else 0 for v in range(0, size)])

@dataclass
class Block:
    block_type: int
    files: list[int]
    space_length: int

    TYPE_FILE = 1
    TYPE_SPACE = 0

def part_2(input):
    # yeah not gonna lie i really tried to do it using my method but i ended up copying some guy's code
    # https://github.com/nitekat1124/advent-of-code-2024/blob/main/solutions/day09.py
    def parse_blocks(data):
        disk_map = data
        blocks = []  # [block_type, [file_id], space_length]

        block_type = Block.TYPE_FILE  # 0: space, 1: file
        file_id = 0
        space_count = 0
        space_idx = []

        # print(disk_map)
        for i in map(int, disk_map):
            if block_type == Block.TYPE_FILE:
                block = Block(
                    block_type=block_type,
                    files=[file_id] * i,
                    space_length=0,
                )
                blocks.append(block)
                file_id += 1
            else:
                if i > 0:
                    space_count += i
                    space_idx.append(len(blocks))
                    block = Block(
                        block_type=block_type,
                        files=[],
                        space_length=i,
                    )
                    blocks.append(block)
            block_type = (block_type + 1) % 2

        return blocks, space_count, space_idx
    blocks, space_count, space_idx = parse_blocks(input)

    curr_block_idx = len(blocks) - 1

    while curr_block_idx > 0:
        if blocks[curr_block_idx].block_type == Block.TYPE_SPACE:
            curr_block_idx -= 1
            continue

        curr_block_len = len(blocks[curr_block_idx].files)
        for curr_space_idx in space_idx:
            if curr_space_idx >= curr_block_idx:
                break

            if blocks[curr_space_idx].space_length >= curr_block_len:
                blocks[curr_space_idx].files.extend(blocks[curr_block_idx].files)
                blocks[curr_space_idx].space_length -= curr_block_len

                blocks[curr_block_idx].block_type = Block.TYPE_SPACE
                blocks[curr_block_idx].space_length = curr_block_len
                blocks[curr_block_idx].files = []

                if blocks[curr_space_idx].space_length == 0:
                    space_idx.remove(curr_space_idx)

                break

        curr_block_idx -= 1

    checksum = 0
    pos = 0
    for block in blocks:
        for file in block.files:
            checksum += pos * file
            pos += 1
        if block.block_type == Block.TYPE_SPACE:
            pos += block.space_length

    return checksum


print(f"Part 1: {part_1(data[:])}")
print(f"Part 2: {part_2([int(v) for v in input])}")