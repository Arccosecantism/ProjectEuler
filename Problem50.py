#Problem: Which number under one million can be represented as the longest sum of consecutive primes

import math
from time import time

def sieveOfEratosthenes(x):
    #Produces a list of numbers under x, also tells if they are prime.
    #this is to create an O(1) prime checker for primes under x 
    ar = []
    for i in range(-1,x):
        ar.append(0)
    ar[0] = 1
    ar[1] = 1
    ub = int(math.ceil(math.sqrt(len(ar)))+1)
    for i in range(2,ub):
        if not(ar[i]):
            ub2 = int(x/i)
            for k in range(i-1,ub2):
                tk = i*(k+1)
                ar[tk] = 1
    return ar

def isPrime(x, soe):
    #O(1) Prime checker
    prime = 1
    if soe[x] == 1:
        prime = 0
    return prime

def getPrimeList(soe):
    #gets all of the primes from a sieve of erastothenes
    primelist = []
    for i in range(0,len(soe)):
        if soe[i] == 0:
            primelist.append(i)
    return primelist


def main():
    #The Strategy: First, we find the maximum number of consecutive primes that, when added together, are less than
    #one million. Then we start at that many primes, and count down, removing one prime each time, all the while
    #testing all possilbe "runs." We do this until the sum of a run is prime, and then we stop. Also, because runs
    #share many numbers, when moving from one run to the next, the new number is added and the lost number is
    #subtracted -- the whole sum is not re-computed. Finally, because all non-2 primes are odd and the sum of the 
    #consecutive primes must be prime and thus odd, if the amount of primes being tested is eve, 2 must be a part of
    #the run

    #Executes in 0.98 seconds
    t0 = time()
    sieve = sieveOfEratosthenes(1000000)
    plist = getPrimeList(sieve)

    longestChain = 0
    done = 0
    pnum = 0
    stval = 0
    ctr = 0
    while stval < 1000000:
        stval += plist[ctr]
        ctr+= 1
    print(ctr)
    ctr -= 1
    
    for i in range(0,ctr):
        ti = ctr-i
        if ti%2 == 1:
            ssum = 0
            for k in range(1,ti+1):
                ssum += plist[k]
            if ssum < 1000000:
                if isPrime(ssum, sieve):
                    longestChain = ti
                    pnum = ssum
                    done = 1
                else:
                    for k in range(ti+1,len(plist)):
                        ssum += plist[k]-plist[k-ti]
                        if ssum < 1000000:
                            if isPrime(ssum, sieve):
                                longestChain = ti
                                pnum = ssum
                                done = 1
                                break
                        else: 
                            break

        else:
            ssum = 0
            for k in range(0,ti):
                ssum += plist[k]
            if ssum < 1000000:
                if isPrime(ssum, sieve):
                    longestChain = ti
                    pnum = ssum
                    done = 1
        if done:
            break

    print("Time Elapsed:", time()-t0)
    print(longestChain, pnum)


main()