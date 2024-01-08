# Advent of Code, Day 8
from math import lcm
import os
import re

input_path = os.path.join(os.path.dirname(__file__), "input.txt")

MAPPING_REGEX = re.compile(r'(?P<word>\w{3}) = \((?P<left>\w{3}), (?P<right>\w{3})\)')


def parse_input():
    map_dict = {}
    with open(input_path) as input_obj:
        # first line
        directions = input_obj.readline().strip()
        for line in input_obj.readlines():
            m = MAPPING_REGEX.search(line)
            if m:
                map_dict[m.group('word')] = {'L': m.group('left'),
                                             'R': m.group('right')}

    return directions, map_dict


def find_steps(starting_point, ending, directions, map_dict):
    current = map_dict[starting_point]
    steps = 0
    while True:
        for counter, d in enumerate(directions):
            next_location = current[d]
            steps += 1
            if next_location.endswith(ending):
                break
            current = map_dict[next_location]
        else:
            continue

        # we reached the end
        return steps


def part_1():
    directions, map_dict = parse_input()
    return find_steps('AAA', 'ZZZ', directions, map_dict)


def part_2():
    directions, map_dict = parse_input()
    # find all **A starting points
    starting = list(filter(lambda x: x.endswith('A'), map_dict.keys()))
    min_steps = [find_steps(p, 'Z', directions, map_dict) for p in starting]
    return lcm(*min_steps)
