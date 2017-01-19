#Problem: What is the first of the first four consecutive integers that have exactly 4 distinct prime factors?

import math
from time import time


def modSieveOfEratosthenes(x):
    #Produces a list of numbers under x, also tells how many prime factors they have
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
    #The strategy: THe first time I solved this, I did a really inefficient brute-force method, but then I saw
    #someone in the project Euler forums talk about modifying a sieve of eratostenes. I realized that was much
    #better, so I re-did the problem using the modified sieve. We simply generate a sieve that tells us how many
    #prime factors each composite number has, and then we coutn up, checking for 4 4's in a row.

    #Executes in  1.436 seconds -- still slower than I'd like
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



