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
    #gets a prime list from sieve
    primelist = []
    for i in range(0,len(soe)):
        if soe[i] == False:
            primelist.append(i)
    return primelist


def main():

    t0 = time()
    psieve = sieveOfEratosthenes(10000)
    plist = getPrimeList(psieve)
    #print(plist)
    cap = 50000000

    two_ctr = 0

    two_val = 4
    three_val = 8
    four_val = 16

    results = set([])
    while two_val < cap:
        two_val = plist[two_ctr]**2
        three_ctr = 0
        while three_val < cap-two_val:
            three_val = plist[three_ctr]**3
            four_ctr = 0
            while four_val < cap-two_val-three_val:
                four_val = plist[four_ctr]**4
                valsum = two_val+three_val+four_val
                #print((two_val,three_val,four_val),valsum)
                if valsum < cap:
                    results.add(valsum)
                four_ctr += 1
            four_val = 16    
            three_ctr += 1
        three_val = 8
        two_ctr += 1

    #print(results)
    finalAmount = len(results)
    print("Time Elapsed:  " + str(time()-t0))
    print(finalAmount)
main() 