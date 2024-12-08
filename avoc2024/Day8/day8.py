import copy

import pandas as pd


def creategrid(df):
    arraygrid = []
    rows, cols = df.shape
    for row in range(rows):
        arraygrid.append(df.iloc[row].values.flatten().tolist())
    return arraygrid


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
                xDiff = abs(nodes[node][i][0] - nodes[node][pos][0])
                yDiff = abs(nodes[node][i][1] - nodes[node][pos][1])
                xnode = 0
                ynode = 0
                xpos = 0
                ypos = 0
                if nodes[node][i][0] > nodes[node][pos][0]:
                    xnode = nodes[node][i][0] + xDiff
                    xpos = nodes[node][pos][0] - xDiff
                else:
                    xnode = nodes[node][i][0] - xDiff
                    xpos = nodes[node][pos][0] + xDiff

                if nodes[node][i][1] > nodes[node][pos][1]:
                    ynode = nodes[node][i][1] + yDiff
                    ypos = nodes[node][pos][1] - yDiff
                else:
                    ynode = nodes[node][i][1] - yDiff
                    ypos = nodes[node][pos][1] + yDiff
                antinodes.add((xnode,ynode))
                antinodes.add((xpos, ypos))
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


def part_one(input):
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

# part_one(None)