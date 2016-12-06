#Problem: Find the sum of all numbers that can be written as the sum of the fifth powers of their digits. (excluding 1)

import math
from time import time

def getFifthPowerSum(ar):
    #determines whether an array of integers, when the fifth powers of the integers are added together,
    #equal some number that uses an ordering of those integers as its digits. Returns 0 if it doesn't; returns the
    #sum of the fifth powers of the digits if it does

    fifthPower = [0,1,32,243,1024,3125,7776,16807,32768,59049]
    ssum = 0
    dpow = 0
    ctr = 1
    dn = 0
    for i in ar:
        ssum += fifthPower[i]
    strsm = str(ssum)
    tsum = 0
    strar = []
    arar = []
    for i in strsm:
        tmpval = ord(i)-ord('0')
        strar.append(tmpval)
    
   

    for i in ar:
        arar.append(i)


    
    same = 1

    while len(strar) < len(arar):
        strar.append(0)
    
    arar.sort()
    strar.sort()
    
    #print(arar, strar)
    
    for i in range(0,len(arar)):
        if arar[i] != strar[i]:
            same = 0
            break

    if same == 1:
        return ssum
    else:
        return 0
 
def growUniqueNumberMultisets(msets, progress, maxNum, amt):
    #recursively produces a list of <amt> integers from 0-<maxNum> where order does not matter.
    #So for g([[]], 0, 2, 2), the list of lists [[]] will have grown to contain [0,0],[0,1],[0,2],[1,1],[1,2],[2,2] (not in this order)
    if progress < maxNum:
        tla = len(msets) 
        for i in range(0,tla):
            tlb = len(msets[i])
            for k in range(1, amt - tlb+1):
                tmp = list(msets[i])
                for j in range(0,k):
                    tmp.append(progress)
                msets.append(tmp)
        growUniqueNumberMultisets(msets, progress+1, maxNum, amt)
        
    if progress == maxNum:
        for i in msets:
            while len(i) < amt:
                i.append(progress)

def main():
	#The strategy: generate all list of possiblities for the digits of a 6-digit number (i.e., 0-6 0's, 0-6 1's, ..., 0-6 9's, and 6 digits only)
    #Then go through this list, for each possibility, checking if an ordering, when converted to an integer k, is equal to the sum of its 
    #digits fifth powers. Then, sum up the k's for each possibility that works. Executes in about .083 seconds, much faster than a brute force approach,
    #which executed in around 6 seconds.
    tic = time()


    numlist = [[]]
    growUniqueNumberMultisets(numlist,0,9,6)
    ssum = 0
    for i in numlist:
        ssum += getFifthPowerSum(i)
    ssum -= 1
    print("Time Elapsed:", time()-tic)
    print(ssum)

main()