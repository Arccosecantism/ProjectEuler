#Problem: Consider all fractions (not necessarily simplified) less than 1 that have numerators and denominators that are 2 digits long.
#          There are exactly four that can be reduced an incorrect, childish way; by cancelling digits instead of factors. For example:
#           one such fraction is 49/98. By cancelling the 9s, we see that 49/98=4/8. When all four of these fractions are multiplied
#           together and fully simplified, what is the value of the denominator? 

import math
from time import time

def gcf(a,b):
    #recursive greatest common factor; used for reducing fractions
    fa = max(a,b)
    fb = min(a,b)
    mod = fa%fb
    if mod == 0:
        return fb
    else:
        return gcf(fb, mod)

def findVals(x,z):
    #about 10 minutes of algebra reveals this about fractions that can be simplified by cancelling digits;
    #If (10x+y)/(10y+z)=x/z, then y = 9xz/(10x-z). This ifunction returns y
    fx = float(x)
    fz = float(z)
    return float(9*fx*fz/(10*fx-fz))

def main():
    #Strategy: (see the findVals function for the major simplification) We look at all pairs of integers 
    #x and z from 1-9 to find what y must be (in the fraction (10x+y)/(10y+z)) according to the findVals function
    #The fractions that work have integer y values and have x > z and have x,y,z all in [1,10]
    #We keep track of the numerators and denominators, multiply the numerators together, and the denominators together
    #to find the unsimplified fraction product. Then we simplify by dividing the numerator and denominator
    #by the gcf of the numerator and denominator. Executes in 1.00 millisecond
    t0 = time()  
    print(gcf(77,121))
    numers = []
    denoms = []
    for i in range(1,9):
        for k in range(i+1,10):
            fv = findVals(i,k)
            if fv == int(fv) and fv > 0 and fv < 10:
                numers.append(i)
                denoms.append(k)
    fnum = 1
    fden = 1
    for i in range(0,len(numers)):
        fnum *= numers[i]
        fden *= denoms[i]
    
    fac = gcf(fnum,fden)
    fnum /= fac
    fden /= fac
    print("Time Elapsed:", time()-t0)
    print(fden)
main()