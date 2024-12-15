import re

from sympy.printing.dot import default_styles


def part_one(input):
    if input is None:
        input = 'resources/input.txt'
    with open(input, 'r') as file:
        lines = file.readlines()
        ax = []
        ay = []
        bx = []
        by = []
        px = []
        py = []
        total = 0
        for line in lines:
            if re.search("Button A:",line) is not None:
                h = line.split(",")
                ax.append(int(h[0].split("X+")[1]))
                ay.append(int(h[1].split("Y+")[1]))
            elif re.search("Button B:",line) is not None:
                h = line.split(",")
                bx.append(int(h[0].split("X+")[1]))
                by.append(int(h[1].split("Y+")[1]))
            elif re.search("Prize:",line) is not None:
                h = line.split(",")
                px.append(int(h[0].split("X=")[1]))
                py.append(int(h[1].split("Y=")[1]))

        for i in range(len(ax)):
            x1 = ax[i]
            y1 = ay[i]
            x2 = bx[i]
            y2 = by[i]
            xp = px[i]
            yp = py[i]
            #Calulate x factors
            x1Factors = []
            x2Factors = []
            f = 1
            tx1 = x1
            tx2 = x2
            while tx1 < xp or tx2 < xp:
                tx1 = f*x1
                tx2 = f*x2
                x1Factors.append(tx1)
                x2Factors.append(tx2)
                f+=1
            validFactors = []
            for factor in x1Factors:
                for factor2 in x2Factors:
                    if factor + factor2 == xp:
                        aFactor = factor//x1
                        bFactor = factor2//x2
                        validFactors.append((aFactor,bFactor))
            prizeWinners = []
            currTotalCost = None
            for factors in validFactors:
                if int((factors[0]*y1) + (factors[1]*y2)) == yp:
                    prizeWinners.append(factors)
            for prize in prizeWinners:
                cost = (prize[0] * 3) + prize[1]
                if currTotalCost is None:
                    currTotalCost = cost
                elif currTotalCost > cost:
                    currTotalCost = cost
            if currTotalCost is not None:
                total += currTotalCost
    print("answer:" + str(total))
    return total

# part_one(None)

def part_two(input):
    #Cramers rule
    if input is None:
        input = 'resources/input.txt'
    with open(input, 'r') as file:
        lines = file.readlines()
        ax = []
        ay = []
        bx = []
        by = []
        px = []
        py = []
        total = 0
        for line in lines:
            if re.search("Button A:",line) is not None:
                h = line.split(",")
                ax.append(int(h[0].split("X+")[1]))
                ay.append(int(h[1].split("Y+")[1]))
            elif re.search("Button B:",line) is not None:
                h = line.split(",")
                bx.append(int(h[0].split("X+")[1]))
                by.append(int(h[1].split("Y+")[1]))
            elif re.search("Prize:",line) is not None:
                h = line.split(",")
                px.append(int(h[0].split("X=")[1])+10000000000000)
                py.append(int(h[1].split("Y=")[1])+10000000000000)

        for i in range(len(ax)):
            det = (ax[i]*by[i])-(ay[i]*bx[i])
            deta = (px[i]*by[i])-(py[i]*bx[i])
            detb = (px[i]*ay[i])-(py[i]*ax[i])
            a = int(abs(deta/det))
            b = int(abs(detb/det))
            if ((ax[i]*a) + (bx[i]*b))==px[i] and ((ay[i]*a) + (by[i]*b))==py[i]:
                total+= (3 * a)+b
    print(total)
    return total

# part_two(None)