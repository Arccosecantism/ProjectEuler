#Problem: Here begins continued fractions: https://projecteuler.net/problem=64 -- How many non-square integers from 1 to 10000 have squareroots that
#have an odd period of repitition in their continued fractions?

import math
from time import time

def isSquare(x):
    #tells if a number is square
    sqx = math.sqrt(x)
    if int(sqx) == sqx:
        return True
    return False
def getContinuedFractionOfSqrt(x):
    #finds the continued fraction of sqrt(x) by finding the closest approimation each time, sort of
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
    #The strategy: Once we have built the function which gives the continued fraction of the sqrt(x), we simply call the function on every integer
    #from 1 to 10000, see if the period of repitition of the continued fraction of the squareroot is odd, and count them
    #Executes in .71 seconds
    t0 = time()
    count = 0
    for i in range(1,10001):
        if not(isSquare(i)):
            cfl = getContinuedFractionOfSqrt(i)
            cs = len(cfl[1])
            
            if cs%2:
                count += 1
    print("Time Elapsed:", time()-t0)
    print(count)

main()
         
    
    
    
