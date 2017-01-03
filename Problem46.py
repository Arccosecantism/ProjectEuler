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
    for i in range(0,x):
        if soe[i] == 0:
            primelist.append(i)
    return primelist

def getDoubleSquareList(x):
    ar = []
    dsq = 0
    fd = -2
    sd = 4 

    while dsq < x:
        ar.append(dsq)
        fd += sd
        dsq += fd
    return ar

def isTwiceSquare(x):
    if x%2 == 1:
        return 0
    prec = .0000001
    tes = math.sqrt(x/2)
    if abs(test-int(tes)) < prec:
        return 1
    return 0

def main():
    t0 = time()
    sieve = sieveOfEratosthenes(1000000)
    doubleSquareList = getDoubleSquareList(1000000)
    ctr = 9
    done = 0
    while not(done) and ctr < 1000000:
        if not(isPrime(ctr,sieve)):
            bk = 1
            for i in doubleSquareList:
                if isPrime(ctr-i,sieve):
                    #print(ctr, i/2, ctr-i)
                    bk = 0
                    break
            if bk:
                done = 1

        ctr += 2
    ans = ctr - 2
    print("Time Elapsed:", time()-t0)
    print(ans)
main()