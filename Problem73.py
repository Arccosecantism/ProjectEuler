#Problem: how many unique rationals p/q where p,q <= 12000; p,q are integers are there where 1/3<p/q<1/2

import math
from time import time

def totientSieve(x):
    #Produces a list of totient(n) for all n < x: uses a modified prime factor sieve
    ar = []
    for i in range(-1,x):
        ar.append(i+1)
    
    ub = int(x/2)+1
    for i in range(2,ub):
        if ar[i] == i:
            for k in range(i,x,i):
                ar[k]=int(ar[k]*(1-1.0/i))
    for i in range(ub-1,x):
        if ar[i] == i:
            ar[i] -= 1
    return ar

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

def getUnderThirdCount(denom, pfs):
    if denom == 2:
        return 0
    facs = pfs[denom]
    ub = int(denom/3)
    thirdList = [1]*ub
    na = denom
    nb = 1
    for i in facs:
        for k in range(i-1,len(thirdList),i):
            thirdList[k] = 0
        #print(thirdList, i)

    return sum(thirdList)
        

def main():
    #The Strategy: We simply sum up, for each denominator, how many numerators will result in a fraction
    #less than 1/3, and then we find the total amount of rationals for 12000,
    # sort of divide that number by two to find the amount of rationals above 1/2, and then subtract the amount under
    #1/3 and the amount above 1/2 to find the answer

    #Executes in 2.5 seconds
    t0 = time()
    cap = 12000

    tsieve = totientSieve(cap+1)
    pfsieve = primeFactorSieve(cap+1)
    totsum = sum(tsieve[2:cap+1])
    under_one_third = 0
    for i in range(2,cap+1):
        under_one_third += getUnderThirdCount(i,pfsieve)

    over_one_half = int(math.ceil(totsum*1.0/2))
    print("Time Elapsed:", time()-t0)
    print(totsum-under_one_third-over_one_half)



main()