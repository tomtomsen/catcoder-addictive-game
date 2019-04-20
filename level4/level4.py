import sys
import math
import array as arr

COLOR_NONE = 0

# ------------------------------
def calcRow( pos, maxCols ):
    return math.ceil(pos / maxCols)

# ------------------------------
def calcCol( pos, maxCols ):
    mod = pos % maxCols
    if (mod == 0):
        return maxCols

    return pos % maxCols

# ------------------------------
#   -1
#    ^
#  1 2 3 4
#    ^
#  5 6 7 8
#
def goNorth( pos, maxCols ):
    if (1 == calcRow(pos, maxCols)):
        return -1

    return pos - maxCols

# ------------------------------
def goEast( pos, maxCols ):
    if (maxCols == calcCol(pos, maxCols)):
        return -1

    return pos + 1

# ------------------------------
def goSouth( pos, maxCols, maxRows ):
    if (maxRows == calcRow(pos, maxCols)):
        return -1

    return pos + maxCols

# ------------------------------
def goWest( pos, maxCols ):
    if (1 == calcCol(pos, maxCols)):
        return -1

    return pos - 1

# ------------------------------
def step(direction, pos, maxCols, maxRows):
    if ("S" == direction):
        return goSouth(pos, maxCols, maxRows)

    if ("N" == direction):
        return goNorth(pos, maxCols)

    if ("E" == direction):
        return goEast(pos, maxCols)

    if ("W" == direction):
        return goWest(pos, maxCols)

# ------------------------------
def isOutOfBounds( pos, maxCols, maxRows ) :
    return pos > maxCols * maxRows or pos < 1;

# ------------------------------
def manhattanDinstance(p1, p2, maxCols):
    r1 = calcRow(p1, maxCols)
    c1 = calcCol(p1, maxCols)
    r2 = calcRow(p2, maxCols)
    c2 = calcCol(p2, maxCols)

    return abs(r1 - r2) + abs(c1 - c2)

# -------------------------------
def initGrid(maxCols, maxRows):
    grid = []
    grid.append(0)

    for x in range(0, maxCols * maxRows):
        grid.append(COLOR_NONE)

    return grid

# -------------------------------
#
# steps: [S, W, E, E]
#
def getValidPath(pathDefinition, grid):

    color = pathDefinition[0]
    startPosArg = pathDefinition[1]
    pathLenArg = pathDefinition[2]

    path = []
    for y in range(0, pathLenArg):
        direction = args[argIdx]
        argIdx += 1

        path.append(startPosArg)
        newPosition = step(direction, startPosArg, colArg, rowArg)
        
        if (newPosition == -1): # out of bounds
            return []

        if (newPosition in path): # crosses itself
            return []

        if (y == pathLenArg-1): # letzter schritt
            if (grid[newPosition] != colorArg):
                return []
        else:
            # andere farbe
            if (grid[newPosition] != colorArg and grid[newPosition] != COLOR_NONE):
                return []
                
        # grid[newPosition] = colorArg

        startPosArg = newPosition

    return path

# ------------------------------
def addPathToGrid(grid, validPath, color):
    return grid

# -------------------------------
def draw(grid, outputFile):
    return 1

# ------------------------------

def main(args, outputFile):
    argIdx = 0
    rowArg = int(args[argIdx])
    argIdx += 1
    colArg = int(args[argIdx])
    argIdx += 1

    grid = initGrid(colArg, rowArg)

    posCountArg = int(args[argIdx])
    argIdx += 1

    for x in range(0, posCountArg):
        posArg = int(args[argIdx])
        argIdx += 1

        colorArg = int(args[argIdx])
        argIdx += 1

        grid[posArg] = colorArg

    pathCountArg = int(args[argIdx])
    argIdx += 1

    for x in range(0, pathCountArg): # path arguments
        colorArg = int(args[argIdx])
        argIdx += 1

        startPosArg = int(args[argIdx])
        argIdx += 1

        pathLenArg = int(args[argIdx])
        argIdx += 1

        pathDefinition = [colorArg, startPosArg, pathLenArg]
        for y in range(0, pathLenArg):
            stepArg = args[argIdx]
            argIdx += 1

            pathDefinition.append(stepArg)
        
        validPath = getValidPath(pathDefinition, grid)
        grid = addPathToGrid(grid, validPath, colorArg)

    draw(grid, outputFile)