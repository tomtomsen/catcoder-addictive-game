import glob
import os
from level1 import main

if __name__ == '__main__':
    for fileInPath in glob.glob('data/in/*.in'):
        fileIn = open(fileInPath, "r")
        fileInBasename = os.path.basename(fileInPath);
        fileOut = open("data/out/" + fileInBasename + ".out", "w")

        fileInContent = fileIn.read()
        args = fileInContent.split(" ")

        print("Processing", fileInBasename + ": ", end="")
        out = main(args)
        fileOut.write("%s" % out)
        print("done")
        