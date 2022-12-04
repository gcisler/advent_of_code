
def parse_input():
    with open("input.txt") as input_obj:
        all_data = input_obj.readlines();

    return [_.rstrip() for _ in all_data]

def part1():
    # list of tuples
    duplicate_list = []
    priority_tally = 0
    for line in parse_input():
        length = len(line)
        assert length % 2 == 0
        first_comp = line[:length//2]
        second_comp = line[length//2:]
        duplicates = [item for item in first_comp if item in second_comp]
        # dedupe when a compartment has more of one item
        for dupe in set(duplicates):
            priority = calc_priority(dupe)
            priority_tally += priority
            duplicate_list.append(dupe)

    print("Total mismatched value priority: ", priority_tally)
    # 7795

def calc_priority(letter):
    # a is 97
    priority_val = ord(letter) - 96
    if priority_val < 0:
        # This is uppercase, which has a lower ord value
        # so make it positive (diff between a and A is 32)
        # and add 26 because upper is higher priority than lower
        priority_val += 32 + 26
    return priority_val

def part2():

    # split into groups of three
    input_list = parse_input()
    group_count = len(input_list)
    assert group_count % 3 == 0

    group_priority_tally = 0
    for i in range(0, group_count, 3):
        group_member = input_list[i:i+3]
        badge = [item for item in group_member[0] if (item in group_member[1] and item in group_member[2])]
        assert badge, "Group {i} is badgeless"
        assert len(set(badge)) == 1
        group_priority_tally += calc_priority(badge[0])

    print("Total group priority: ", group_priority_tally)


part1()
part2()

