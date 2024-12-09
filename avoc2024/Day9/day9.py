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
            return total
        else:
            total+= i * outputBlock[i]


def calculateBlockAndCheckSum(input):
    outputBlock = []
    seq = 0
    currPos = 0
    usedPos = []
    emptyPos = []
    for i in range(len(input)):
        if i%2 == 0:
            for j in range(int(input[i])):
                outputBlock.append(seq)
                usedPos.append(currPos)
                currPos += 1
            seq+=1
        else:
            for j in range(int(input[i])):
                outputBlock.append(".")
                emptyPos.append(currPos)
                currPos += 1
    maxValue = 0
    gap, usedPos, emptyPos, max = gapsExist(outputBlock,maxValue)
    while gap:
        pos =emptyPos[0]
        outputBlock[pos] = outputBlock[usedPos[-1]]
        outputBlock[usedPos[-1]] = "."
        usedPos.pop()
        gap, usedPos, emptyPos, max = gapsExist(outputBlock,maxValue)

    return calculateCheckSum(outputBlock)



def part_one(input):
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

# part_one(None)