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

def sumNumeratorDigits(frac):
    numer = frac[0]
    ssum = 0
    while numer >= 1:
        ssum += numer%10
        numer = int(numer/10)
    return ssum

def main():

    e_list = []
    maxVal = 100
    for i in range(2,1+maxVal):
        if i%3:
            e_list.append(1)
        else:
            e_list.append(2*i/3)
    startFrac = [e_list[-1],1]
    for i in range(2,len(e_list)+1):
        startFrac = getNextFraction(startFrac, e_list[-i])
    startFrac = getNextFraction(startFrac, 2)
    numeratorSum = int(sumNumeratorDigits(startFrac))
    print(numeratorSum)

main()