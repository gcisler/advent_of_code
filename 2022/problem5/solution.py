import re

def parse_input():
    move_regex = re.compile("move (\d+) from (\d) to (\d)")
    crates_strings = []
    moves = []
    with open("input.txt") as input_obj:
        for line in input_obj.readlines():
            m = move_regex.match(line)
            if m:
                moves.append(list(map(int, m.groups())))
            elif line.startswith("["):
                crates_strings.append(line.rstrip())

    # parse crates
    stacks = 9
    crates = [[] for _ in range(stacks+1)]
    crates_strings.reverse()
    for height in crates_strings:
        for stack in range(stacks):
            entry = height[1+4*stack].strip()
            if entry:
                crates[stack+1].append(entry)

    return crates, moves

def part1():
    crates, moves = parse_input()

    for count, src, dst in moves:
        for c in range(count):
            assert crates[src]
            crates[dst].append(crates[src].pop())

    # return the end of each list
    return ''.join([stack[-1] for stack in crates[1:]])


def part2():
    crates, moves = parse_input()

    for count, src, dst in moves:
        assert len(crates[src]) >= count
        moving_stack = crates[src][-count:]
        crates[src] = crates[src][:-count]
        crates[dst].extend(moving_stack)

    # return the end of each list
    return ''.join([stack[-1] for stack in crates[1:]])

print(part1())
print(part2())
# VWLCWGSDQ
# TCGLQSLPW