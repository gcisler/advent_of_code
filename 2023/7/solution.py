# Advent of Code, Day 7
from collections import defaultdict
from functools import cmp_to_key
import os

input_path = os.path.join(os.path.dirname(__file__), "input.txt")
CARDS = ['A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2']



# secondary ordering
    # compare first cards, then second card, etc


def compare_cards(first, second):
    first_index = CARDS.index(first)
    second_index = CARDS.index(second)
    if first_index < second_index:
        return 1
    elif first_index > second_index:
        return -1
    else:
        return 0


def compare_hands(hand1, hand2):
    hand1_c = categorize_hand(hand1[0])
    hand2_c = categorize_hand(hand2[0])
    if hand1_c > hand2_c:
        return 1
    elif hand1_c < hand2_c:
        return -1
    else:
        # compare letters
        for index in range(5):
            letter_comp = compare_cards(hand1[0][index], hand2[0][index])
            if not letter_comp:
                # equal values
                continue
            else:
                return letter_comp

def categorize_hand(hand):
    # options
    # 6 five
    # 5 four
    # 4 full: 3 and 2
    # 3 three: three of a kind, random others
    # 2 two: two pairs
    # 1 high: 5 distinct cards
    # 0 nothing
    hand_dict = defaultdict(int)
    for c in hand:
        hand_dict[c] += 1

    vals = list(hand_dict.values())
    vals.sort()
    match len(hand_dict):
        case 1:
            # five of a kind
            return 6
        case 2:
            if vals == [2,3]:
                # full house
                return 4
            elif vals == [1,4]:
                # four of a kind
                return 5
        case 3:
            if vals == [1,1,3]:
                # three of a kind
                return 3
            if vals == [1,2,2]:
                # two pairs
                return 2
        case 4:
            # nothing
            return 0
        case 5:
            # high
            return 1

def parse_input():
    hand_bid_list = []
    with open(input_path) as input_obj:
        for line in input_obj.readlines():
            hand, bid = line.strip().split(" ")
            hand_bid_list.append((hand, int(bid)))
    return hand_bid_list
        
def part_1():
    hand_bid_list = parse_input()
    hand_bid_list = sorted(hand_bid_list, key=cmp_to_key(compare_hands))

    total_winning = 0
    for index, hand_bid in enumerate(hand_bid_list):
        this_round = (index+1) * hand_bid[1]
        total_winning += this_round
    return total_winning


def part_2():
    pass
    