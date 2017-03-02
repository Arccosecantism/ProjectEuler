#Problem: consider the Diophantine equation x^2-Dy^2=1. for any non-square value of D, we can find the minimum x value that has a y value that makes the
#          equation true. So for D=3: 2^2-3*1^2 = 1 and for D=6: 5^2-6*2^2 = 1.
#          Find the value of D<=1000 that has the largest corresponding minimum x value solution.

#          Note: this Diophantine equation is Pell's equation, and shall be referred to as such
import math
from time import time


def isSquare(x):
    #tells if a number is square
    sqx = math.sqrt(x)
    if int(sqx) == sqx:
        return True
    return False

def getContinuedFractionOfSqrt(x):
    #gets the continued fraction coefficients of sqrt(x)
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
    #tests if a possible solution to Pell's equation is an actual solution
    return x*x-d*y*y == 1

def findPellSolution(n):
    #finds the minimum solution to Pell's equation where D = n. After doing some research (which I am having to do more and more), I found
    #out that this is actually closely related to the convergents of continued fractions, which sort of makes sense, because the convergents
    #are the best rational approximations of an irrational number, and that sort of fits in with Pell's equation.
    #Anyway, the way to solve this is by creating convergents, and letting tx = p and ty = q where p is the numerator and q is the denominator.
    #Then, we test if tx^2+D*ty^2=1. And the magical thing is that the first one that works is the smallest solution to Pell's equation
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

    #The strategy: Go through every non-square value J from 2 to 1000 and find the minimal x-value for the Pell equation with D=J
    #Record the largest.
    #Executes in .065 seconds
    t0 = time()
    largest = [0,0]
    for i in range(2,1001):
        if not(isSquare(i)):
            minx = findPellSolution(i)[0]
            if minx > largest[1]:
                largest = [i,minx]
    print("Time Elapsed:", time()-t0)
    print(largest[0])
main()

