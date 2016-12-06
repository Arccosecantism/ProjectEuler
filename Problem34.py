#Problem: Find the sum of all numbers that can be written as the sum of the fifth powers of their digits. (excluding 1)

import math
from time import time

def getFactorialSum(ar):
    #determines whether an array of integers, when the factorial of the integers are added together,
    #equal some number that uses an ordering of those integers as its digits. Returns 0 if it doesn't; returns the
    #sum of the factorials of the digits if it does.

    factorialList = [1,1,2,6,24,120,720,5040,40320,362880]
    ssum = 0

    for i in ar:
        ssum += factorialList[i]

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
    if len(strar) != len(arar):
        same = 0
    
    if same:
        arar.sort()
        strar.sort()
        
        #print(arar, strar)
        for i in range(0,len(arar)):
            if arar[i] != strar[i]:
                same = 0
                break

    if same:
        print(ssum, arar)
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

def addLists(listlist):
    #combines a list of lists into one list with all the elements
    #for a([[3,4,5],[1,6],[],[0,0]]), the result is [3,4,5,1,6,0,0]
    retlist = []
    for i in range(0,len(listlist)):
        for k in range(0,len(listlist[i])):
            retlist.append(listlist[i][k])
    return retlist

def main():
	#The strategy: generate all list of possiblities for the digits of a 2,3,4,5,6, and 7-digit number
    #Then go through this list, for each possibility, checking if an ordering, when converted to an integer k, is equal to the sum of its 
    #digits' factorials. Then, sum up the k's for each possibility that works. Executes in about .3 seconds
    tic = time()
    
    numlists = []
    for i in range(2,8):
        tmplist = [[]]
       
        growUniqueNumberMultisets(tmplist,0,9,i)
        numlists.append(tmplist)

    #print(numlist)
    ssum = 0
    for i in numlists:
        for k in i:
         ssum += getFactorialSum(k)
    
    print("Time Elapsed:", time()-tic)
    print(ssum)

main()