def isAllIncreasing(parts):
    for i in range(len(parts)-1):
        if parts[i] < parts[i+1]:
            continue
        else:
            return False
    return True

def isAllDecreasing(parts):
    for i in range(len(parts)-1):
        if parts[i] > parts[i+1]:
            continue
        else:
            return False
    return True

def isAtleaseOne(parts):
    for i in range(len(parts)-1):
        if abs(parts[i] - parts[i+1])>0:
            continue
        else:
            return False
    return True

def isMaxThree(parts):
    for i in range(len(parts)-1):
        if abs(parts[i] - parts[i+1])<4:
            continue
        else:
            return False
    return True

def meetsCriteria(parts):
    if (isAllDecreasing(parts) or isAllIncreasing(parts)) and (isMaxThree(parts) and isAtleaseOne(parts)):
        return True
    else:
        original = parts.copy()
        for i in range(len(original)):
            parts = original.copy()
            parts.pop(i)
            if not meetsCriteria2(parts):
                continue
            else:
                return True
        return False

def meetsCriteria2(parts):
    if (isAllDecreasing(parts) or isAllIncreasing(parts)) and (isMaxThree(parts) and isAtleaseOne(parts)):
        return True
    else:
        return False

def part_one(input):
    total = 0
    if input is None:
        input = 'resources/input.txt'
    with open(input, 'r') as file:
        lines = file.readlines()
        for line in lines:
            parts = line.split(' ')
            int_parts = []
            for i in parts:
                int_parts.append(int(i))
            if meetsCriteria(int_parts):
                total+=1
        print(total)
        return total

def part_two(input):
    total = 0
    if input is None:
        input = 'resources/input.txt'
    with open(input, 'r') as file:
        lines = file.readlines()
        for line in lines:
            parts = line.split(' ')
            int_parts = []
            for i in parts:
                int_parts.append(int(i))
            if meetsCriteria(int_parts):
                total += 1
        print(total)
        return total

# part_one(None)
part_two(None)
