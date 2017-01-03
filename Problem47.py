import math
from time import time


def modSieveOfEratosthenes(x):
    #Produces a list of numbers under x, also tells if they are prime.
    #this is to create an O(1) prime checker for primes under x 
    ar = []
    for i in range(-1,x):
        ar.append(0)
    ar[0] = 0
    ar[1] = 0
    for i in range(2,x+1):
        if ar[i] == 0:
            ub2 = int(x/i)
            for k in range(0,ub2):
                tk = i*(k+1)
                ar[tk] += 1
    return ar



def main():
    t0 = time()
    msieve = modSieveOfEratosthenes(1000000)

    spot = 0
    chain = 0 
    for i in range(0,len(msieve)):
        if msieve[i] == 4:
            chain += 1
            if chain == 4:
                spot = i-3
                break
        else:
            chain = 0


    print("Time Elapsed:", time()-t0)
    print(spot)

main()



