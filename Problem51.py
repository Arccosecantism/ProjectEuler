
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

def digitListListToNumList(diglistlist):
    nlist = []
    for i in diglistlist:
        num = int(''.join(map(str,list(i))))
        nlist.append(num)
    return nlist

def getPositionIndicators(num, maxlen):
    indics = []
    numlist = []
    for i in range(1, maxlen):
        numlist.append([i,1])
    subsets = generateSubsets(num, numlist)
    #print(subsets)
    for i in subsets:
        tlist = []
        for k in range(0,maxlen):
            tlist.append(0)
        for k in i:
            tlist[k-1] = 1
        indics.append(tlist)
    return indics

def generateSubsets(siz, numlist):
    newlist = []
    if siz > 0:
        for i in range(0,len(numlist)):
            if numlist[i][1] == 1 and len(numlist)-i >= siz :
                for k in range(0,i+1):
                    numlist[k][1] = 0 
                nextstep = generateSubsets(siz-1, numlist)
                for k in nextstep:
                    al = [numlist[i][0]]
                    bl = list(k)
                    cl = al+bl
                    newlist.append(list(cl)) 
                for k in range(0,i+1):
                    numlist[k][1] = 1 
    else:
        newlist.append([])
    return newlist


def constructNumberPossibilities(positions):
    lastDigit = [1,3,7,9]
    nlist = [[]]
    newl = []
    openfirst = positions[0]
    for i in range(0,len(positions)-1):
        if positions[i] == 1:
            for k in nlist:
                k.append(-1)
        elif positions[i] == 0:
            newl = []
            for k in nlist:
                st = 0
                if i == 0:
                    #print(positions)
                    st = 1
                for j in range(st,10):
                    tk = list(k)
                    tk.append(j)
                    newl.append(tk)
            nlist = list(newl)
    
    newl = []
    for k in nlist:
        for j in range(0,4):
            tk = list(k)
            tk.append(lastDigit[j])
            newl.append(tk)
    nlist = list(newl)
   # print(nlist)
    finalList = []
    st = 0
    if positions[0] == 1:
        st = 1
    for i in nlist:
        plist = []
        
        for k in range(st,10):
            ti = list(i)
            for j in range(0,len(ti)):
                if ti[j] == -1:
                    ti[j] = k
            plist.append(ti)
        finalList.append(plist)
    return finalList






def main():
    
    t0 = time()

    sieve = sieveOfEratosthenes(1000000)

    found = 0
    digctr = 5
    required = 8
    small = 0
    #while not(found):

    positions = getPositionIndicators(3,6)
    print(positions)
    digs = []
    for i in positions:
        numpos = constructNumberPossibilities(i)
        for k in numpos:
            digs.append(digitListListToNumList(list(k)))
    print(len(digs))

    #print(isPrime(1107,sieve))
    for i in digs:
        rc = 0
        for k in i:
            if isPrime(k,sieve):
                rc+=1
        if rc >= required:
            print(i)
            small = i[0]
            found = 1
        if found:
            break 

    print("Time Elapsed:", time()-t0)
    print(small)
main()