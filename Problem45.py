import math
from time import time

def isTriangular(x):
    if math.sqrt(8*x+1)%2 == 1:
        return 1
    return 0

def isPentagonal(x):
    if math.sqrt(24*x+1)%6 == 5:
        return 1
    return 0

def main():
    t0 = time()
    numCtr = 1
    hexCtr = 1
    fd = 1
    sd = 4
    done = 0
    while not(done):

        if hexCtr > 40755 and isPentagonal(hexCtr):
            done = 1
        else:
            numCtr+=1
            fd += sd
            hexCtr += fd
    print("Elapsed Time:", time()-t0)
    print(hexCtr)

main()