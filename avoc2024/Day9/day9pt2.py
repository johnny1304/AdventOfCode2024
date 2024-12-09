def creategrid(df):
    arraygrid = []
    rows, cols = df.shape
    for row in range(rows):
        arraygrid.append(df.iloc[row].values.flatten().tolist())
    return arraygrid


def gapsExist(outputBlock,maxValue):
    usedPos = []
    emptyPos = []
    for i in range(maxValue, len(outputBlock)):
        if outputBlock[i] == ".":
            emptyPos.append(i)
        else:
            usedPos.append(i)
    for i in range(len(usedPos)-1):
        if abs(usedPos[i] - usedPos[i+1]) > 1:
            return True, usedPos, emptyPos, i
    return False, usedPos, emptyPos, len(outputBlock)


def calculateCheckSum(outputBlock):
    total = 0
    for i in range(len(outputBlock)):
        if outputBlock[i] == ".":
            continue
        else:
            total+= i * outputBlock[i]
    return total


def findGap(outputBlock, segSize, currentPos):
    currGapSize = 0
    start = 0
    for i in range(len(outputBlock)):
        if outputBlock[i] == ".":
            if currGapSize == 0:
                start = i
                currGapSize += 1
            else:
                currGapSize += 1
        else:
            start = i
            currGapSize = 0
        if currGapSize == segSize and start<currentPos:
            return start



def calculateBlockAndCheckSum(input):
    outputBlock = []
    seq = 0
    currPos = 0
    usedPos = []
    emptyPos = []
    blocks=dict()
    for i in range(len(input)):
        if i%2 == 0:
            startPos = currPos
            for j in range(int(input[i])):
                outputBlock.append(seq)
                usedPos.append(currPos)
                currPos += 1
            blocks[seq] = (startPos, currPos-1)
            seq+=1
        else:
            for j in range(int(input[i])):
                outputBlock.append(".")
                emptyPos.append(currPos)
                currPos += 1
    seq -=1
    for i in range(seq,0,-1):
        segSize = abs(blocks[i][0]-blocks[i][1])+1
        start = findGap(outputBlock,segSize,blocks[i][0])
        if start is not None:
            for j in range(segSize):
                outputBlock[j+start] = i
            for j in range(segSize):
                outputBlock[blocks[i][0] + j] = "."
    return calculateCheckSum(outputBlock)



def part_two(input):
    if input is None:
        input = 'resources/input.txt'
    with open(input, 'r') as file:
        lines = file.readlines()
        inputlines = []
        for line in range(len(lines)):
            for char in lines[line].strip("\n"):
                inputlines.append(char)
        total = calculateBlockAndCheckSum(inputlines)
    print("answer:" + str(total))
    return total

part_two(None)