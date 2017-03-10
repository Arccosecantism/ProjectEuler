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


def dumbSortFracs(fracList):
    tl = list(fracList)
    nl = []
    for i in range(0,len(fracList)):
        minVal = 2
        minFrac = [0,0]
        minSpot = -1
        for k in range(0,len(tl)):
            fv = tl[k][0]*1.0/tl[k][1]
            if fv < minVal:
                minVal = fv
                minFrac = tl[k]
                minSpot = k
        del tl[minSpot]
        nl.append(minFrac)
    return nl

def gcf(x,y):
    #Euclid's method for finding greatest common factor
    a = max(x,y)
    b = x+y-a
    r = 2
    while r:
        r=a%b
        a=b
        b=r
    return a

def genFracListCapped(cap):
    fracList = []
    for i in range(2,cap+1):
        for k in range(1,i):
            gv = gcf(i,k)
            if gv == 1:
                fracList.append([k,i])
    return dumbSortFracs(fracList)

def getBetterFracForm(sfl):
    strList = []
    for i in sfl:
        ns = str(i[0])+"/"+str(i[1])
        strList.append(ns)
    return strList

def main():
    #The Strategy: We simply check every denominator, and find all the numerators that create a irreducible rational between 1/3 and 1/2, and sum up
    #the amounts

    #Executes in 28.4 seconds -- disappointing
    t0 = time()
    cap = 30

    fracList = genFracListCapped(cap)
    bFracList = []
    atFracList = []
    btFracList = []
    ctFracList = []
    cFracList = []
    for i in fracList:
        tmpval = i[0]*1.0/i[1]
        if tmpval<=1.0/3:
            atFracList.append(i)
        elif tmpval < 1.0/2:
            bFracList.append(i)
        else:
            cFracList.append(i)
        if tmpval > 1.0/3 and tmpval <= 2.0/3:
            btFracList.append(i)
        elif tmpval > 2.0/3:
            ctFracList.append(i)

    

    tsieve = totientSieve(cap+1)

    totsum = sum(tsieve[2:cap+1])
    under_one_third = int(math.ceil(totsum*1.0/3))
    over_one_half = int(math.ceil(totsum*1.0/2))
    print("Time Elapsed:", time()-t0)
    print(getBetterFracForm(fracList))
    print("break")
    print(getBetterFracForm(atFracList))
    print("break")
    print(len(atFracList), len(btFracList), len(ctFracList)+1, len(fracList))
    print("break")
    print(under_one_third, totsum,over_one_half)
    print("break")
    print(getBetterFracForm(bFracList))
    print("break")
    print(getBetterFracForm(cFracList))
    print("break")
    print(len(bFracList))
    print("break")
    print(totsum-under_one_third-over_one_half)



main()