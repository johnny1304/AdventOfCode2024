import copy

import pandas as pd


def creategrid(df):
    arraygrid = []
    rows, cols = df.shape
    for row in range(rows):
        arraygrid.append(df.iloc[row].values.flatten().tolist())
    return arraygrid


def isValidNodes(currNode, currPos, cols, rows):
    if (currNode[0] > cols - 1 or currNode[0] < 0) and (currPos[0] > cols - 1 or currPos[0] < 0):
        return False
    elif (currNode[1] > rows - 1 or currNode[1] < 0) and (currPos[1] > rows - 1 or currPos[1] < 0):
        return False
    else:
        return True


def calculateAntinodeLocations(arraygrid):
    rows = len(arraygrid)
    cols = len(arraygrid[0])
    nodes = dict()
    antinodes = set()
    for row in range(rows):
        for col in range(cols):
            if arraygrid[row][col]!=('.'):
                if(nodes.get(arraygrid[row][col]) != None):
                    nodes.get(arraygrid[row][col]).append((col, row))
                else:
                    nodes[arraygrid[row][col]] = [(col,row)]

    for node in nodes:
        for i in range(len(nodes[node])-1):
            pos = copy.deepcopy(i)+1
            while pos < len(nodes[node]):
                antinodes.add((nodes[node][i][0],nodes[node][i][1]))
                antinodes.add((nodes[node][pos][0],nodes[node][pos][1]))
                xDiff = abs(nodes[node][i][0] - nodes[node][pos][0])
                yDiff = abs(nodes[node][i][1] - nodes[node][pos][1])
                currNode = copy.deepcopy(nodes[node][i])
                currPos = copy.deepcopy(nodes[node][pos])
                while isValidNodes(currNode , currPos , cols, rows):
                    if currNode[0] >  currPos[0]:
                        xnode = currNode[0] + xDiff
                        xpos = currPos[0] - xDiff
                    else:
                        xnode = currNode[0] - xDiff
                        xpos = currPos[0] + xDiff

                    if currNode[1] > currPos[1]:
                        ynode = currNode[1] + yDiff
                        ypos = currPos[1] - yDiff
                    else:
                        ynode = currNode[1] - yDiff
                        ypos = currPos[1] + yDiff
                    antinodes.add((xnode,ynode))
                    antinodes.add((xpos, ypos))
                    currNode = (xnode,ynode)
                    currPos = (xpos, ypos)
                pos+=1
    removeList = []
    for antinode in antinodes:
        if antinode[0]>cols-1 or antinode[0]<0:
            removeList.append(antinode)
        elif antinode[1]>rows-1 or antinode[1]<0:
            removeList.append(antinode)
    for antinode in removeList:
        antinodes.remove(antinode)
    return len(antinodes)


def part_two(input):
    if input is None:
        input = 'resources/input.txt'
    with open(input, 'r') as file:
        lines = file.readlines()
        inputlines = [[] for _ in range(len(lines))]
        for line in range(len(lines)):
            for char in lines[line].strip("\n"):
                inputlines[line].append(char)
        df = pd.DataFrame(inputlines)
        arraygrid = creategrid(df)
        totalAntinodes = calculateAntinodeLocations(arraygrid)
    print(totalAntinodes)
    return totalAntinodes

# part_two(None)