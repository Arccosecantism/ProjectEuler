import math
from time import time

def gcf(x,y):
    #Euclid's method for finding greatest common factor
    a = max(x,y)
    b = x+y-a
    r = 2
    while r:
        r=a%b
        a=b
        b=r
    return a

def flipFraction(frac):
    #flips a fraction: f(x) = 1/x
    return [frac[1], frac[0]]

def addIntegerToFraction(frac, xnt):
    #Adds a whole number to a fraction
    return [frac[0]+xnt*frac[1],frac[1]]

def reduceFraction(fpair):
    #reduces a fraction
    fac = gcf(fpair[0],fpair[1])
    return [int(fpair[0]/fac), int(fpair[1]/fac)]

def getNextFraction(frac, adder):
    nfrac = reduceFraction(addIntegerToFraction(flipFraction(frac),adder))
    return nfrac


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

def getNthConvergentSqrt(n, alist):
    
    sp = len(alist)-n
    startFrac = [alist[-sp],1]
    for i in range(sp+1,len(alist)+1):
        startFrac = getNextFraction(startFrac, alist[-i])
    return startFrac
 

def main():
    cl = getContinuedFractionOfSqrt(2)
    print(cl, getNthConvergentSqrt(1, cl)) 
main()

