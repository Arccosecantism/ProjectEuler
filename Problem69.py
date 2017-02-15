import math
from time import time


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




def altTotient(x, pfs):
    primes = pfs[x]
    totala = 1
    totalb = 1
    for i in primes:
        #print(1.0/i)
        totala *= (i-1)
        totalb *= i
    return (totalb*1.0)/totala

def main():

    sieve = primeFactorSieve(1000002)
    #print(sieve)
    #print(plist, sieve)
    altTots = []
    for i in range(1,1000000):
        altTots.append([i,altTotient(i,sieve)])
    largest = 0
    largestVal = 0
    for i in altTots:
        if i[1] > largest:
            largest = i[1]
            largestVal = i[0]
    print(largest,largestVal)

main()