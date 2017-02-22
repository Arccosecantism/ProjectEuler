
import math
from time import time

def sieveOfEratosthenes(x):
    #Produces a list of numbers under x, also tells if they are prime.
    #this is to create an O(1) prime checker for primes under x 
    ar = []
    flick = True
    for i in range(-1,x):
        ar.append(flick)
        flick = not(flick)
    ar[1] = True
    ar[2] = False
    ub = int(math.ceil(math.sqrt(len(ar)))+1)
    for i in range(2,ub):
        if not(ar[i]):
            for k in range(i*i,x,i):
                ar[k] = True
    return ar

def isPrimeL(x, plist, soe):
    #checks if a number that has prime factors in prime list is prime -- good for checking large numbers
    #if a number is too large, the sieve of eratosthenes takes too long to generate, so we can't have an O(1) check
    #But, if the number is small, this function defaults to an O(1) check
    if x<len(soe):
        if soe[x] == False:
            return 1
    else:
        prime = 1
        mxc = goodSqrt(x)
        for i in plist:
            if not(x%i):
                prime = 0
            if i > mxc:
                break
        return prime
    return 0

def goodSqrt(x):
    #returns the squareroot, but rounded up to a very careful degree to avoid rounding errors
    return int(math.ceil(math.sqrt(x))+1)

def getPrimeList(soe):
    #gets a prime list of sieve
    primelist = []
    for i in range(0,len(soe)):
        if soe[i] == False:
            primelist.append(i)
    return primelist


def testCompatibility(pa, pb, soe, plist):
    sa = str(pa)
    sb = str(pb)
    ssum = 0
    for i in sa:
        ssum += ord(i)
    for i in sb:
        ssum += ord(i)
    if ssum%3 == 0:
        return 0
    sca = sa+sb
    scb = sb+sa
    return (isPrimeL(int(sca),plist,soe) and isPrimeL(int(scb),plist,soe))

def main():

    t0 = time()
    sieve = sieveOfEratosthenes(1000000)
    #print(time()-t0)

    cap = 100000
    plist = getPrimeList(sieve)
    tplist = []
    for i in range(4,len(plist)):
        if plist[i] > cap:
            break
        else:
            tplist.append(plist[i])
    print(tplist)
    primeGroups = [ [ [3,0], [7,0] ], [ [[3,7],[0,1],0] ], [],[],[] ]
    for i in tplist:
        print(i)
        pgl_1 = len(primeGroups) 
        pgl_2 = [len(primeGroups[g]) for g in range(0,pgl_1)]
        for k in range(0,pgl_1):
            
            
            if k == 0:
                #tp = time()
                for j in range(0,pgl_2[k]):
                
                    primeGroups[k][j][1] = testCompatibility(i,primeGroups[k][j][0],sieve,plist)
                    if primeGroups[k][j][1]:
                        primeGroups[k+1].append([[primeGroups[k][j][0],i],[j,pgl_2[0]],0])
                #print("TE:", time()-tp, time()-t0, i) 
                
            elif k < 4:
                for j in range(0,pgl_2[k]):

                    primeGroups[k][j][2] = primeGroups[0][primeGroups[k][j][1][1]][1] and primeGroups[k-1][primeGroups[k][j][1][0]][-1]
                    if primeGroups[k][j][2]:
                        primeGroups[k+1].append([list(primeGroups[k][j][0]+[i]),[j,pgl_2[0]],0])
                        

        primeGroups[0].append([i,0])
        if len(primeGroups[4]):
            break

    ssum = sum(primeGroups[4][0][0])
    print(primeGroups[4][0][0])
    print("Time Elapsed:", time()-t0)
    print(ssum)
  

main()