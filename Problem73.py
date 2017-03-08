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



def main():
    #The Strategy: We simply check every denominator, and find all the numerators that create a irreducible rational between 1/3 and 1/2, and sum up
    #the amounts

    #Executes in 28.4 seconds -- disappointing
    t0 = time()
    cap = 15

    tsieve = totientSieve(cap+1)

    totsum = sum(tsieve[2:cap+1])
    under_one_third = int(math.floor((totsum-2)*1.0/3))+1
    over_one_half = int(math.ceil(totsum*1.0/2))
    print("Time Elapsed:", time()-t0)
    print(totsum-under_one_third-over_one_half)



main()