# Advent of Code, Day 2
import os
import re
import math

input_path = os.path.join(os.path.dirname(__file__), "input.txt")

bag_limit_dict = {'red': 12,
                  'green': 13,
                  'blue': 14}

CUBE_REGEX = re.compile("(\d+) ([red|green|blue]+)")

def parse_input():
    with open(input_path) as input_obj:
        all_games = {}
        for line in input_obj.readlines():
            # remove game
            line = line.replace("Game ", "").strip()
            game, line = line.split(':', 1)
            grabs_str = line.split(';')
            all_games[int(game)] = [CUBE_REGEX.findall(grab) for grab in grabs_str]
    return all_games
        
def part_1():
  id_total = 0
  all_games = parse_input()
  for game, grab_list in all_games.items():
      for grab in grab_list:
          for count, color in grab:
              if int(count) > bag_limit_dict[color]:
                  break
          else:
              continue
          break
      else:
          id_total += game

  return id_total

def minimum_game_power(grab_list):
    min_dict = {'red': 0, 'green': 0, 'blue': 0}
    for grab in grab_list:
        for count, color in grab:
            min_dict[color] = max(min_dict[color], int(count))

    return math.prod(min_dict.values())

def part_2():
    product_total = 0
    all_games = parse_input()
    for grab_list in all_games.values():
        product_total += minimum_game_power(grab_list)

    return product_total

    