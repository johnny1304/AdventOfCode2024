import pandas as pd
from numpy.core.getlimits import iinfo


def creategrid(df):
    arraygrid = []
    rows, cols = df.shape
    for row in range(rows):
        arraygrid.append(df.iloc[row].values.flatten().tolist())
    return arraygrid


def getStartPoints(arraygrid):
    startpoints = []
    for row in range(len(arraygrid)):
        for col in range(len(arraygrid[row])):
            if arraygrid[row][col] == 0:
                startpoints.append((row, col))
    return startpoints


def validStep(inputLines, step):
    if step[0] >= 0 and step[0]< len(inputLines) and step[1] >= 0 and step[1]< len(inputLines[0]):
        return True
    else:
        return False



def calcualteNextSteps(startpoint, inputlines):
    possibleSteps = [(startpoint[0] + 1, startpoint[1]), (startpoint[0], startpoint[1] + 1), (startpoint[0], startpoint[1] - 1), (startpoint[0] - 1, startpoint[1])]
    nextSteps = []
    for step in possibleSteps:
        if validStep(inputlines, step):
            # print("test STEP: ",str(inputlines[step[0]][step[1]]))
            # print("test STEP loc: ", str(step[1]),str(step[1]))
            if (inputlines[step[0]][step[1]] - inputlines[startpoint[0]][startpoint[1]]) == 1:
                # print("Success")
                nextSteps.append(step)
    return nextSteps




def calculateTotalTrailHeads(startPoints, inputlines):
    total=0
    for startpoint in startPoints:
        endpoints = set()
        nextSteps = calcualteNextSteps(startpoint, inputlines)
        while len(nextSteps)>0:
            secondHopSteps = []
            for nextStep in nextSteps:
                if inputlines[nextStep[0]][nextStep[1]] == 9:
                    endpoints.add(nextStep)
                else:
                    secondHopSteps.extend(calcualteNextSteps(nextStep, inputlines))
            nextSteps = secondHopSteps
        total += len(endpoints)
    return total


def part_one(input):
    if input is None:
        input = 'resources/input.txt'
    with open(input, 'r') as file:
        lines = file.readlines()
        inputlines = []
        for line in range(len(lines)):
            row = []
            for char in lines[line].strip("\n"):
                row.append(int(char))
            inputlines.append(row)
        startPoints = getStartPoints(inputlines)
        total = calculateTotalTrailHeads(startPoints, inputlines)
    print("answer:" + str(total))
    return total


def calculateAllPossibleRoutesToTrailHeads(startPoints, inputlines):
    totalRoutes = 0
    for startpoint in startPoints:
        nextSteps = calcualteNextSteps(startpoint, inputlines)
        while len(nextSteps) > 0:
            secondHopSteps = []
            for nextStep in nextSteps:
                if inputlines[nextStep[0]][nextStep[1]] == 9:
                    totalRoutes+=1
                else:
                    secondHopSteps.extend(calcualteNextSteps(nextStep, inputlines))
            nextSteps = secondHopSteps
    return totalRoutes

def part_two(input):
    if input is None:
        input = 'resources/input.txt'
    with open(input, 'r') as file:
        lines = file.readlines()
        inputlines = []
        for line in range(len(lines)):
            row = []
            for char in lines[line].strip("\n"):
                row.append(int(char))
            inputlines.append(row)
        startPoints = getStartPoints(inputlines)
        total = calculateAllPossibleRoutesToTrailHeads(startPoints, inputlines)
    print("answer:" + str(total))
    return total

# part_one(None)
part_two(None)