# Advent of Code, Day 4
import os
import re
from collections import OrderedDict

input_path = os.path.join(os.path.dirname(__file__), "input.txt")

DIGITS_REGEX = re.compile(" (\d+)")
def parse_input():
    card_list = []
    with open(input_path) as input_obj:
        for line in input_obj.readlines():
            line = line.replace("Card: ", "").strip()
            card, line = line.split(':', 1)
            winning, have = line.split("|")
            winning = DIGITS_REGEX.findall(winning)
            have = DIGITS_REGEX.findall(have)
            card_list.append({'winning': winning, 'have': have, 'count': 1})
    return card_list

def part_1():
    card_list = parse_input()
    total = 0
    for card in card_list:
        matching = [n for n in card['winning'] if n in card['have']]
        if matching:
            points = 2**(len(matching)-1)
            total += points

    return total

def part_2():
    card_list = parse_input()
    total_cards = 0
    while(card_list):
        card_dict = card_list.pop(0)
        matching = [n for n in card_dict['winning'] if n in card_dict['have']]
        won = len(matching)
        card_dict['won'] = won
        total_cards += card_dict['count']
        print(card_dict, total_cards)
        for i in range(won):
            card_list[i]['count'] += card_dict['count']

    return total_cards


    # Once all of the originals and copies have been processed, you end up with 1
    #     instance of card 1, 2 instances of card 2, 4 instances of card 3, 8
    #     instances of card 4, 14 instances of card 5, and 1 instance of card 6.
    #     In total, this example pile of scratchcards causes you to ultimately have
    #     30 scratchcards!