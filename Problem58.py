#Problem: Hard to depict part of the problem -- better to just visit the site: https://projecteuler.net/problem=58

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



def getPrimeList(soe):
    #gets a prime list of sieve
    primelist = []
    for i in range(0,len(soe)):
        if soe[i] == 0:
            primelist.append(i)
    return primelist

def goodSqrt(x):
    #returns the squareroot, but rounded up to a very careful degree to avoid rounding errors
    return int(math.ceil(math.sqrt(x))+1)

def isPrimeL(x, plist, soe):
    #checks if a number that has prime factors in prime list is prime -- good for checking large numbers
    #if a number is too large, the sieve of eratosthenes takes too long to generate, so we can't have an O(1) check
    #But, if the number is small, this function defaults to an O(1) check
    if x<len(soe):
        if soe[x] == 0:
            return 1
    else:
        prime = 1
        mxc = goodSqrt(x)
        for i in plist:
            if not(x%i):
                prime = 0
            if i > mxc:
                break
        return prime
    return 0

def main():
    #The Strategy: Get each corner value using some mathematical trickery, and check if each one is prime.
    #Stop when it falls below 10% primes on the diagonals.

    #Numbers get pretty large -- primalty tests are expensive: Executes in 11.17 seconds. I don't know if there
    #is a better way to do this aside from getting a better sieve and prime checker.
    t0 = time()
    sieve = sieveOfEratosthenes(1000000)
    plist = getPrimeList(sieve)
    sl = 1
    ctr = 0
    totnum = 1
    while sl < 100000:
        totnum += 4

        terms = [0,0,0]
        terms[0] = sl*sl+sl+1
        terms[1] = terms[0]+sl+1
        terms[2] = terms[1]+sl+1
        for i in range(0,3):
            ctr += isPrimeL(terms[i],plist,sieve)
        
        sl += 2
        if 10*ctr<totnum:
            break
    print("Time Elapsed:", time()-t0)
    print(sl)


main()