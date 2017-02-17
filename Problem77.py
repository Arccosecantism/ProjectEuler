import math
from time import time

def sieveOfEratosthenes(x):
    #Produces a list of numbers under x, also tells if they are prime.
    #this is to create an O(1) prime checker for primes under x 
    ar = []
    flick = True
    for i in range(-1,x):
        val = 1
        if flick:
            val = 0
        ar.append(val)
        flick = not(flick)
    ar[1] = 0
    ar[2] = 1
    ub = int(math.ceil(math.sqrt(len(ar)))+1)
    for i in range(2,ub):
        if ar[i]:
            for k in range(i*i,x,i):
                ar[k] = 0
    return ar

def primeFactorSieve(x):
    #Produces a list of numbers under x, also tells if they are prime.
    #this is to create an O(1) prime checker for primes under x 
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


def getSmallPrimeSieve(soe, num):
    return soe[0:num+1]

def findNthCValue(n, pfs):

    divs = pfs[n]
    return sum(divs)
            
def getBSequence(cseq):
    bseq = [0,cseq[1]]
    for i in range(2,len(cseq)):
        ssum = 0
        for k in range(1,i-1):
            ssum+=cseq[k]*bseq[i-k]
        bv = int(1.0/i*(cseq[i]+ssum))
        bseq.append(bv)
    return bseq
def main():
    sieve = sieveOfEratosthenes(10000)
    primeFactorList = primeFactorSieve(10000)
    aSequence = getSmallPrimeSieve(sieve,20)
    print(findNthCValue(6, primeFactorList))
    
    cSequence = []
    for i in range(0,100):
        cSequence.append(findNthCValue(i,primeFactorList))
    #print(cSequence)

    bSequence = getBSequence(cSequence)

    first_fk_val = -1
    for i in range(0,len(bSequence)):
        if bSequence[i] > 5000 and first_fk_val == -1:
            first_fk_val = i
            break
    print(first_fk_val)
main()

