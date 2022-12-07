# Advent of Code, Day 6
import os

input_path = os.path.join(os.path.dirname(__file__), "input.txt")

def parse_input():
  with open(input_path) as input_obj:
    return input_obj.read();

def parse_buffer(buffer_length):
  datastream = parse_input()
  for index in range(buffer_length, len(datastream)):
    if len(set(datastream[index-buffer_length:index])) == buffer_length:
      return index
  else:
    return "ERROR"


def part_1():
  return parse_buffer(4)

def part_2():
  return parse_buffer(14)
