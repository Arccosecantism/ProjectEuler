import math
from time import time




import math
from time import time

def factorial(x):
    if x == 0 or x == 1:
        return 1
    else:
        return x*factorial(x-1)

def getNumberOfOrders(digar):
    zeros = 0
    for i in digar:
        if i == 0:
            zeros += 1
    bl = len(digar)

    prod = bl-zeros
    for i in range(1,bl):
        prod*=i
    
    sd = list(digar)
    sd.sort()

    reps = [0] * len(digar)
    lastval = -1
    val = -1
    chain = 1
    for i in range(0,len(sd)):
        val = sd[i]
        if lastval == val:
            chain += 1
        else:
            reps[chain-1] += 1
            chain = 1
        lastval = val
    for i in range(0,len(reps)):
        if reps[i]:
            prod /= (factorial(i+1)**reps[i])
    return prod



def getDigitFactorialSumTrue(x, facAr):
    
    ssum = 0
    sx = str(x)
    for i in sx:
        ssum += facAr[int(i)]
    return ssum


def digitFamilyToNum(fam):
 
    ssum = 0
    for k in range(0,len(fam)):
        exp = len(fam)-k-1
        ssum+=(fam[k]*(10**exp))

    return ssum


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
    
def getDigitsStarsBars(stars):
    bars = 10
    proList = [0]*(stars+bars-1)
    nlist = [[i,1] for i in range(0,stars+bars-1)]
    subs = generateSubsets(bars-1, nlist)
    digitLists = []
    for i in subs:
        tl = list(proList)
        for k in i:
            tl[k]=1 
        td = []
        ctr = 9
        
        requireda = False
        requiredb = False
        for k in range(0,len(tl)):
            if tl[k] == 0:
                td.append(ctr)
                if ctr == 1 or ctr == 2 and not(requireda):
                    requireda = True
                if ctr != 0 and not(requiredb):
                    requiredb = True
            else:
                ctr-=1
        if stars == 7:
            if requireda and requiredb:
                digitLists.append(td)
        elif requiredb:
            digitLists.append(td)
    return digitLists


def main():
    
    
    bigAr = []
    for i in range(0,2200001):
       # if not(i%100000):
           
        bigAr.append(getDigitFactorialSumTrue(i, facs))
    print("Long_Array_Done")

    for i in helpArray:
        ctr = 1




    

def main():
    print(getNumberOfOrders([9,1,2,3]))
    longest = 0
    longestVal = 0


    facs = [1]
    for i in range(1,10):
        facs.append(i*facs[-1])
    
    digits = getDigitsStarsBars(6)
    helpArray = []
    for i in range(1,7):
        nd = getDigitsStarsBars(i)
        for j in nd:
            helpArray.append(j)
       # print(helpArray)


    smallAr = []
    for i in range(0,2200001):
        if not(i%10000):
            print (i)
        smallAr.append(0)
    print("Small_Array_Done")

    bigAr = []
    for i in range(0,2200001):
       # if not(i%100000):
           
        bigAr.append(getDigitFactorialSumTrue(i, facs))
    print("Long_Array_Done")


    longVals = []
    for i in range(0,len(helpArray)):
        ctr = 1
        nnum = digitFamilyToNum(helpArray[i])
        end = False
        visitedNumbers = []
        while not(end):
        
            if nnum >= len(bigAr):
                print("bigger?")
                nnum = getDigitFactorialSumTrue(nnum)
            else:
                if smallAr[nnum] == 1:

                    if nnum == 0:
                        print(i,nnum,"Zero?")
                    #print("a",i,nnum,ar[nnum])
                    end = True
                    smallAr[0] = 0
                    for j in visitedNumbers:
                        
                        smallAr[j] = 0
                        #print ("b",i,ar[j])
                    

                else:       
                        #print(nnum)
                        smallAr[nnum] = 1
                        nnum = bigAr[nnum]
                        if nnum == 0:
                            print(i,nnum,"Zero?")
                        visitedNumbers.append(nnum)
                        
                        ctr += 1
    
            
        print(helpArray[i])        
        if ctr == 61:
            longVals.append(helpArray[i])
        if not(i%10000):
            print(i)
    ssum = 0
    for i in longVals:
        ssum += getNumberOfOrders(i)
    print(longVals, ssum)


main()