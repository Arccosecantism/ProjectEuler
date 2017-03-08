#Problem: How many unique rational numbers p/q are there such that p,q are integers; 0<(p/q)<1; p,q < 1000000 (one million)? (We have to
#            discount reductions: that is, 9/15 is not distinct from 3/5)
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


def main():
    #The strategy: This is pretty obvious, especially since we covered totients earlier. A rational will be unique if it is irreducible. 
    #A rational is irreducible if the numerator and denominator are relatively prime. So the number of rationals between 0 and 1 with a given denominator d
    #is equal to the number of integers under d that are relatively prime to d, which is exactly the definithin of totient(d)=phi(d)

    #So, we simply generate phi(j) for 2<=j<=1000000 and sum them up
    #Executes in 7.131 seconds (I looked online, haven't seen much better times)
    t0 = time()
    cap = 1000000
    sieve = totientSieve(cap+10)
    
    print("here")
    #print(plist, sieve)
    ssum = sum(sieve[1:cap+1])-1
    
    #for i in range(2,cap+1):
        #print(totient(i,sieve))
    #    ssum+=sieve[i]
    print("Time Elapsed:", time()-t0)
    print(ssum)

main()