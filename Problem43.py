
import math
from time import time

def getAsThreeDigits(x):
    tdl = [0,0,0]
    tdl[2] = x%10
    tdl[1] = int(x/10)%10
    tdl[0] = int(x/100)%10
    return tdl

def getLastTwoDigits(x):
    return x%100

def getFirstTwoDigits(x):
    x = int(x/10)
    while x >= 100:
        x = int(x/10)
        
    return x

def getMissingDigit(digx):
 
    digar = []
    #print(digx)
    for i in range(0,10):
        digar.append(0)
    for i in digx:
        digar[i] += 1
    #print(digar)
    md = -2
    for i in range(0,len(digar)):
        if digar[i] == 0 and md == -2:
            md = i
        elif digar[i] == 0 and md != -2:
            md = -1
    return md

def hasNoDuplicateDigit(digx):
    digar = []
    for i in range(0,10):
        digar.append(0)
    for i in digx:
        digar[i] += 1
    nodupes = 1
    for i in digar:
        if i >= 2:
            nodupes = 0
    return nodupes

def getMultipleList(mult, cap):
    mlist = []
    for i in range(0,cap):
        if not(i%mult):
            mlist.append(getAsThreeDigits(i))
    return mlist

def getOverlaps(nums_a, nums_b):
    overlaps = []
    for i in nums_a:
        for k in nums_b:
            if i[:2] == k[len(k)-2:len(k)]:
                #print("overlap", k, i)
                connum = list(k+i[2:])
                #print("combine:", connum)
                if hasNoDuplicateDigit(connum):
                    overlaps.append(connum)
    return overlaps

def constructNumber(digx):
    missingDigit = getMissingDigit(digx)
    #print("here", missingDigit)
    num = 0
    if missingDigit >= 0 and missingDigit <= 9:
        num = int(''.join(map(str,digx)))
        num += missingDigit * 1000000000
    return num
            

def main():
    t0 = time()
    primeList = [2,3,5,7,11,13,17]
    primeMultipleList = []
    for i in primeList:
        multList = getMultipleList(i,1000)
        nodupes = []
        for j in multList:
            if hasNoDuplicateDigit(j):
                nodupes.append(j)
        primeMultipleList.append(nodupes)
    
    #for i in range(0,1001):
     #   print(getFirstTwoDigits(i))
    #print(primeMultipleList[-1],primeMultipleList[-2])
    baseList = list(primeMultipleList[-1])
    for i in range(1,len(primeMultipleList)):
        overlaps = getOverlaps(baseList, primeMultipleList[len(primeMultipleList)-i-1])
        baseList = list(overlaps)
        #print(baseList, "\n")
    
    ssum = 0
    for i in baseList:
        ssum += constructNumber(i)
        print(constructNumber(i))

    
    print("Time Elapsed:", time()-t0)
    print(ssum)
main()