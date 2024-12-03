import re

def part_one(input):
    total = 0
    if input is None:
        input = 'resources/input.txt'
    with open(input, 'r') as file:
        lines = file.readlines()
        for line in lines:
            parts = find_all_matches("mul\(\d+,\d+\)",line)
            for part in parts:
                inputs = part.split("(")[1].split(")")[0].split(",")
                total += int(inputs[0]) * int(inputs[1])
        print(total)
        return total


def find_all_matches(pattern, string, group=0):
    pat = re.compile(pattern)
    pos = 0
    out = []
    while m := pat.search(string, pos):
        pos = m.start() + 1
        out.append(m[group])
    return out


def extractActiveMultiplication(complete_line):
    donts = complete_line.split("don't()")
    do = ""
    for i in range(0, len(donts)):
        if i==0:
            do = do+donts[i]
        else:
            dos = donts[i].split("do()")
            for i in range(1,len(dos)):
                do = do + dos[i]
    return do





def part_two(input):
    total = 0
    if input is None:
        input = 'resources/input.txt'
    with open(input, 'r') as file:
        lines = file.readlines()
        complete_line = ""
        for line in lines:
            complete_line = complete_line+line.strip("\n")
        active_muls = extractActiveMultiplication(complete_line)
        total = extractAndMultiply(active_muls, total)
        print(total)
        return total


def extractAndMultiply(line, total):
    parts = find_all_matches("mul\(\d+,\d+\)", line)
    for part in parts:
        inputs = part.split("(")[1].split(")")[0].split(",")
        total += int(inputs[0]) * int(inputs[1])
    return total


part_two(None)