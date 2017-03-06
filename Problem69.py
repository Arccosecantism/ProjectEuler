#Problem: consider the totient function phi: N->N where phi(x) is the number of natural numbers under x that are relatively prime to x.
#           for n<=1,000,000, which n produces the largest n/phi(n)?

import math
from time import time


def primeFactorSieve(x):
    #Produces a list of numbers under x and the unique primes in each of those number's prime factorization
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




def altTotient(x, pfs):
    #finds x/totient(x) by being clever (aka, researching):
    #totient of x can be found by multiplying all (1-1/j) where j is a prime dividing x and then by mulitplying by x
    primes = pfs[x]
    totala = 1
    totalb = 1
    for i in primes:
        #print(1.0/i)
        totala *= (i-1)
        totalb *= i
    return (totalb*1.0)/totala

def main():
    #The strategy: now that we have a quick way to generate totients, the problem is easy: simply generate all
    t0 = time()
    sieve = primeFactorSieve(1000002)
    altTots = []
    largest = 0
    largestVal = 0
    for i in range(1,1000000):
        atot = altTotient(i,sieve)
        if atot > largest:
            largest = atot
            largestVal = i
    print("Time Elapsed:", time()-t0)
    print(largest,largestVal)

main()