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


def getPrimeList(soe):
    #gets a prime list of sieve
    primelist = []
    for i in range(0,len(soe)):
        if soe[i] == False:
            primelist.append(i)
    return primelist


def testPermuations(x,y):
    sx = str(x)
    sy = str(y)
    arx = [int(i) for i in sx]
    ary = [int(i) for i in sy]
    arx.sort()
    ary.sort()
    return arx == ary 


def main():
    sieve = sieveOfEratosthenes(5000)
    plist = getPrimeList(sieve)
    mplist = []
    for i in plist:
        if i >= 2000:
            mplist.append(i)
    
    smallestRatio = 3
    smallestVal = 0
    smallestTot = 0
    tesx = 0
    totx = 0
    for i in range(0,len(mplist)-1):
        for k in range(i,len(mplist)):
            tesx = mplist[i]*mplist[k]
            totx = (mplist[i]-1)*(mplist[k]-1)
            if tesx < 10000000:
                if testPermuations(tesx,totx):
                    ratio = tesx*1.0/totx
                    if ratio < smallestRatio:
                        smallestRatio = ratio
                        smallestVal = tesx
                        smallestTot = totx

    print(smallestVal, smallestRatio)
   
main()
