#Problem:   A prime is cyclic if every number formed by ccling its digits is also prime: so 197 is a cyclic prime becasue 197, 971, and 719 are all prime
#           but 23 is not a cyclic prime because while 23 is prime, 32 is not prime. How many cyclic primes are there under 1000000 (one million)?
#           By the way, 2,3,5,7 are all cyclic primes.

import math
from time import time

def digitsToInt(intList):
    #converts a list of digits to integers: d([4,6,1,3]) = 4613
    strnum = ""
    for i in intList:
        strnum += str(i)
    return int(strnum)

def sieveOfEratosthenes(x):
    #Produces a list of numbers under x, also tells if they are prime.
    #this is to create an O(1) prime checker for primes under x 
    ar = []
    for i in range(-1,x):
        ar.append([i+1,0])
    ar[0][1] = 1
    ar[1][1] = 1
    for i in range(2,len(ar)):
        if not(ar[i][1]):
            for k in range(1,int(x/i)):
                tk = i*(k+1)
                ar[tk][1] = 1
    return ar

def isPrime(x, soe):
    #checks if a number is prime
    if soe[x][1] == 0:
        return 1
    else:
        return 0
def addLists(listlist):
    #combines a list of lists into one list with all the elements
    #for a([[3,4,5],[1,6],[],[0,0]]), the result is [3,4,5,1,6,0,0]
    retlist = []
    for i in range(0,len(listlist)):
        for k in range(0,len(listlist[i])):
            retlist.append(listlist[i][k])
    return retlist

def getNumberMultisets(amt, numList):
    #recursively produces a list of <amt> integers taken from numList. So, g(2,[1,2,4]) = [[1,1],[1,2],[1,4],[2,1],[2,2],[2,4],[4,1],[4,2],[4,4]]
    #(not necessarily in this order)
    startSet = [[]]
    endSet = []
    ctr = 0
    while ctr < amt:
        for i in range(0,len(startSet)):
            for k in numList:
                tmpset = list(startSet[i])
                tmpset.append(k)
                endSet.append(tmpset)

        startSet = list(endSet)
        endSet = []
        ctr += 1      
    return startSet

def getCycles(intList):
    #produces all cycles of a list of digits. So g([1,8,4]) = [[1,8,4],[8,4,1],[4,1,8]], again maybe not in that order
    cycleList = []
    for i in range(0,len(intList)):
        tmpList = []
        for k in range(-i,len(intList)-i):
            tmpList.append(intList[k])      
        cycleList.append(tmpList)

    return cycleList

def checkPrimeCycles(intList, soe):
    #checks if a number represented by a list of digits is a cyclical prime.
    #so c([7,1], sieve) = 1 because (71 and 17 are both prime)
    #but c([2,3], sieve) = 0
    cycles = getCycles(intList)
    good = 1
    for i in cycles:
        cnum = digitsToInt(i)
        if not(isPrime(cnum, soe)):
            good = 0

    return good

def main():
    #The strategy: we generate all possible cyclical primes under 1 million that are constituted entirely of 1,3,7,9 as their digits (one of the cycles
    #will end with each digit). Then we check all of those possible primes and see if they are actually cyclical primes. Execution time is a bit annoying:
    #4.89 seconds
    t0 = time()
    cap = 1000000

    numMsets = []
    for i in range(2,len(str(cap))):
        nlist = getNumberMultisets(i, [1,3,7,9])
        numMsets.append(nlist)

    primePossibilities = addLists(numMsets)
    primeList = sieveOfEratosthenes(cap)
    cyclicPrimeCount = 4

    for i in primePossibilities:
        if checkPrimeCycles(i,primeList):
            cyclicPrimeCount += 1
    
    print("Time Elapsed", time()-t0)
    print(cyclicPrimeCount)
main()