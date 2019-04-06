import sys
import math
import glob
import os

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

def main ( args ):
    rowArg = int(args[0])
    colArg = int(args[1])
    posCount = int(args[2])

    str = ""
    for argIdx in range(0, posCount):
        posArg = int(args[argIdx + 3])
        str = str + " " + ("%d %d" % (calcRow( posArg, colArg ), calcCol( posArg, colArg)))

    return str