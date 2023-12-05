# Advent of Code, Day 7
import os
import re
from collections import defaultdict

input_path = os.path.join(os.path.dirname(__file__), "input.txt")

class Dir:
    def __init__(self, name, parent):
        self.name = name
        self.parent = parent
        self.dir_size = 0
        self.ls_dirs = {}
        self.ls_files = {}

    def add_file(self, add_size):
        self.dir_size += add_size
        if self.parent:
            self.parent.add_file(add_size)

class File:
    def __init__(self, name, size):
        self.name = name
        self.size = size

CMD_UP_REGEX = re.compile("^\$ cd \.\.")
CMD_CD_REGEX = re.compile("^\$ cd (.+)")
CMD_LS_REGEX = re.compile("^\$ ls")

DIR_REGEX = re.compile("^dir (.+)")
FILE_REGEX = re.compile("^(\d+) (.+)")

def parse_input():
    filesystem = {}

    with open(input_path) as input_obj:
        all_lines = input_obj.readlines()

    curr_dir = None
    while (all_lines):
        line = all_lines.pop(0)
        if m := CMD_UP_REGEX.search(line):
            curr_dir = curr_dir.parent
            continue
        if m := CMD_CD_REGEX.search(line):
            dir_name = m.group(1)
            # manage the first instance
            if curr_dir:
                curr_dir = curr_dir.ls_dirs.get(dir_name, Dir(dir_name, curr_dir))
            else:
                curr_dir = Dir(dir_name, curr_dir)
            continue
        if CMD_LS_REGEX.search(line):
            while(all_lines):
                line = all_lines.pop(0)
                if line.startswith("$"):
                    # put back
                    all_lines.insert(0, line)
                    break
                if m:= DIR_REGEX.search(line):
                    dir_name = m.group(1)
                    curr_dir.ls_dirs[dir_name] = Dir(dir_name, curr_dir)
                elif m:= FILE_REGEX.search(line):
                    size = int(m.group(1))
                    curr_dir.ls_files[m.group(2)] = size
                    curr_dir.add_file(size)
                else:
                    raise FileNotFoundError("Cannot parse '%s'", line)
            continue

    # find top
    while curr_dir.parent:
        curr_dir = curr_dir.parent

    return curr_dir

def find_dir_lessthan(d, limit):
    valid_dirs = []
    if d.dir_size <= limit:
        valid_dirs.append(d.dir_size)
    # now add subdirs
    for sub_dir in d.ls_dirs.values():
        valid_dirs.extend(find_dir_lessthan(sub_dir, limit))
    return valid_dirs


def part_1():

    top_dir = parse_input()
    return sum(find_dir_lessthan(top_dir, 100000))
    # 1543140


def part_2():
    MAX_SPACE = 70000000
    RUN_SPACE = 30000000
    top_dir = parse_input()
    free_space = MAX_SPACE - top_dir.dir_size
    if free_space > RUN_SPACE:
        return 0
    else:
        print("Looking for dir at least ", RUN_SPACE )
        valid_dirs = find_dir_lessthan(top_dir, RUN_SPACE)
        valid_dirs = [d for d in valid_dirs if d > RUN_SPACE - free_space]
        return min(valid_dirs)
    