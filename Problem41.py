#Problem: An integer is pandigital n if it contains the digits 1-n exactly once in its decimal representation. so 2143 is pandigital 4. 
#         2143 is also prime, so 2134 is a pandigital prime. What is the largest pandigital prime that exists?
import math
from time import time

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

def getPrimeListUnder(x, soe):
    #gets a prime list under x, using a sieve
    primelist = []
    for i in range(0,x):
        if soe[i] == 0:
            primelist.append(i)
    return primelist

def goodSqrt(x):
    #returns the squareroot, but rounded up to a very careful degree to avoid rounding errors
    return int(math.ceil(math.sqrt(x))+1)

def isPrimeL(x, plist):
    #checks if a number that has prime factors in prime list is prime -- good for checking large numbers
    #if a number is too large, the sieve of eratosthenes takes too long to generate, so we can't have an O(1) check
    prime = 1
    for i in plist:
        if not(x%i):
            prime = 0
    return prime

def getReverseList(flist):
	#gives the reverse of a list: g([5,3,4]) = [4,3,5] 
	revlist = []
	for i in range(0,len(flist)):
		revlist.append(flist[len(flist)-1-i])
	return revlist

def multiplyLists(alist, listlist):
    #this is weird: it takes a list and a list of lists, and returns a list of lists which is the pairing
    #of the firs list with every element of the second list. It's hard to explain, so here is an example:
    # m([1,4,3], [[2,4], [], [1,3,5], [0,0]]) = [[1,4,3,2,4], [1,4,3,2,4], [1,4,3], [1,4,3,1,3,5], [1,4,3,0,0]]
    #this is only useful for some recursive functions
    nlist = []
    for i in range(0,len(listlist)):
        tmplista = list(alist)
        tmplistb = list(listlist[i])
        nlist.append(list(tmplista+tmplistb))
    return nlist

def getBackwardsPandigitalPrimeCandidates(numList, first):
    #gets all candidates for padigital primes out of a numberlist, but they are reversed.
    #it represents these numbers as a decimal digit list
    nlist = []
    empty = 1
    for k in numList:
        
        okay = 1
        if k[1] == 0:
            okay = 0
        if first == 1 and not((k[0] == 1 or k[0] == 3 or k[0] == 7 or k[0] == 9)):
            okay = 0
        if okay:
            empty = 0
            k[1] = 0
            tmplist = []
            tmplist.append(k[0])
            branches = multiplyLists(tmplist,getBackwardsPandigitalPrimeCandidates(numList,0))
            k[1] = 1   
            for j in branches:
                nlist.append(j)
    if empty == 1:
        nlist.append([])
    return nlist          

def getPandigitalPrimeCandidates():
    # gets all candidates for pandigital primes
    #we only do 4-digit numbers and 7-digit numbers, because no other pandigital n numbers are definitely not prime:
    #if a number is pandigital 9, for instnace, the sum of the digits is always 45, a multiple of 3, so it's divisible by 3.
    #the same is true for  a pandigital x number where x is in {2,3,5,6,8}
    numlist_4 = []
    for i in range(1,5):
        numlist_4.append([i,1])
    
    numlist_7 = []
    for i in range(1,8):
        numlist_7.append([i,1])

    rev_cand_4 = getBackwardsPandigitalPrimeCandidates(numlist_4, 1)
    rev_cand_7 = getBackwardsPandigitalPrimeCandidates(numlist_7, 1)
    cand_4 = []
    for i in rev_cand_4:
        cand_4.append(getReverseList(list(i)))
    
    cand_7 = []
    for i in rev_cand_7:
        cand_7.append(getReverseList(list(i)))
    
    totcand_l = list(cand_4+cand_7)
    totcand_i = []
    for i in totcand_l:
        totcand_i.append(int(''.join(map(str,i))))
    
    return totcand_i

def main():
    #the strategy: we generate all possible pandigital primes. a possible pandigital prime is an ordering of 1-n where n = 4 or 7, and the last digit is 1,3,7, or 9.
    #so 1234 is not a possible pandigital prime, but 2341 is. 15243 is not. Then we just check each one if it's prime, and store the largest
    #

    t0 = time()
    cap = 8000000
    pandigPrimeCand = getPandigitalPrimeCandidates()
    sieve = sieveOfEratosthenes(goodSqrt(cap)+1)
    primeList = getPrimeListUnder(goodSqrt(cap)+1, sieve)
    largest = 0
    for i in pandigPrimeCand:
        if i > largest:
            if isPrimeL(i, primeList):
                largest = i
            
    print("Time Elapsed:", time()-t0)
    print(largest)
main()