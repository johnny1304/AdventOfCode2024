import re
from shutil import copy2

import numpy
import pandas as pd
from pandas.core.interchange.dataframe_protocol import DataFrame


def find_all_matches(pattern, string, group=0):
    return len(re.findall(pattern,string))


def searchDiagonals(df):
    rows, cols = df.shape
    count = 0
    for i in range(cols + rows -1):
        count += find_all_matches("XMAS", "".join(numpy.diag(df,-i)))
        count += find_all_matches("SAMX", "".join(numpy.diag(df,-i)))
        if i != 0:
            count += find_all_matches("XMAS", "".join(numpy.diag(df, i)))
            count += find_all_matches("SAMX", "".join(numpy.diag(df, i)))
        print("".join(numpy.diag(df, -i)))
    inverted = []
    for row in range(rows):
        l = df.iloc[row].values.flatten().tolist()
        l.reverse()
        inverted.append(l)
    idf = pd.DataFrame(inverted)
    print(idf)
    for i in range(cols + rows -1):
        count += find_all_matches("XMAS", "".join(numpy.diag(idf, -i)))
        count += find_all_matches("SAMX", "".join(numpy.diag(idf, -i)))
        if i != 0:
            count += find_all_matches("XMAS", "".join(numpy.diag(idf, i)))
            count += find_all_matches("SAMX", "".join(numpy.diag(idf, i)))
    print("Diagonal:" + str(count))
    return count

def searchHorizontal(df):
    rows, cols = df.shape
    count = 0
    for i in range(rows):
         input = "".join(df.iloc[i])
         count += find_all_matches("XMAS", input)
         count += find_all_matches("SAMX", input)
         print("".join(df.iloc[i]))
         print(count)
    print("Horizontal:" + str(count))
    return count

def searchVertical(df):
    rows, cols = df.shape
    count = 0
    for i in range(cols):
        count += find_all_matches("XMAS", "".join(df[i].values.tolist()))
        count += find_all_matches("SAMX", "".join(df[i].values.tolist()))
    return count


def part_one(input):
    total = 0
    if input is None:
        input = 'resources/input.txt'
    with open(input, 'r') as file:
        lines = file.readlines()
        inputlines = [[] for _ in range(len(lines))]
        for line in range(len(lines)):
            for char in lines[line].strip("\n"):
                inputlines[line].append(char)
        df =pd.DataFrame(inputlines)
        total += searchHorizontal(df)
        total += searchVertical(df)
        total += searchDiagonals(df)
    print(total)
    return total


def allValidCoordinates(tl, br, tr, bl, height, width):
    if (0 <= tl[0] < height and
            0 <= tl[1] < width and
            0 <= br[0] < height and
            0 <= br[1] < width and
            0 <= tr[0] < height and
            0 <= tr[1] < width  and
            0 <= bl[0] < height and
            0 <= bl[1] < width):
        return True


def checkCross(ag, row, col, height, width):
    tl = (row-1,col-1)
    br = (row+1,col+1)
    tr = (row-1,col+1)
    bl = (row+1,col-1)
    if allValidCoordinates(tl,br,tr,bl, height,width):
        if (ag[tl[0]][tl[1]]=="M" and ag[tr[0]][tr[1]]=="S" and ag[bl[0]][bl[1]]=="M" and ag[br[0]][br[1]]=="S"):
            print(tl, tr,row,col, bl, br)
            return True
        elif (ag[tl[0]][tl[1]]=="S" and ag[tr[0]][tr[1]]=="S" and ag[bl[0]][bl[1]]=="M" and ag[br[0]][br[1]]=="M"):
            print(tl, tr,  row,col, bl, br)
            return True
        elif (ag[tl[0]][tl[1]]=="M" and ag[tr[0]][tr[1]]=="M" and ag[bl[0]][bl[1]]=="S" and ag[br[0]][br[1]]=="S"):
            print(tl, tr,  row,col, bl, br)
            return True
        elif (ag[tl[0]][tl[1]]=="S" and ag[tr[0]][tr[1]]=="M" and ag[bl[0]][bl[1]]=="S" and ag[br[0]][br[1]]=="M"):
            print(tl, tr,  row,col, bl, br)
            return True
        else:
            return False

def checkForCenterCross(arraygrid, row, col):
    height = len(arraygrid)
    width = len(arraygrid[0])
    if arraygrid[row][col] == "A":
        print('A')
        if checkCross(arraygrid, row, col, height, width):
            return 1
    return 0

def findCrosses(arraygrid):
    count = 0
    for row in range(len(arraygrid)):
        for col in range(len(arraygrid[0])):
            count+=checkForCenterCross(arraygrid,row,col)
    return count


def creategrid(df):
    arraygrid = []
    rows, cols = df.shape
    for row in range(rows):
        arraygrid.append(df.iloc[row].values.flatten().tolist())
    return arraygrid


def part_two(input):
    total = 0
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
        total += findCrosses(arraygrid)
    print(total)
    return total




part_two(None)