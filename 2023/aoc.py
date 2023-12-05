"""Advent of code runner
Copied from https://github.com/jagath-jaikumar/advent_of_code/blob/main/aoc.py

Usage:
  aoc.py day <day_number> [--timed]
  aoc.py generate <day_number>
  aoc.py (-h | --help)
  aoc.py --version

Options:
  -h --help     Show this screen.
  --version     Show version.
  --timed       Run with timer
"""
from docopt import docopt
import importlib
import time
import sys
import os

def day(args):
    try:
        i = importlib.import_module(f"{args['<day_number>']}.solution", package=".")
    except Exception:
        print("No such day available")
        sys.exit(1)

    a = time.time()
    print("Part1:", i.part_1())
    if args['--timed']:
        print(f"Part 1 Solution time: {time.time()-a} seconds")

    b = time.time()
    print("Part1:", i.part_2())
    if args['--timed']:
        print(f"Part 2 Solution time: {time.time()-b} seconds")


def generate(args):
    path = os.path.join(os.path.dirname(__file__), args['<day_number>'])
    if os.path.exists(path):
        print("Day already exists")
        return

    os.makedirs(args['<day_number>'])
    with open(f"{args['<day_number>']}/input.txt", 'w') as f:
        pass

    with open(f"{args['<day_number>']}/solution.py", 'w') as f:
        f.write(f"""# Advent of Code, Day {args['<day_number>']}
import os

input_path = os.path.join(os.path.dirname(__file__), "input.txt")

def parse_input():
    with open(input_path) as input_obj:
        return input_obj.readlines()
        
def part_1():
  pass

def part_2():
  pass
    """)

if __name__ == '__main__':
    args = docopt(__doc__, version='Advent of Code runner 1.0')

    if args['day']:
        day(args)
    elif args['generate']:
        generate(args)

