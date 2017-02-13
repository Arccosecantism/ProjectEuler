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



def getBetweenFractions(x, lb, ub, pfs):
    pfacs = pfs[x]
    tnums = [i for i in range(lb,ub)]
    fnums = []
    for i in tnums:
        ctr = 0
        done = 0
        while not(done) and ctr<len(pfacs):
            if not(i%pfacs[ctr]):
                done = 1 
            ctr+=1
        if not(done):
            fnums.append(i)
    return fnums


def main():

    cap = 12000

    psieve = primeFactorSieve(cap+1)

    one_third = 1.0/3.0
    one_half = .5

    
    ssum = 0
    for i in range(5,cap+1):
        lb = int(math.ceil(one_third*i))
        ub = int(math.ceil(one_half*i))
        bfs = getBetweenFractions(i,lb,ub,psieve)
        #print(bfs)
        ssum += len(bfs)
    print(ssum)

main()