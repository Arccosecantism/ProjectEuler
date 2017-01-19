#Problem: There are 2 sets of 3 4-digit numbers that are an arithmetic sequence, are all prime, and are permutations
#           of each other in base 10. One is {1487, 4817, 8147}. What is the other one?


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

def isPrime(x, soe):
    #O(1) prime checker
    prime = 1
    if soe[x] == 1:
        prime = 0
    return prime

def numToDigitAmounts(x):
    #breaks a number up into an array of digit amounts -- so N(15224233) = [[1,1], [2,3], [3,2], [4,1], [5,1]]
    sx = str(x)
    ar = []
    prev = -1
    for i in sx:
        if int(i) == prev:
            ar[-1][1]+=1
            
        else:
            ar.append([int(i), 1])
            prev = int(i)
    return ar

def multiplyLists(alist, listlist):
    #confusing: takes a list and a list of lists and combines them in a multiplicative way:
    #M([3,2,1], [[0,4,5], [], [1,2]]) = [[3,2,1,0,4,5], [3,2,1], [3,2,1,1,2]]
    nlist = []
    for i in range(0,len(listlist)):
        tmplista = list(alist)
        tmplistb = list(listlist[i])
        nlist.append(list(tmplista+tmplistb))
    return nlist

def getPermutations(numList):
    #recursively gets all permutations with no duplicates of an array describing the amount of digits.
    #So GP([[1,1],[3,2]]) = [[1,3,3], [3,1,3], [3,3,1]]
    nlist = []
    empty = 1
    for k in numList:
        if k[1] >= 1:
            empty = 0
            k[1] -= 1
            tmplist = []
            tmplist.append(k[0])
            branches = multiplyLists(tmplist,getPermutations(numList))
            k[1] += 1   
            for j in branches:
                nlist.append(j)
    if empty == 1:
        nlist.append([])
    return nlist

def digitListListToNumList(diglistlist):
    #Turns a list of digit lists into a list of integers
    nlist = []
    for i in diglistlist:
        num = int(''.join(map(str,list(i))))
        nlist.append(num)
    return nlist

def getNumericalPermutations(x):
    #combines some previous functions -- gets all base 10 permutions of a number
    #So GN(1332) = [1233, 1323, 1332, 2133, 2313, 2331, 3123, 3132, 3213, 3231, 3312, 3321]
    #(not necessarily in this order)
    return digitListListToNumList(getPermutations(numToDigitAmounts(x)))

def getLargerPrimePermutations(x, soe):
    #Out of a list of numerical permutation of a number x, gets the ones
    #that are both larger and prime
    n_perms = getNumericalPermutations(x)
    p_perms = []
    for i in n_perms:
        if isPrime(i,soe) and i > x:
            p_perms.append(i)
    return p_perms
    
def getPermutationSeries(x, soe):
    #Out of list of numbers (that happen to be larger prime permutations of x),
    #Picks all possible subsets that have size three and include x.
    pser = []
    perms = getLargerPrimePermutations(x, soe)
    perms.sort()
    for i in range(0,len(perms)-1):
        for k in range(i+1,len(perms)):
            pser.append([x,perms[i],perms[k]])
    return pser

def checkIfArithmetic(series):
    #Checks if a series is arithmetic
    if series[2]-series[1] == series[1]-series[0]:
        return 1
    return 0

def main():
    #The Strategy: Check all prime 4-digit numbers k by getting the larger prime permutations of k, getting all
    #3-large subsets containing k and checking if they are arithmetic progressions. If there is one, keep k

    #Executes in 
    t0 = time()
    sieve = sieveOfEratosthenes(10000)
    done = 0
    goodSeries = []
    for i in range(1001,9999,2):
        if isPrime(i,sieve) and i != 1487:
            ps = getPermutationSeries(i,sieve)
            if len(ps) > 0:
                for k in ps:
                    if checkIfArithmetic(k):
                        goodSeries = [k]
                        done = 1
                        break
        if done:
            break

    print("Time Elapsed", time()-t0)
    print(goodSeries)
main()
    