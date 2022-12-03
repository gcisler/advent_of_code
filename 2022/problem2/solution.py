# /usr/bin/python

ROCK = 1
PAPER = 2
SCISSORS = 3


def parse_input():
    with open("input.txt") as input_obj:
        all_data = input_obj.readlines();

    return [_.rstrip().split(" ") for _ in all_data]

WINS_DICT = {ROCK: SCISSORS,
             PAPER: ROCK,
             SCISSORS: PAPER}

LOSE_DICT = {v:k for k,v in WINS_DICT.items()}

SYMBOL_DICT = {"A": ROCK,
            "B": PAPER,
            "C": SCISSORS}

ASSUMPTION_DICT = {"X": ROCK,
                   "Y": PAPER,
                   "Z": SCISSORS}

def follow_strategy():

    total_score = 0
    # ignore the second column of the input
    for opponent, personal in parse_input():
        opponent_choice = SYMBOL_DICT[opponent]
        personal_choice = ASSUMPTION_DICT[personal]
        round_score = personal_choice
        if opponent_choice == personal_choice:
            # draw
            round_score += 3
        elif opponent_choice == WINS_DICT[personal_choice]:
            # strategy wins
            round_score += 6
        else:
            # opponent wins
            round_score += 0
        total_score += round_score

    print("Total Score: ", total_score)
    return total_score
    # not 13631
    # second guess: 13675

def follow_new_strategy():
    total_score = 0

    for opponent, decision in parse_input():
        opponent_choice = SYMBOL_DICT[opponent]
        round_score = 0
        match decision:
            case "X":
                # lose
                personal_choice = LOSE_DICT[opponent_choice]
            case "Y":
                # draw
                personal_choice = opponent_choice
                round_score += 3
            case "Z":
                # win
                personal_choice = WINS_DICT[opponent_choice]
                round_score += 6
        round_score += personal_choice

        total_score += round_score

    print("New Total Score: ", total_score)
    return total_score
    # too high 14585

follow_strategy()
follow_new_strategy()