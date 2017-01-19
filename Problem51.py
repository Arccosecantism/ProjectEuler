#Problem: I cannot explain this problem well -- this is a copy-paste:

#           By replacing the 1st digit of the 2-digit number *3, it turns out that six of the nine possible values: 
#           13, 23, 43, 53, 73, and 83, are all prime.

#           By replacing the 3rd and 4th digits of 56**3 with the same digit, this 5-digit number is the first example 
#           having seven primes among the ten generated numbers, yielding the family:
#           56003, 56113, 56333, 56443, 56663, 56773, and 56993. 
#           Consequently 56003, being the first member of this family, is the smallest prime with this property.

#           Find the smallest prime which, by replacing part of the number (not necessarily adjacent digits) with the
#           same digit, is part of an eight prime value family.

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
    #O(1) primality checker
    prime = 1
    if soe[x] == 1:
        prime = 0
    return prime

def digitListListToNumList(diglistlist):
    #Converts a list of digit-lists to lists of ints
    nlist = []
    for i in diglistlist:
        num = int(''.join(map(str,list(i))))
        nlist.append(num)
    return nlist

def generateSubsets(siz, numlist):
    #Recursively gets all siz-sized subsets of a number list: so (2,[[1,1],[2,1],[3,1]])) = [[1,2],[1,3],[2,3]]
    #The number list is a bit confusing -- it is all the umbers you want in a pair with 1: so
    #If you want subsets of {3,6,7}, the number list used is [[3,1],[6,1],[7,1]] -- works better for 
    #recursion
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


def getPositionIndicators(num, maxlen):
    #Get the possible positions of digis that can be incremented for num positions and a nubmer length of maxlen
    #So gp(3,5) = [[1,1,1,0,0],[1,1,0,1,0],[1,0,1,1,0],[0,1,1,1,0]]. The last digit is always 0 because you can
    #never increment that digit and have the number be prime 8 times.
    indics = []
    numlist = []
    for i in range(1, maxlen):
        numlist.append([i,1])
    subsets = generateSubsets(num, numlist)
    for i in subsets:
        tlist = []
        for k in range(0,maxlen):
            tlist.append(0)
        for k in i:
            tlist[k-1] = 1
        indics.append(tlist)
    return indics



def constructNumberPossibilities(positions):
    #It's complicated which numbers get returned, but they are all the ones that are candidates for being a number
    #like the one described at the top. The numbers are grouped in families
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
    #The Strategy: We use brute force with some optimizations. First, we assume the nubmer we are
    #looking for will have 6 digits -- otherwise the sieve will take much longer to generate. Using modular
    #arithmetic, we know only a multiple of 3 (in this case 3) digits that aren't the last digit must be changed;
    #otherwise, one of the numbers will be a multiple of 3. We generate all possible numbers and check them,
    #remembering the smallest one.

    #Executes in 1.333 seconds
    t0 = time()
    sieve = sieveOfEratosthenes(1000000)

    found = 0
    digctr = 5
    required = 8
    small = 0
    #while not(found):

    positions = getPositionIndicators(3,6)
    digs = []
    for i in positions:
        numpos = constructNumberPossibilities(i)
        for k in numpos:
            digs.append(digitListListToNumList(list(k)))

    for i in digs:
        rc = 0
        for k in i:
            if isPrime(k,sieve):
                rc+=1
        if rc >= required:
            small = i[0]
            found = 1
        if found:
            break 

    print("Time Elapsed:", time()-t0)
    print(small)
main()