
#Problem:   The number 3797 has an interesting property. Being prime itself, it is possible to continuously remove digits from left to right, and remain prime at each stage:
#           3797, 797, 97, and 7. Similarly we can work from right to left: 3797, 379, 37, and 3. Find the sum of the only eleven primes that are both truncatable from left to right and right to left.
#           By the way: 2, 3, 5, and 7 are not considered to be truncatable primes.


import math
from time import time

def digitsToInt(intList):
    #converts a list of digits to integers: d([4,6,1,3]) = 4613
    num = int(''.join(map(str,intList)))
    return num

def addLists(listlist):
    #combines a list of lists into one list with all the elements
    #for a([[3,4,5],[1,6],[],[0,0]]), the result is [3,4,5,1,6,0,0]
    retlist = []
    
    for i in range(0,len(listlist)):
            retlist += listlist[i]
    return retlist   

def sieveOfEratosthenes(x):
    #Produces a list of numbers under x, also tells if they are prime.
    #this is to create an O(1) prime checker for primes under x 
    ar = []
    for i in range(-1,x):
        ar.append(0)
    ar[0] = 1
    ar[1] = 1
    ub = int(math.ceil(math.sqrt(len(ar)))+1)
    for i in range(2,ub):
        if not(ar[i]):
            ub2 = int(x/i)
            for k in range(i-1,ub2):
                tk = i*(k+1)
                ar[tk] = 1
    return ar

def isPrime(x, soe):
    #checks if a number is prime
    if soe[x] == 0:
        return 1
    else:
        return 0

def getPossiblePrimeDigits(amt):
    #produces a list of <amt> integers taken from numList. So, g(2,[1,2,4]) = [[1,1],[1,2],[1,4],[2,1],[2,2],[2,4],[4,1],[4,2],[4,4]]
    #(not necessarily in this order)
    numListA = [1,3,7,9]
    numListB = [2,3,5,7]
    startSet = [[]]
    endSet = []
    ctr = 0
    once = 1
    while ctr < amt:
        for i in range(0,len(startSet)):
            if once:
                once = 0
                for k in numListB:
                    tmpset = list(startSet[i])
                    tmpset.append(k)
                    endSet.append(tmpset)
            else:
                for k in numListA:
                    tmpset = list(startSet[i])
                    tmpset.append(k)
                    endSet.append(tmpset)

        startSet = list(endSet)
        endSet = []
        ctr += 1      
    return startSet

def checkDigitListIsPrime(diglist, soe):
    #checks if digits make a prime number
    return isPrime(digitsToInt(diglist), soe)

def checkLeftTrunc(flist, soe):
    #checks if a number is left-truncatably prime
    isPrime = 1
    ml = len(flist)
    ctr = 0
    while ctr < ml and isPrime == 1:
        nlist = flist[ctr:]
        if not(checkDigitListIsPrime(nlist, soe)):
            isPrime = 0
        ctr += 1
    return isPrime

def checkRightTrunc(flist, soe):
    #checks if a number is right-truncatably prime
    isPrime = 1
    ml = len(flist)
    ctr = 0
    while ctr < ml and isPrime == 1:
        nc = len(flist)-ctr
        nlist = flist[:nc]
        if not(checkDigitListIsPrime(nlist, soe)):
            isPrime = 0
        ctr += 1
    return isPrime


def main():
    #The strategy: We first notice that all of the digits except the leftmost must be 1,3,7,or 9 and we know the rightmost has to be 2,3,5,or 7 because by truncating, each digits
    #will end up being the last one. We create all the possible combinations of {2,3,5,7} followed by 1-5 amount of {1,3,7,9}. Then we simply check if the number is left and right truncatable.
    #Also, we just assume all the numbers are under 1000000 -- it turns out that there are 11 truncatable primes under 1000000, so we know we are done, but I suppose there is technically not
    #guarantee. Execution time is 3.7 seconds
    t0 = time()
    sieve = sieveOfEratosthenes(1000000)
    cap = 6
    primePos = []
    for i in range(2, cap+1):
        tmpset = getPossiblePrimeDigits(i)
        primePos.append(tmpset)
    primePos = addLists(primePos)
    ssum = 0
    for i in primePos:
        if checkLeftTrunc(i, sieve) and checkRightTrunc(i, sieve):
            ssum += digitsToInt(i)

    print("time Elapsed:", time()-t0)
    print(ssum)

main()