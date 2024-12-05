import math
from collections import OrderedDict

import pandas as pd


def middleItem(line):
    size = len(line)
    return int(list(line.items())[int(math.floor(size / 2))][0])

def calculateSafeLines(order, lineInputs):
    total = 0
    for line in lineInputs:
        if checkLineSafe(line, order):
            total += middleItem(line)
    return total


def checkLineSafe(line, order):
    for page in line:
        if page in order:
            before = order[page]
            for item in before:
                if item in line:
                    if line[page] < line[item]:
                        continue
                    else:
                        return False
    return True


def part_one(input):
    total = 0
    order = {}
    firstSection = True
    lineInputs =[]
    if input is None:
        input = 'resources/input.txt'
    with open(input, 'r') as file:
        lines = file.readlines()
        for line in lines:
            if line == "\n":
                firstSection = False
            elif firstSection:
                keys = line.strip("\n").split("|")
                if keys[0] not in order:
                    order[keys[0]] = [keys[1]]
                else:
                    order[keys[0]].append(keys[1])
            else:
                pages = OrderedDict()
                count = 1
                for page in line.strip("\n").split(","):
                    pages[page] = count
                    count+=1
                lineInputs.append(pages)

    print(order)
    print(lineInputs)
    ans = calculateSafeLines(order, lineInputs)
    print (ans)
    return ans


def reorderLine(line, order):
    while not checkLineSafe(line, order):
        for page in line:
            if page in order:
                before = order[page]
                for item in before:
                    if item in line:
                        if line[page] > line[item]:
                            itemIndex = line[item]
                            pageIndex = line[page]
                            line[item] = pageIndex
                            line[page] = itemIndex
    linereordered = ["" for _ in range(len(line))]
    for page in line:
        linereordered[line[page]-1] = page
    return linereordered


def middleItemList(fixedline):
    size = len(fixedline)
    print(fixedline)
    return int(fixedline[int(math.floor(size / 2))])


def calculateAndCorrectInccorectLines(order, lineInputs):
    total = 0
    for line in lineInputs:
        if not checkLineSafe(line, order):
            fixedline = reorderLine(line, order)
            total += middleItemList(fixedline)
    return total


def part_two(input):
    total = 0
    order = {}
    firstSection = True
    lineInputs =[]
    if input is None:
        input = 'resources/input.txt'
    with open(input, 'r') as file:
        lines = file.readlines()
        for line in lines:
            if line == "\n":
                firstSection = False
            elif firstSection:
                keys = line.strip("\n").split("|")
                if keys[0] not in order:
                    order[keys[0]] = [keys[1]]
                else:
                    order[keys[0]].append(keys[1])
            else:
                pages = OrderedDict()
                count = 1
                for page in line.strip("\n").split(","):
                    pages[page] = count
                    count+=1
                lineInputs.append(pages)

    print(order)
    print(lineInputs)
    ans = calculateAndCorrectInccorectLines(order, lineInputs)
    print (ans)
    return ans
part_two(None)
