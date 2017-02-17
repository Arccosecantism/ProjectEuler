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
        val = partList[int(num-pentList[ctr])]
        ms = ctr%4
        if ms == 2 or ms ==3:
            val = -val
        ssum += val
        ctr += 1
    return ssum

def main():
    pentagonList = getPentagonalNumbers(100000)
    #divList = getListSumOfDivisors(200)
    print("done")
    partitionList = [1]
    ctr = 1
    val = 1
    while val%1000000 != 0:
        val = numberOfPartitions(ctr,partitionList,pentagonList)
        #print(val)

        partitionList.append(val)
        ctr+=1
        print(ctr)
    
    print(ctr-1)
    

main()