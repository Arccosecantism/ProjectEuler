import math
from time import time

def sieveOfEratosthenes(x):
    #Produces a list of numbers under x, also tells if they are prime.
    #this is to create an O(1) prime checker for primes under x 
    ar = []
    flick = True
    for i in range(-1,x):
        val = 1
        if flick:
            val = 0
        ar.append(val)
        flick = not(flick)
    ar[1] = 0
    ar[2] = 1
    ub = int(math.ceil(math.sqrt(len(ar)))+1)
    for i in range(2,ub):
        if ar[i]:
            for k in range(i*i,x,i):
                ar[k] = 0
    return ar

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




#For the next functions, an explanation is in order: After doing some research, I found the best way
#to solve this problem was by finding the Euler transform of a =[0,1,1,0,1,0,1,0,0,0,1,0,1...] where each prime 
#numbered-spot = 1 and the rest are 0. You find the Euler transform by generating c, where the nth term of c is 
#d*a[d] for all divisors d of n. Because a[d] = 0 for non-prime d and 1 for prime d, c[n] = sum(prime factors of c)
#then, b, the Euler transform, is  b[n]=1/n*(c[n]+ {sum from k=1 to n-1 of}(c[k]b[n-k]) ) and b[1] = c[1]. 
#Then b[n] is the number  of ways to write n as the sum of prime numbers, somehow. 
#This is ridiculously non-intuitive, and I have no idea why it works

def findNthCValue(n, pfs):
    #finds the nth c value
    divs = pfs[n]
    return sum(divs)
            
def getBSequence(cseq):
    #generates the Euler transform of the sequence a, which is the b sequence
    bseq = [0,cseq[1]]
    for i in range(2,len(cseq)):
        ssum = 0
        for k in range(1,i):
            ssum+=cseq[k]*bseq[i-k]
        bv = int(1.0/i*(cseq[i]+ssum))
        bseq.append(bv)
    return bseq

def main():
    #The strategy: we generate the c sequence up to 1000 (ends up being big enough), and then generate the b sequence.
    # Then We simply find the first k such that bSequnce[k] > 5000 

    #Executes in .251 seconds

    t0 = time()
    sieve = sieveOfEratosthenes(10000)
    primeFactorList = primeFactorSieve(10000)
    
    cSequence = []
    for i in range(0,1000):
        cSequence.append(findNthCValue(i,primeFactorList))

    bSequence = getBSequence(cSequence)

    first_fk_val = -1
    for i in range(0,len(bSequence)):
        if bSequence[i] > 5000 and first_fk_val == -1:
            first_fk_val = i
            break
    print("Time Elapsed:", time()-t0)
    print(first_fk_val)
main()

