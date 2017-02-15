import math
from time import time


def getListSumOfDivisors(cap):
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
    ssum = 0
    ctr = 0
    
    while pentList[ctr] <= num:
        val = partList[num-pentList[ctr]]
        ms = ctr%4
        if ms == 2 or ms ==3:
            val = -val
        ssum += val
        ctr += 1
    return ssum

def main():
    pentagonList = getPentagonalNumbers(1000000)
    #divList = getListSumOfDivisors(200)
    partitionList = [1]
    for i in range(1,100001):
        partitionList.append(numberOfPartitions(i,partitionList,pentagonList))
    
    done = False
    for i in range(0,len(partitionList)):
        if not(partitionList[i]%1000000) and done == False:
            print(i)
    

main()