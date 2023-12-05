# Advent of Code, Day 1
import os
import re

input_path = os.path.join(os.path.dirname(__file__), "input.txt")
nums = list(map(str, range(10)))
num_dict = {
    '0': 0,
    'zero': 0,
    '1': 1,
    'one': 1,
    '2': 2,
    'two': 2,
    'three': 3,
    '3': 3,
    "four": 4,
    '4': 4,
    'five': 5,
    '5': 5,
    "six": 6,
    '6': 6,
    "seven": 7,
    '7': 7,
    "eight": 8,
    '8': 8,
    "nine": 9,
    '9': 9
}
def parse_input():
    with open(input_path) as input_obj:
        return input_obj.readlines()

def is_num(variable):
    return variable in nums


def index_nums(line):
    line = str(line)
    all_indices = {}
    for n in num_dict:
        for r in re.finditer(n, line):
            all_indices[r.start()] = num_dict[n]
    val = all_indices[min(all_indices)] * 10 + all_indices[max(all_indices)]
    return val

def part_1():

    total = 0
    for line in parse_input():
        line_mod = list(filter(is_num, line))
        if line_mod:
            total += 10 * int(line_mod[0]) + int(line_mod[-1])

    return total

def part_2():

    total = 0
    for line in parse_input():
        total += index_nums(line)

    return total