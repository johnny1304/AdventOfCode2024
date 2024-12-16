import copy


def part_one(input, moveInput):
    if input is None:
        input = 'resources/input.txt'
    robot = (0, 0)
    width = 0
    height = 0
    walls = []
    boxes = []
    with open(input, 'r') as file:
        lines = file.readlines()
        for line in range(len(lines)):
            height = len(lines)
            for char in range(len(lines[line])):
                width = len(lines[line])
                if char == "@":
                    robot = (line,char)
                if char == "#":
                    walls.append((line,char))
                if char == "O":
                    boxes.append((line,char))

    with open(moveInput, 'r') as file:
        lines = file.readlines()
        for line in lines:
            for char in line.strip('\n'):
                if char == ('^'):
                    nextMove = (robot[0]-1,robot[1])
                    if nextMove in walls:
                        print("wall")
                    elif nextMove in boxes:
                        print("box")
                        currBoxes=[]
                        pos = copy.deepcopy(nextMove)
                        while pos in boxes:
                            currBoxes.append(pos)
                            pos = (pos[0]-1,pos[1])
                        if pos not in walls:
                            for box in currBoxes:
                                index =boxes.index(box)
                                boxes[index] = (box[0]-1,box[1])
                            robot = nextMove
                    else:
                        print("move")
                        robot = nextMove

                elif char == ('v'):
                    nextMove = (robot[0]+1,robot[1])
                    if nextMove in walls:
                        print("wall")
                    elif nextMove in boxes:
                        print("box")
                        currBoxes=[]
                        pos = copy.deepcopy(nextMove)
                        while pos in boxes:
                            currBoxes.append(pos)
                            pos = (pos[0]+1,pos[1])
                        if pos not in walls:
                            for box in currBoxes:
                                index =boxes.index(box)
                                boxes[index] = (box[0]+1,box[1])
                            robot = nextMove
                    else:
                        print("move")
                        robot = nextMove
                elif char == ('>'):
                    nextMove = (robot[0],robot[1]+1)
                    if nextMove in walls:
                        print("wall")
                    elif nextMove in boxes:
                        print("box")
                        currBoxes=[]
                        pos = copy.deepcopy(nextMove)
                        while pos in boxes:
                            currBoxes.append(pos)
                            pos = (pos[0],pos[1]+1)
                        if pos not in walls:
                            for box in currBoxes:
                                index =boxes.index(box)
                                boxes[index] = (box[0],box[1]+1)
                            robot = nextMove
                    else:
                        print("move")
                        robot = nextMove
                elif char == ('<'):
                    nextMove = (robot[0],robot[1]-1)
                    if nextMove in walls:
                        print("wall")
                    elif nextMove in boxes:
                        print("box")
                        currBoxes=[]
                        pos = copy.deepcopy(nextMove)
                        while pos in boxes:
                            currBoxes.append(pos)
                            pos = (pos[0],pos[1]-1)
                        if pos not in walls:
                            for box in currBoxes:
                                index =boxes.index(box)
                                boxes[index] = (box[0],box[1]-1)
                            robot = nextMove
                    else:
                        print("move")
                        robot = nextMove