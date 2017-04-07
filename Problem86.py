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
    psieve = primeFactorSieve(1000000)
    mctr = 1
    ptlist = []
    while 2*mctr<cap:

        partners = generateCoprimeNumbers(mctr,psieve)
        print(partners)
        for k in partners:
            av = mctr*mctr-k*k
            bv = 2*k*mctr
            mult = 1
            while bv*mult < cap:
                if av*mult < 2*cap: 
                    ptlist.append((av*mult,bv*mult,))
                mult += 1
        mctr += 1
    return ptlist
    
def main():
    
    print(generatePythagTriples(100))

main()