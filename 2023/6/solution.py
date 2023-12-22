# Advent of Code, Day 6
import os
import re

input_path = os.path.join(os.path.dirname(__file__), "input.txt")

NUM_REGEX = re.compile(r' (\d+)')
def parse_input():
    with open(input_path) as input_obj:
        time_line = input_obj.readline()
        times = NUM_REGEX.findall(time_line)
        dist_line = input_obj.readline()
        dists = NUM_REGEX.findall(dist_line)
        td_tuple = zip(map(int, times), map(int, dists))
        return td_tuple

def parse_input2():
    with open(input_path) as input_obj:
        time_line = input_obj.readline()
        time_line = time_line.replace("Time:", "")
        t = int(time_line.replace(" ", "").strip())
        dist_line = input_obj.readline()
        dist_line = dist_line.replace("Distance:", "")
        d = int(dist_line.replace(" ", "").strip())
    return (t,d)

def winning_time_count(max_time, distance):
    winning = 0
    for t in range(max_time):
        calc_dist = t * (max_time - t)
        if calc_dist > distance:
            winning += 1
    print(winning)
    return winning


def part_1():
    td_tuple = parse_input()
    mult_val = 1
    for t, d in td_tuple:
        mult_val *= winning_time_count(t,d)

    return mult_val


def part_2():
    t,d = parse_input2()
    print(t,d)
    return winning_time_count(t,d)
    