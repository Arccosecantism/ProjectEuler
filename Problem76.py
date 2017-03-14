#Problem: How many ways are there to write 100 as the sum of wo of more natural numbers (excluding 0)?

import math
from time import time


def getListSumOfDivisors(cap):
    #
    cap = max(2,cap)
    sodList = [0]*cap
    sodList[0] = 0
    sodList[1] = 1
    for i in range(2,cap):
        ssum = 1+i
        ub = int(i/2)+1
        for k in range(2,ub):
            if not(i&k):
                ssum += k
        sodList[i] = ssum
    return sodList

def getPentagonalNumbers(amt):
    #returns an amt-long list of the first generalized pentagonal numbers (numbers of the form n(3n-1)/3 )
    stop = int(amt/2)+1
    if amt%2:
        stop = -stop
    num = 1
    pentagList = []
    while num != stop:
        pentagList.append((3*num*num-num)/2)
        
        num = -num
        if num > 0:
            num += 1
        #print(stop,num)    
    return pentagList



def numberOfPartitions(num, partList, pentList):
    #tells the number of partitions of n, based on previous values;
    #some research shows that P(n) = P(n-1)+P(n-2)-P(n-5)-P(n-7)+P(n-12)
    #                                  + P(n-15) - P(n-22) ... ++/-- P(n-k(3k-1)/3) until k(3k-1)/3 = n
    #this is highly non-intuitive and makes little sense
    ssum = 0
    ctr = 0
    
    while pentList[ctr] <= num:
        val = partList[int(num-pentList[ctr])]
        ms = ctr%4
        if ms == 2 or ms ==3:
            val = -val
        ssum += val
        ctr += 1
    return ssum

def main():
    #The strategy: we generate a lot of pentagonal numbers and a list of partition values of n. We simply 
    #keep building up the list until we reach 100. then subtract 1, as one ofthe partitions of 100 is simply 100

    #Executes in .002 seconds
    t0 = time()
    pentagonList = getPentagonalNumbers(1000)
    #divList = getListSumOfDivisors(200)
    partitionList = [1]
    for i in range(1,101):
        partitionList.append(numberOfPartitions(i,partitionList,pentagonList))
    print("Time Elapsed:", time()-t0)
    print(partitionList[-1]-1)
    

main()