#Problem: what number n<10000000 (ten milliion) has totient(n) = phi(n) = k where k and n have the same digits in a different order and minimizes 
#         n/phi(n)?

import math
from time import time

def sieveOfEratosthenes(x):
    #Produces a list of numbers under x, also tells if they are prime.
    #this is to create an O(1) prime checker for primes under x 
    ar = []
    flick = True
    for i in range(-1,x):
        ar.append(flick)
        flick = not(flick)
    ar[1] = True
    ar[2] = False
    ub = int(math.ceil(math.sqrt(len(ar)))+1)
    for i in range(2,ub):
        if not(ar[i]):
            for k in range(i*i,x,i):
                ar[k] = True
    return ar


def getPrimeList(soe):
    #gets a prime list from sieve
    primelist = []
    for i in range(0,len(soe)):
        if soe[i] == False:
            primelist.append(i)
    return primelist


def testPermuations(x,y):
    #Tests if two numbers have the same digits -- if x is a digital re-ordering of y
    sx = str(x)
    sy = str(y)
    arx = [int(i) for i in sx]
    ary = [int(i) for i in sy]
    arx.sort()
    ary.sort()
    return arx == ary 


def main():
    #The Strategy: The first thing to realize is that minimizing n/phi(n) is the hard part. What does this look like? Well, n/phi(n) is 
    #equal to P/Q where P is the product of all unique prime factors of n and Q is the product of all (unique prime factors - 1). So,
    #having more unique unique prime factors increases n/phi(n). But we want to minimize it, so n should have very few prime factors.
    #The case where n is prime is obviously the best, however, phi(n) where n is prime is n-1, which can't be a digital reordering
    #So, we need to check multiples of two primes and hope one of them works.
    #If our max is 10000000, the center of factors (the squareroot) is 3,200-ish. Going out a reasonable amount, we'll check numbers that
    #are products of primes beteween 2000 and 5000.
    #Then, the work is easy -- generate all the numbers, check if they are permutations, and record the one that has the largest n/phi(n)

    #Executes in .739 seconds
    t0 = time()
    sieve = sieveOfEratosthenes(5000)
    plist = getPrimeList(sieve)
    mplist = []
    for i in plist:
        if i >= 2000:
            mplist.append(i)
    
    smallestRatio = 3
    smallestVal = 0
    smallestTot = 0
    tesx = 0
    totx = 0
    for i in range(0,len(mplist)-1):
        for k in range(i,len(mplist)):
            tesx = mplist[i]*mplist[k]
            totx = (mplist[i]-1)*(mplist[k]-1)
            if tesx < 10000000:
                if testPermuations(tesx,totx):
                    ratio = tesx*1.0/totx
                    if ratio < smallestRatio:
                        smallestRatio = ratio
                        smallestVal = tesx
                        smallestTot = totx
    print("Time Elapsed:", time()-t0)
    print(smallestVal, smallestRatio)
   
main()
