#/usr/bin/python

def parse_input():
    with open("input.txt") as input_obj:
        all_data = input_obj.read();

    return all_data.split("\n\n")

def part1():
    elf_groups = parse_input()
    max_tally = 0
    for single_elf in elf_groups:
        tally = sum(int(count) for count in single_elf.split("\n"))
        if tally > max_tally:
            max_tally = tally
    print("Max single elf: ", max_tally)
    return max_tally

#Part2 Find the top three values
def part2():
    elf_groups = parse_input()
    all_tally = []
    for single_elf in elf_groups:
        tally = sum(int(count) for count in single_elf.split("\n"))
        all_tally.append(tally)

    sorted_tally = sorted(all_tally, reverse=True)
    topthree = sum(sorted_tally[:3])
    print("Max top three: ", topthree)



part1()
part2()
