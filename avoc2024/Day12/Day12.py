from collections import Counter

from Cython.Utils import OrderedSet


def creategrid(df):
    arraygrid = []
    rows, cols = df.shape
    for row in range(rows):
        arraygrid.append(df.iloc[row].values.flatten().tolist())
    return arraygrid

def validStep(inputLines, step):
    if step[0] >= 0 and step[0]< len(inputLines) and step[1] >= 0 and step[1]< len(inputLines[0]):
        return True
    else:
        return False

def getAreaAndPerim (startpoint, visited, perims, areas, inputlines,):
    nextSteps = getNextSteps(startpoint, inputlines)
    totalArea = 0
    if len(nextSteps) == 0:
        perims[inputlines[startpoint[0]][startpoint[1]] + str(startpoint)] = 4
        visited.add(startpoint)
        totalArea += 1
    while len(nextSteps) > 0:
        secondHopSteps = []
        for nextStep in nextSteps:
            if nextStep in visited:
                continue
            else:
                newNextStep = getNextSteps(nextStep, inputlines)
                perims[inputlines[nextStep[0]][nextStep[1]]+str(startpoint)] = perims.get(inputlines[nextStep[0]][nextStep[1]]+str(startpoint),0)+(4-len(newNextStep))
                secondHopSteps.extend(getNextSteps(nextStep, inputlines))
                visited.add(nextStep)
                totalArea+=1
        nextSteps = secondHopSteps
    areas[inputlines[startpoint[0]][startpoint[1]]+str(startpoint)] = totalArea

def getNextSteps(startpoint,inputlines):
    possibleSteps = [(startpoint[0] + 1, startpoint[1]), (startpoint[0], startpoint[1] + 1),
                     (startpoint[0], startpoint[1] - 1), (startpoint[0] - 1, startpoint[1])]
    nextSteps = []
    for step in possibleSteps:
        if validStep(inputlines, step):
            if inputlines[step[0]][step[1]] == inputlines[startpoint[0]][startpoint[1]]:
                nextSteps.append(step)
    return nextSteps


def part_one(input):
    if input is None:
        input = 'resources/input.txt'
    with open(input, 'r') as file:
        lines = file.readlines()
        inputlines = []
        for line in range(len(lines)):
            row = []
            for char in lines[line].strip("\n"):
                row.append(char)
            inputlines.append(row)
        perims = Counter()
        areas = Counter()
        visited = set()
        for line in range(len(inputlines)):
            for point in range(len(inputlines[line])):
                currPoint = (line, point)
                if currPoint not in visited:
                    getAreaAndPerim(currPoint,visited, perims, areas, inputlines)
        totalCost = 0
        for key in areas.keys():
            totalCost += areas[key] * perims[key]
    print("answer:" + str(totalCost))
    return totalCost

# part_one(None)


def getSides(startpoint, nextSteps):
    possibleSteps = {(startpoint[0] + 1, startpoint[1]):"b", (startpoint[0], startpoint[1] + 1):"r",
                     (startpoint[0], startpoint[1] - 1):"l", (startpoint[0] - 1, startpoint[1]):"t"}
    sides = set()
    for step in possibleSteps:
        if step not in nextSteps:
            sides.add(possibleSteps[step])
    return sides


def calulateSidesFromEdges(edges):

    bottomEdges = list(OrderedSet(edges.get("b",[])))
    topEdges = list(OrderedSet(edges.get("t",[])))
    rightEdges = list(OrderedSet(edges.get("r",[])))
    leftEdges = list(OrderedSet(edges.get("l",[])))
    bCount = 0
    tCount = 0
    rCount = 0
    lCount = 0

    for node in bottomEdges:

        if (node[0],node[1]+1) not in bottomEdges:

            bCount+=1


    for node in topEdges:

        if (node[0],node[1]+1) not in topEdges:
            tCount += 1

    for node in rightEdges:
        if (node[0]+1,node[1]) not in rightEdges:
            rCount += 1

    for node in leftEdges:
        if (node[0]+1,node[1]) not in leftEdges:
            lCount += 1


    return bCount+tCount+rCount+lCount






def getAreaAndPerimBasedSide (startpoint, visited, perims, areas, inputlines,):
    nextSteps = getNextSteps(startpoint, inputlines)
    sides = dict()
    edges = dict()
    if len(nextSteps) == 0:
        edges['b'] = [startpoint]
        edges['t'] = [startpoint]
        edges['l'] = [startpoint]
        edges['r'] = [startpoint]
    for i in nextSteps:
        sides[i] = getSides(startpoint, nextSteps)
        for d in sides[i]:
            if d not in edges:
                edges[d] = [startpoint]
            else:
                edges.get(d).append(startpoint)


    perims[inputlines[startpoint[0]][startpoint[1]] + str(startpoint)] = perims.get(
            inputlines[startpoint[0]][startpoint[1]] + str(startpoint), 0) +  4- len(sides)

    totalArea = 1
    visited.add(startpoint)

    totalArea = loopsides(inputlines, nextSteps, perims, sides, startpoint, totalArea, visited, edges)


    totalSides = calulateSidesFromEdges(edges)
    perims[inputlines[startpoint[0]][startpoint[1]] + str(startpoint)] = totalSides
    areas[inputlines[startpoint[0]][startpoint[1]]+str(startpoint)] = totalArea


def loopsides(inputlines, nextSteps, perims, sides, startpoint, totalArea, visited, edges):
    while len(nextSteps) > 0:
        secondHopSteps = []
        for nextStep in nextSteps:
            if nextStep in visited:
                continue
            else:
                newNextStep = getNextSteps(nextStep, inputlines)
                nextSides = getSides(nextStep, newNextStep)
                diff = nextSides.difference(sides[nextStep])

                for d in nextSides:
                    if d not in edges:
                        edges[d] = [nextStep]
                    else:
                        edges.get(d).append(nextStep)
                for d in diff:
                    if d in nextSides:
                        perims[inputlines[nextStep[0]][nextStep[1]] + str(startpoint)] = perims.get(
                            inputlines[nextStep[0]][nextStep[1]] + str(startpoint), 0) + 1
                for i in newNextStep:
                    sides[i] = nextSides
                secondHopSteps.extend(getNextSteps(nextStep, inputlines))
                visited.add(nextStep)
                totalArea += 1
        nextSteps = secondHopSteps
    return totalArea


def part_two(input):
    if input is None:
        input = 'resources/input.txt'
    with open(input, 'r') as file:
        lines = file.readlines()
        inputlines = []
        for line in range(len(lines)):
            row = []
            for char in lines[line].strip("\n"):
                row.append(char)
            inputlines.append(row)
        perims = Counter()
        areas = Counter()
        visited = set()
        for line in range(len(inputlines)):
            for point in range(len(inputlines[line])):
                currPoint = (line, point)
                if currPoint not in visited:
                    getAreaAndPerimBasedSide(currPoint,visited, perims, areas, inputlines)
        totalCost = 0
        for key in areas.keys():
            totalCost += areas[key] * perims[key]


    print("answer:" + str(totalCost))
    return totalCost

part_two(None)