
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

def totient(x, pfs):
    primes = pfs[x]
    totala = 1
    totalb = 1
    for i in primes:
        
        totala *= (i-1)
        totalb *= i
    return totala*1.0*x/totalb

def main():

    cap = 1000000
    sieve = primeFactorSieve(cap+10)
    
    #print(sieve)
    #print(plist, sieve)
    ssum = 0
    
    for i in range(2,cap+1):
        #print(totient(i,sieve))
        ssum+=int(totient(i,sieve))
    print(ssum)

main()