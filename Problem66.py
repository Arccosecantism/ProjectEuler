import math
from time import time


def isSquare(x):
    prec = .000001
    rtx = math.sqrt(x)
    if abs(rtx-int(rtx)) < prec:
        return True
    return False
def getContinuedFractionOfSqrt(x):
    sqx = math.sqrt(x)
    ipart = int(sqx)
    
    rem = ipart
    cycle = []
    intEl =int((sqx+rem)/(x-rem*rem))
    cycle.append(intEl)
    
    firstDenom = x-rem*rem
    firstRem = -rem+intEl*firstDenom

    denom = firstDenom
    rem = firstRem

    done = False
    while not(done):
        denom = (x-rem*rem)/denom
        intEl = int((sqx+rem)/(denom))
        rem = -rem+intEl*denom
        if rem == firstRem and denom == firstDenom:
            done = True
        else:
            cycle.append(intEl)
    return [ipart] + cycle

def testPellSolution(x,d,y):
    return x*x-d*y*y == 1

def findPellSolution(n):
    alist = getContinuedFractionOfSqrt(n)
    convergents = []
    
    pnum = alist[0]
    num = alist[1]*alist[0]+1

    pden = 1
    den = alist[1]
    
    if testPellSolution(pnum, n, pden):
        return [pnum,pden, n]
    elif testPellSolution(num, n, den):
        return [num,den, n]

    ctr = 1
    gs = len(alist)-1
    sol = []
    done = False
    while not(done):
        na = 1+ctr%gs
        nnum = alist[na]*num+pnum
        pnum = num
        nden = alist[na]*den+pden
        pden = den
        den = nden
        num = nnum
        if testPellSolution(num,n,den):
            done = True
            sol = [num,den, n]
        ctr += 1
    return sol
 

def main():
    largest = [0,0]
    for i in range(2,1001):
        if not(isSquare(i)):
            minx = findPellSolution(i)[0]
            if minx > largest[1]:
                largest = [i,minx]
    print(largest[0])
main()

