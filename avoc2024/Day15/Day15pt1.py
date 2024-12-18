import copy


def part_one(input, moveInput):
    if input is None:
        input = 'resources/input.txt'
    robot = (0, 0)
    width = 0
    height = 0
    grid = []
    walls = []
    with open(input, 'r') as file:
        lines = file.readlines()
        for line in range(len(lines)):
            row = []
            for char in range(len(lines[line].strip("\n"))):
                if lines[line][char] == "@":
                    robot = (line,char)
                if lines[line][char] == "#":
                    walls.append((line,char))
                row.append(lines[line][char])
            grid.append(row)


    with open(moveInput, 'r') as file:
        lines = file.readlines()
        for line in lines:
            for d in line.strip("\n"):
                move = moves.get(d)
                toBeMovedLeft = []
                toBeMovedRight =[]
                nextMoves = [tuple(map(sum,zip(move,robot)))]

                i=0
                while len(nextMoves)>0:
                    #loop next moves in here
                    nextGrid = []
                    for node in nextGrid:
                        nextMove = tuple(map(sum,zip(node,move)))
                        if grid[nextMove[0]][nextMove[1]] == ']':
                            nsq = tuple(map(sum,zip(nextMove,move)))
                            nextGrid.append(nsq)
                            nextGrid.append(tuple(map(sum,zip(nsq,moves.get("<")))))
                            toBeMovedRight.append(nsq)
                            toBeMovedLeft.append(tuple(map(sum,zip(nsq,moves.get("<")))))
                        elif grid[nextMove[0]][nextMove[1]] == '[':
                            nsq = tuple(map(sum,zip(nextMove,move)))
                            nextGrid.append(nsq)
                            nextGrid.append(tuple(map(sum, zip(nsq, moves.get(">")))))
                            toBeMovedLeft.append(nsq)
                            toBeMovedRight.append(tuple(map(sum,zip(nsq,moves.get(">")))))
                        i+=2
                    nextMoves = nextGrid
                print("set:"+str(toBeMovedLeft))
                # newGrid = copy.deepcopy(grid)
                # for i in range(len(newGrid)):
                #     for j in range(len(newGrid[0])):
                #         newGrid[i][j] = "."

                # grid = newGrid
                # print(newGrid)
                for w in walls:
                    grid[w[0]][w[1]] = "#"
                for bx in list(set(toBeMovedLeft)):
                    grid[bx[0]][bx[1]] = "["
                print("left")
                for row in grid:
                    print(row)
                for bx in list(set(toBeMovedRight)):
                    grid[bx[0]][bx[1]] = "]"

                grid[robot[0]][robot[1]] = "."
                robot = tuple(map(sum,zip(move,robot)))
                grid[robot[0]][robot[1]] = "@"
                for row in grid:
                    print(row)






moves = {
    "^" : (-1,0),
    ">" : (0,1),
    "<" : (0,-1),
    "v" : (1,0)
}