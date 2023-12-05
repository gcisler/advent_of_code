# Advent of Code, Day 8
import os

input_path = os.path.join(os.path.dirname(__file__), "input.txt")

def parse_input():
    forest_matrix = []
    with open(input_path) as input_obj:
        for line in input_obj.readlines():
            forest_matrix.append(list(map(int, list(line.strip()))))
    return forest_matrix
        
def part_1():
  forest_matrix = parse_input()

  # count all the edges
  visible_trees = 0
  visible_trees += len(forest_matrix) * 2
  visible_trees += (len(forest_matrix[0]) - 2) * 2

  # calculate interior
  # don't want to do this

def part_2():
  pass
    