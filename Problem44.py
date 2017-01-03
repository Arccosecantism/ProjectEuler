import math
from time import time



def isPentagonal(x):
    if pentToIndex(x) == -1:
        return 0
    return 1

def getFirstPentIndex(basePent, sumLength):
    ansNumer = basePent-sumLength-3*int(sumLength*(sumLength-1)/2)
    ansDenom = 3*sumLength
    if ansNumer%ansDenom == 0:
        ans = int(ansNumer/ansDenom)
    else:
        ans = -1
    #print(ans)
    if ans >= 4:
        return int(ans)
    else:
        return -1
def pentToIndex(p):
    retin = -1
    sindx = 1+math.sqrt(24*p+1)
    if sindx == int(sindx):
        if int(sindx)%6 == 0:
            retin = int(int(sindx)/6)
    if retin <= 0:
        retin = -1
    return retin
    
def main():
    t0 = time()

    ctr = 1
    found = 0
    basePent = 1
    #pentagonList = getPentList(100000)
    print(pentToIndex(5), pentToIndex(70), pentToIndex(4), pentToIndex(6), pentToIndex(69), pentToIndex(71), pentToIndex(2))
   # print(pentagonList)
    pi = 0
    pk = 0
    print("got40")
    while not(found):
        #print(ctr)
        basePent = int(ctr*(3*ctr-1)/2)
        minran = basePent%3
        if minran == 0:
            minran = 3
            
        maxran = int(math.ceil(math.sqrt(2.0*basePent/3.0+25.0/36.0)-5.0/6.0))+1
        #print(maxran, minran, 2.0*basePent/3.0+25.0/36.0, basePent)
        for i in range(minran,maxran,3):
            firstidx = getFirstPentIndex(basePent, i)
            if firstidx >= 1:
                firstPent = int(firstidx*(3*firstidx-1)/2)
                secondPent = basePent + firstPent
                sumPent = secondPent + firstPent
                #print("Okay:", basePent, ctr, i, firstPent, secondPent, sumPent)
                if isPentagonal(sumPent):
                   
                   # print("Done", pi, pk, basePent, firstPent, secondPent, sumPent)
                    found = 1
        ctr +=1



    print("Time Elapsed:", time()-t0)
    print(basePent)
main()