#Problem: 	What integers a and b (-1000<a<1000; -1000<b<1000), when used as coefficients in f(n)=n^2+an+b, will result in the longest sequence of primes for consecutive
#           integers (starting from 0) values of n?

import math
from time import time

def sieveOfEratosthenes(x):
    #Produces a list of numbers under x, also tellis if they are prime.
    #this is to create an O(1) prime checker for primes under x 
    ar = []
    for i in range(0,x):
        ar.append([i+1,0])
    for i in range(1,len(ar)):
        ti = i+1
        if not(ar[i][1]):
            for k in range(i+1,len(ar)):
                tk = k+1
                if not(ar[k][1]):
                    ar[k][1] = not(tk%ti) 
   # print(ar)
    return ar
    

def isPrime(x,par):
    #Tells if a number is prime -- O(1)
    if x-1 < 0 or x-1 >= len(par):
        print("Error: ", x)
    return not(par[x-1][1])

def checkConsecutiveValues(b,c,par):
    #for f(n) = n^2 + bn + c, finds the length of the sequence of primes for consecutive integers (starting from 0) values of n
    val = c
    fd = b+1
    sd = 2
    numberReached = 0
    while isPrime(val,par):
        numberReached += 1
       
        val += fd
        fd += sd
       # print(val)
    return numberReached

def checkRoots(b,c):
    #a helpful optimization -- looks at the roots of the quadratic to se if they go negative.
    #because we know n^2+n+41, which produces 40 primes in a row is not the greatest, we know that 
    #n^2 + bn + c can't be negative in the range (0,40)
    good = 1
    if b*b-4*c > 0:
       r1 = (-b+math.sqrt(b*b-4*c))/2
       r2 = (-b-math.sqrt(b*b-4*c))/2
       if (r1 > 0  and r1 < 40) or (r2 > 0 and r2 < 40):
           good = 0
    return good




def main():
	#This is a tricky problem. It's straightforward, but there are a few optimizations required. The strategy is to test all values of a and b 
    #and check the number of consecutive prime values and keep track of the largest coeeficients. Three optimizations I used: b must be odd and prime,
    #the quadratic must not have any real roots in the range(0,40), and a sieve of Eratosthenes trades a minor amount of memory and 5-ish seconds of
    #generation time for an O(1) prime check instead of a O(sqrt(n)) check. Overall, executes in 6.61 seconds, and generating the sieves takes 5.35 seconds
    # -- I'm a bit unhappy with the total time, but it's better than what I started with, which was about a 2 minute execute time. 
    tic = time()
    pcap = 20000
    ncap = 1000
    par = sieveOfEratosthenes(pcap)
    cposar = sieveOfEratosthenes(ncap) 
    print("Time Elapsed: ", time() - tic)
    #print(cposar)
    longest = [0,0,0]
    
   # print(checkConsecutiveValues(-15,97,par))
    for i in range(1-ncap, ncap+1, 2):
        for k in range(1, ncap+1, 2):
            
            if checkRoots(i,k) and isPrime(k,par):
                
                cval = checkConsecutiveValues(i,k,par)
               # print("works:", i, k, cval)
                if cval > longest[2]:
                    longest = [i,k,cval]
            else:
                lop = 3
                #print("Found one:", i, k)

    print("Time Elapsed: ", time() - tic)
    #print(par)
    print(longest)
	
main()


