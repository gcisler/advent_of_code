# Advent of Code, Day 5
import os
import re
import itertools

MAPPER_REGEX = re.compile(r"(\w+)-to-(\w+) map:")
NUMBER_REGEX = re.compile(r'(\d+) (\d+) (\d+)')
input_path = os.path.join(os.path.dirname(__file__), "input.txt")


class MapMaster:
    def __init__(self):
        self.seeds = []
        self.seed_pair_iter = []
        self.mapping = {}
        self.range_vals = {}

    def get_seed_location(self, search_num):
        map_val = 'seed'
        while map_val in self.mapping:
            temp_map_dict = self.range_vals[map_val]
            for m_range, m_diff in temp_map_dict.items():
                if search_num in m_range:
                    search_num += m_diff
                    break
            else:
                # search_num stays the same
                pass
            map_val = self.mapping[map_val]

        return search_num


def parse_input():
    m = MapMaster()
    map_from = ""
    map_to = ""
    with open(input_path) as input_obj:
        seed_line = input_obj.readline()
        seed_line = seed_line.replace("seeds: ", "")
        m.seeds = list(map(int, seed_line.split(" ")))
        seed_pair = itertools.batched(m.seeds, 2)
        m.seed_pair_iter = itertools.chain.from_iterable([range(a,a+b) for a,b in seed_pair])

        for line in input_obj.readlines():
            line = line.strip()
            if not line:
                # reset mapping values
                map_from = ""
                map_to = ""
                continue

            # assume number mapping so check this first
            num_reg = NUMBER_REGEX.match(line)
            # if match assume correct length
            if num_reg:
                dest_start, source_start, range_len = map(int, num_reg.groups())
                diff_start = dest_start - source_start
                # also assume we have already defined map_from and map_to
                m.range_vals[map_from][range(source_start, source_start + range_len)] = diff_start


            else:
                map_reg = MAPPER_REGEX.match(line)
                if map_reg:
                    map_from, map_to = map_reg.groups()
                    m.mapping[map_from] = map_to
                    m.range_vals[map_from] = {}

        return m

        
def part_1():
    m = parse_input()
    return min([m.get_seed_location(s) for s in m.seeds])


def part_2():
    m = parse_input()
    return min([m.get_seed_location(s) for s in m.seed_pair_iter])
    