#Problem: The number, 1406357289, is a 0 to 9 pandigital number because it is made up of each of the digits 0 to 9 in some order, but it also has a rather interesting sub-string divisibility property.

#Let d1 be the 1st digit, d2 be the 2nd digit, and so on. In this way, we note the following:

#d2d3d4=406 is divisible by 2
#d3d4d5=063 is divisible by 3
#d4d5d6=635 is divisible by 5
#d5d6d7=357 is divisible by 7
#d6d7d8=572 is divisible by 11
#d7d8d9=728 is divisible by 13
#d8d9d10=289 is divisible by 17
#Find the sum of all 0 to 9 pandigital numbers with this property.

import math
from time import time

def getAsThreeDigits(x):
    #gets a number as a three-digit digit-list: so g(42) = [0,4,5]
    tdl = [0,0,0]
    tdl[2] = x%10
    tdl[1] = int(x/10)%10
    tdl[0] = int(x/100)%10
    return tdl

def getLastTwoDigits(x):
    #gets the last two digits of a number
    return x%100

def getFirstTwoDigits(x):
    #gets the first two digits of a number
    x = int(x/10)
    while x >= 100:
        x = int(x/10)
        
    return x

def getMissingDigit(digx):
    #finds the missing digit of a 9-long almost pandigital list: so M([1,5,2,4,0,8,9,3,6]) = 7, because 7 wan't included
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
    #checks if a list of digits has no duplicate numbers: so H([2,5,3,3,0]) = 1
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
    #gets a list of multiples of mult under cap as three-digit numbers: so getMultipleList(330,1000) = [330, 660, 990]
    mlist = []
    for i in range(mult,cap,mult):
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