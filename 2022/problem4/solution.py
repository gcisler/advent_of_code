import re

LINE_REGEX = re.compile("^(\d+)-(\d+),(\d+)-(\d+)")


def parse_input():
    with open("input.txt") as input_obj:
        all_data = input_obj.readlines()

    return [_.rstrip() for _ in all_data]


def subrange(line):
    ranges = list(map(int, LINE_REGEX.match(line).groups()))
    left = ranges[:2]
    right = ranges[2:]

    return (left[0] <= right[0] and left[1] >= right[1]) or \
        (right[0] <= left[0] and right[1] >= left[1])


def part1():

    return sum([subrange(line) for line in parse_input()])


def overlap(line):
    ranges = list(map(int, LINE_REGEX.match(line).groups()))
    left = ranges[:2]
    right = ranges[2:]

    return (left[0] == right[0] or left[1] == right[1]) or \
        (left[0] < right[0] and left[1] >= right[0]) or \
        (right[0] < left[0] and right[1] >= left[0])


def part2():
    return sum([overlap(line) for line in parse_input()])




print(part1())
print(part2())
