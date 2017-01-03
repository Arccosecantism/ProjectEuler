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
    prime = 1
    if soe[x] == 1:
        prime = 0
    return prime

def getPrimeList(soe):
    primelist = []
    for i in range(0,len(soe)):
        if soe[i] == 0:
            primelist.append(i)
    return primelist


def main():
    t0 = time()
    sieve = sieveOfEratosthenes(1000000)
    plist = getPrimeList(sieve)

    longestChain = 0
    done = 0
    pnum = 0
    stval = 999
    
    for i in range(0,stval):
        ti = stval-i
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