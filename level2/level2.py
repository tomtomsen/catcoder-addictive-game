import math

# ------------------------------
def calcRow( pos, cols ):
    return math.ceil(pos / cols)

# ------------------------------
def calcCol( pos, cols ):
    mod = pos % cols
    if (mod == 0):
        return cols
    return pos % cols

# ------------------------------
def manhattanDinstance(p1, p2, cols):
    r1 = calcRow(p1, cols)
    c1 = calcCol(p1, cols)
    r2 = calcRow(p2, cols)
    c2 = calcCol(p2, cols)

    return abs(r1 - r2) + abs(c1 - c2)

# ------------------------------
def main(args):

    rowArg = int(args[0])
    colArg = int(args[1])
    numOfPointsArg = int(args[2])

    str = ""
    for currentColor in range(1, int(numOfPointsArg/2)+1):
        pos1 = 0
        for argIdx in range(0, numOfPointsArg):
            posArg = int(args[3+argIdx*2])
            colorArg = int(args[4+argIdx*2])

            if (colorArg == currentColor):
                if (pos1 == 0):
                    pos1 = posArg
                else:
                    if str != "":
                        str = str + " "

                    str = str + "%d" % (manhattanDinstance(pos1, posArg, colArg))
                    break

    return str
