import copy
from pdb import line_prefix


def calculateNextOperand(operands):
    zeroIndexes = []
    for i in range(len(operands)):
        if operands[i] == '*':
            zeroIndexes.append(i)
        else:
            operands[i] = "*"
            for operand in zeroIndexes:
                operands[operand] = "+"
            break




def calculateValidEquations(answer, equationInputs):
    operands = ["+" for _ in range(len(equationInputs)-1)]
    first = True
    while "+" in operands:
        if not first:
            calculateNextOperand(operands)
        calculation = [int(equationInputs[0])]
        for i in range(len(operands)):
            calculation.append(operands[i])
            calculation.append(int(equationInputs[i+1]))
        if calculateEquationFromString(calculation) == int(answer):
            print("::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::")
            return calculateEquationFromString(calculation), True
        first = False
    return 0, False


def calculateEquationFromString(calculation):
    calc = copy.deepcopy(calculation)
    while "+" in calc or "*" in calc or "||" in calc:
        for i in range(len(calc)):
            if calc[i] == "+":
                calc[i] = calc[i - 1] + calc[i + 1]
                del calc[i - 1]
                del calc[i]
                break
            elif calc[i] == "*":
                calc[i] = calc[i - 1] * calc[i + 1]
                del calc[i - 1]
                del calc[i]
                break
            elif calc[i] == "||":
                calc[i] =int( str(calc[i - 1]) + str(calc[i + 1]))
                del calc[i - 1]
                del calc[i]
                break
    return calc[0]


def part_one(input):
    total = 0
    if input is None:
        input = 'resources/input.txt'
    with open(input, 'r') as file:
        lines = file.readlines()
        for line in lines:
            lineParse = line.strip("\n").split(": ")
            answer = lineParse[0]
            equation = lineParse[1]
            equationInputs = equation.split(" ")
            calculatedResult, safe = calculateValidEquations(answer, equationInputs)
            if safe:
                total+=calculatedResult
    print(total)
    return total


def calculateNextPipeOperator(operands):
    zeroIndexes = []
    for i in range(len(operands)):
        if operands[i] == '*':
            zeroIndexes.append(i)
        else:
            if operands[i] == "||":
                operands[i] = "*"
            else:
                operands[i] = "||"
            for operand in zeroIndexes:
                operands[operand] = "+"
            break


def calculateValidEquationsWithPipeOperand(answer, equationInputs):
    operands = ["+" for _ in range(len(equationInputs) - 1)]
    first = True
    while "+" in operands or "||" in operands:
        if not first:
            calculateNextPipeOperator(operands)
        calculation = [int(equationInputs[0])]
        for i in range(len(operands)):
            calculation.append(operands[i])
            calculation.append(int(equationInputs[i + 1]))
        if calculateEquationFromString(calculation) == int(answer):
            print("::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::")
            return calculateEquationFromString(calculation)
        first = False
    return 0


def part_two(input):
    total = 0
    if input is None:
        input = 'resources/input.txt'
    with open(input, 'r') as file:
        lines = file.readlines()
        for line in lines:
            lineParse = line.strip("\n").split(": ")
            answer = lineParse[0]
            equation = lineParse[1]
            equationInputs = equation.split(" ")
            total += calculateValidEquationsWithPipeOperand(answer, equationInputs)
    print(total)
    return total

def part_one(input):
    total = 0
    if input is None:
        input = 'resources/input.txt'
    with open(input, 'r') as file:
        lines = file.readlines()
        inputlines = [[] for _ in range(len(lines))]
        row = 0
        for line in lines:
            col = 0
            lineParse = line.strip("\n").split(": ")
            answer = lineParse[0]
            equation = lineParse[1]
            equationInputs = equation.split(" ")
            calculatedResult, safe = calculateValidEquations(answer, equationInputs)
            if safe:
                total+=calculatedResult
    print(total)
    return total

part_two(None)