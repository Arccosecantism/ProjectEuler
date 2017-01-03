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
    prime = 1
    if soe[x] == 1:
        prime = 0
    return prime

def numToDigitAmounts(x):
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
    nlist = []
    #print(alist, listlist)
    for i in range(0,len(listlist)):
        tmplista = list(alist)
        tmplistb = list(listlist[i])
        nlist.append(list(tmplista+tmplistb))
    return nlist

def getPermutations(numList):
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
    nlist = []
    for i in diglistlist:
        num = int(''.join(map(str,list(i))))
        nlist.append(num)
    return nlist

def getNumericalPermutations(x):
    return digitListListToNumList(getPermutations(numToDigitAmounts(x)))

def getLargerPrimePermutations(x, soe):
    n_perms = getNumericalPermutations(x)
    p_perms = []
    for i in n_perms:
        if isPrime(i,soe) and i > x:
            p_perms.append(i)
    return p_perms
    
def getPermutationSeries(x, soe):
    pser = []
    perms = getLargerPrimePermutations(x, soe)
    perms.sort()
    for i in range(0,len(perms)-1):
        for k in range(i+1,len(perms)):
            pser.append([x,perms[i],perms[k]])
    return pser

def checkIfArithmetic(series):
    if series[2]-series[1] == series[1]-series[0]:
        return 1
    return 0

def main():
    t0 = time()
    sieve = sieveOfEratosthenes(1000000)
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
    