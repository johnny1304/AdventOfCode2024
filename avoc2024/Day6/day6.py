import copy

import pandas as pd

def creategrid(df):
    arraygrid = []
    rows, cols = df.shape
    for row in range(rows):
        arraygrid.append(df.iloc[row].values.flatten().tolist())
    return arraygrid


def isObstacle(nextSquare, arraygrid):
    # print(nextSquare)
    # print(arraygrid[nextSquare[0]][nextSquare[1]])
    return arraygrid[nextSquare[0]][nextSquare[1]] == "#"


def calculatePathSquares(arraygrid, soldierPos):
    width = len(arraygrid[0])
    height = len(arraygrid)
    direction = 1
    pathsquares= set()
    while isValidCoordinate(height, soldierPos, width):
        print("soldier"+str(soldierPos))
        print(direction)
        pathsquares.add((soldierPos[0], soldierPos[1]))
        if direction == 1:
            nextSquare = (soldierPos[0]-1,soldierPos[1])
            if isValidCoordinate(height, nextSquare, width) and isObstacle(nextSquare,arraygrid):
                direction = changeDirection(direction)
            else:
                soldierPos= (soldierPos[0]-1,soldierPos[1])
        elif direction == 2:
            nextSquare = (soldierPos[0],soldierPos[1]+1)
            if isValidCoordinate(height, nextSquare, width) and isObstacle(nextSquare,arraygrid):
                direction = changeDirection(direction)
            else:
                soldierPos= (soldierPos[0],soldierPos[1]+1)
        elif direction == 3:
            nextSquare = (soldierPos[0]+1,soldierPos[1])
            if isValidCoordinate(height, nextSquare, width) and isObstacle(nextSquare,arraygrid):
                direction = changeDirection(direction)
            else:
                soldierPos= (soldierPos[0]+1,soldierPos[1])
        elif direction == 4:
            nextSquare = (soldierPos[0],soldierPos[1]-1)
            if isValidCoordinate(height, nextSquare, width) and isObstacle(nextSquare,arraygrid):
                direction = changeDirection(direction)
            else:
                soldierPos = (soldierPos[0],soldierPos[1]-1)
    return len(pathsquares)

def changeDirection(direction):
    if direction != 4:
        direction += 1
    else:
        direction = 1
    return direction


def isValidCoordinate(height, soldierPos, width):
    return soldierPos[0] >= 0 and soldierPos[1] >= 0 and soldierPos[0] < width and soldierPos[1] < height


def part_one(input):
    total = 0
    soldierPos = ()
    if input is None:
        input = 'resources/input.txt'
    with open(input, 'r') as file:
        lines = file.readlines()
        inputlines = [[] for _ in range(len(lines))]
        row = 0
        for line in range(len(lines)):
            col = 0
            for char in lines[line].strip("\n"):
                inputlines[line].append(char)
                if char == '^':
                    soldierPos = (row, col)
                col+=1
            row+=1
        df = pd.DataFrame(inputlines)
        arraygrid = creategrid(df)
    total = calculatePathSquares(arraygrid,soldierPos)
    print(total)
    return total


def checkLoop(soldierPos, nextSquare, pathsquares):
    if soldierPos in pathsquares and nextSquare in pathsquares:
        return True


def calculateLoopsSquares(arraygrid, soldierPos):
    width = len(arraygrid[0])
    height = len(arraygrid)
    direction = 1
    pathsquares = set()
    while isValidCoordinate(height, soldierPos, width):
        # print("soldier" + str(soldierPos))
        # print(direction)
        if pathsquares.__contains__((soldierPos[0], soldierPos[1], direction)):
            return True
        pathsquares.add((soldierPos[0], soldierPos[1], direction))
        if direction == 1:
            nextSquare = (soldierPos[0] - 1, soldierPos[1])
            if isValidCoordinate(height, nextSquare, width) and isObstacle(nextSquare, arraygrid):
                direction = changeDirection(direction)
            else:
                soldierPos = (soldierPos[0] - 1, soldierPos[1])
        elif direction == 2:
            nextSquare = (soldierPos[0], soldierPos[1] + 1)
            if isValidCoordinate(height, nextSquare, width) and isObstacle(nextSquare, arraygrid):
                direction = changeDirection(direction)
            else:
                soldierPos = (soldierPos[0], soldierPos[1] + 1)
        elif direction == 3:
            nextSquare = (soldierPos[0] + 1, soldierPos[1])
            if isValidCoordinate(height, nextSquare, width) and isObstacle(nextSquare, arraygrid):
                direction = changeDirection(direction)
            else:
                soldierPos = (soldierPos[0] + 1, soldierPos[1])
        elif direction == 4:
            nextSquare = (soldierPos[0], soldierPos[1] - 1)
            if isValidCoordinate(height, nextSquare, width) and isObstacle(nextSquare, arraygrid):
                direction = changeDirection(direction)
            else:
                soldierPos = (soldierPos[0], soldierPos[1] - 1)
    return False

def part_two(input):
    total = 0
    soldierPos = ()
    if input is None:
        input = 'resources/input.txt'
    with open(input, 'r') as file:
        lines = file.readlines()
        inputlines = [[] for _ in range(len(lines))]
        row = 0
        for line in range(len(lines)):
            col = 0
            for char in lines[line].strip("\n"):
                inputlines[line].append(char)
                if char == '^':
                    soldierPos = (row, col)
                col+=1
            row+=1
        df = pd.DataFrame(inputlines)
        arraygrid = creategrid(df)
    row, col = df.shape

    for r in range(row):
        for c in range(col):
            arraygridEdited = copy.deepcopy(arraygrid)
            arraygridEdited[r][c] = '#'
            if calculateLoopsSquares(arraygridEdited,soldierPos):
                total+=1
    print(total)
    return total
part_two(None)