import copy
from collections import Counter

from Tools.demo.sortvisu import steps
from numpy.testing.print_coercion_tables import print_new_cast_table


def rearrangeStones(stoneCounter):
    newStones=Counter()
    for stone,n in stoneCounter.items():
        if stone == 0:
            newStones[1] = newStones.get(1,0) + (1*n)
        elif len(str(stone)) % 2 == 0:
            strStone = str(stone)

            firstHalf = int(strStone[0:len(strStone)//2])
            secondHalf = int(strStone[len(strStone) // 2:len(strStone)])

            newStones[firstHalf] = newStones.get(firstHalf, 0)+(1*n)
            newStones[secondHalf] = newStones.get(secondHalf, 0)+(1*n)
        else:
            val = stone * 2024
            newStones[val] = newStones.get(val, 0)+(1*n)
    return newStones



def part_one(input, blinks):
    if input is None:
        input = 'resources/input.txt'
    with open(input, 'r') as file:
        lines = file.readlines()
        stones = []
        stoneCounter = Counter()
        for line in lines:
            stones.extend( line.strip("").split(" "))
        for stone in stones:
            stoneCounter[int(stone)] = 1
        while blinks>0:
            stoneCounter = rearrangeStones(stoneCounter)
            blinks-=1
        total = stoneCounter.total()
        print("answer:" + str(total))
        return total

part_one(None,75)