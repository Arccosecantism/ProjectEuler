import math
from time import time

def removeDuplicates(la):
    if len(la) == 0 or len(la) == 1:
        return la
    lb = [la[0]]
    for i in range(1,len(la)):
        good = True
        for k in lb:
            if k == la[i]:
                good = False
        if good:
            lb.append(la[i])
    return lb

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

def primeFactorize(num, pfs):
    pfac = pfs[num]
    ctr = 0
    pfacl = []
    tn = num
    while tn > 1:
        while not(tn%pfac[ctr]):
            tn /= pfac[ctr]
            pfacl.append(pfac[ctr])
        ctr += 1
    return pfacl
    
        
def generatePrimeFactorList(cap):
    pfsieve = primeFactorSieve(cap+10)
    primeFactors = [[],[]]
    for i in range(2,cap+1):
        primeFactors.append(primeFactorize(i,pfsieve))
    return primeFactors

def getFactorizations(x,pfl,fzl):
    #print(x,fzl)
    if fzl[x] != []:
        return fzl[x]

    xpfs = pfl[x]
    if len(xpfs) <= 1:
        return [[x]]
    tack = xpfs[-1]
    sx = x//tack

    prefacs = getFactorizations(sx,pfl,fzl)

    faczns = []
    for i in prefacs:
        ti = list(i)
        faczns.append(ti+[tack])
        if not(ti[-1]%tack):
            ti[-1] *= tack
            faczns.append(ti)
        else:
            dif = 0
            for j in range(0,len(ti)):
                if ti[j] != dif:
                    ui = list(ti)
                    ui[j]*=tack
                    faczns.append(ui)
                    dif = ti[j]
    return faczns
def main():
    t0 = time()
    rcap = 12000
    cap = 2*rcap
    
    primeFactorList = generatePrimeFactorList(cap+10)
    factorizationList = [list([])]*(cap+2)
    #print(factorizationList)
    for i in range(2,cap+1):
        factorizationList[i] = getFactorizations(i,primeFactorList,factorizationList)
    minPSNums = [0]*(rcap+1)
    for i in range(2,len(factorizationList)):

        for j in factorizationList[i]:
            if len(j)>1:
                ssum = sum(j)
                idx = i-ssum+len(j)
                if idx <= rcap:
                    if minPSNums[idx] == 0:
                        minPSNums[idx] = i
    mpnSet = set([])
    for i in minPSNums:
        if i > 0:
            mpnSet.add(i)
    fsum = sum(mpnSet)
    print("Time Elapsed:  " + str(time()-t0))
    print(fsum)



main()
             
