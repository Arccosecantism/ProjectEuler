
import math
from time import time

def isSquare(x):
    sqx = math.sqrt(x)
    if int(sqx) == sqx:
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
    return [ipart, cycle]

def main():
    t0 = time()
    count = 0
    mmax = 0
    for i in range(1,10001):
        if not(isSquare(i)):
            cfl = getContinuedFractionOfSqrt(i)
            cs = len(cfl[1])
            if cs>mmax:
                mmax = cs
                print(i,cs, cfl[1])
            
            if cs%2:
                count += 1
    print("Time Elapsed:", time()-t0)
    print(count)

main()
         
    
    
    
