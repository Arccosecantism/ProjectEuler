#Problem: (equivalent to) what is the smallest n such that the number of integer partitions of n is divisible by 1,000,000?
from time import time


def getPentagonalNumbers(amt):
    #gets amt generalized pentagonal numbers
    stop = int(amt/2)+1
    if amt%2:
        stop = -stop
    num = 1
    pentagList = []
    while num != stop:
        pentagList.append(int((3*num*num-num)/2))
        
        num = -num
        if num > 0:
            num += 1
        #print(stop,num)    
    return pentagList

def main():
    
    #The strategy: simply generate all partitions of n (mod 1 million) untill one is divisible by 1 million

    #Executes in 32.8 seconds
    t0 = time()
    pentagonList = getPentagonalNumbers(100000)
    print("done")
    partitionList = [1]
    ctr = 1
    val = 1
    sgnTab = [1,1,-1,-1]
    while val != 0:

        actr = 0
        val = 0
        
        while pentagonList[actr] <= ctr:
            val += sgnTab[actr%4]*partitionList[ctr-pentagonList[actr]]
            actr += 1
        
        val = val%1000000
        partitionList.append(val)
        print(ctr)
        ctr+=1
        
    
    print("Time Elapsed:", time()-t0)
    print(ctr-1)
    

main()