#Problem: Consider the sequence: s1 = 1   + 1/2                     = 3/2
#                                s2 = 1   + 1/(2+1/2)               = 7/5
#                                s3 = 1   + 1/(2+1/(2+1/2))         = 17/12
#                                s4 = 1   + 1/(2+1/(2+1/(2+1/2)))   = 41/29
#
#           Sometimes, as is the case with s8 = 1393/985, the numerator has more digits in its decimal
#           representation than the denominator. How many terms in the sequence have this property?
#           (One other thing, lim x->inf (sx) = sqrt(2) -- this is neat)    
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

def testFractionLengths(frac):
    #sees if a fraction has more digits in its numerator than its denominator
    return len(str(frac[0])) > len(str(frac[1]))

def nextExpansionMinusOne(frac):
    #Gets the next term in the sequence, but minus 1
    return reduceFraction(flipFraction(addIntegerToFraction(frac,2)))    

def main():
    #The Strategy: Firstly, we represent all nubmers as fractions because it makes the calculations simpler
    #Then, we simply generate all terms in the sequence one at a time, and count each one that more digits
    #in its numerator than its denominator.

    #Executes in 0.306 seconds
    t0 = time()
    ssum = 0
    cap = 1000
    val = [1,2]
    for i in range(2,cap+1):
        val = nextExpansionMinusOne(val)
        ssum += testFractionLengths(addIntegerToFraction(val,1))
    print("Time Elapsed:", time()-t0)
    print(ssum)
    
main()