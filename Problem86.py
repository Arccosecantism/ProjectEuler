import math
from time import time

def primeFactorSieve(x):
    #Produces a list of numbers under x, also tells if they are prime.
    ar = []
    for i in range(-1,x):
        ar.append([])
    
    ub = int(x/2)+1
    for i in range(2,ub):
        if ar[i] == []:
            for k in range(i,x,i):
                ar[k].append(i)
    for i in range(2,x+1):
        if ar[i] == []:
            ar[i] = [i]
    return ar

def generateCoprimeNumbers(x, pfs):
    #generates a list of numbers x is relatively prime with and such that, for any element j in the list,
    #x and j aren't both odd (this last part helps in generating pythag triples)
    numList = [1]*x
    if x&1:
        for i in range(0,len(numList)):
            if not(i&1):
                numList[i] = 0
    facs = pfs[x]
    
    for i in facs:
        for k in range(0,len(numList)):
            if not((k+1)%i):
                numList[k] = 0
    goodList = []
    for i in range(0,len(numList)):
        if numList[i] == 1:
            goodList.append(i+1)
    return goodList

def generatePythagTriples(cap):
    psieve = primeFactorSieve(cap+10)
    mctr = 1
    pthist = []
    for i in range(cap+1):
        pthist.append([])

    while 2*mctr<=cap:

        partners = generateCoprimeNumbers(mctr,psieve)
       # print(partners)
        for k in partners:
            av = mctr*mctr-k*k
            bv = 2*k*mctr
            smaller = min(av,bv)
            larger = max(av,bv)
            mult = 1
            while smaller*mult <= cap: 
                if larger*mult <= 2*cap:
                    pthist[smaller*mult].append(larger*mult)
                mult += 1
        mctr += 1
    return pthist
    
def countPrismsForCap(pythagHist, maxcap):

    ssum = 0
    for i in range(0,min(len(pythagHist),maxcap)):
        for k in pythagHist[i]:
            ssum += max(int(k/2) - (k-i-1),0)
            if k <= maxcap:
                ssum += int(i/2)
    
    return ssum

def binarySearchCuboidAmounts(cmin, cmax, goal, pythagHist):
    guess = int((cmin+cmax)/2)
    if guess == cmax or guess == cmin:
        return guess
    gc = countPrismsForCap(pythagHist, guess)
    #print(gc)
    if gc<goal:
        return binarySearchCuboidAmounts(guess,cmax,goal,pythagHist)
    elif gc>goal:
        return binarySearchCuboidAmounts(cmin,guess,goal,pythagHist)

def main():
    trueMax = 3000
    trueMin = 1000
    goal = 1000000
    pythagHist = generatePythagTriples(trueMax+10)
    threshold = binarySearchCuboidAmounts(trueMin, trueMax, goal, pythagHist)
    print(threshold)
main()