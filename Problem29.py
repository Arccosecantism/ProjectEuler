
#Problem: 	When you create a spiral of numbers: like 
#                    21 22 23 24 25
#                    20 7  8  9  10
#                    19 6  1  2  11
#                    18 5  4  3  12
#                    17 16 15 14 13
#           what is the sum of the numbers on the diagonals when the size of the spiral is 1001 by 1001?
#           (for 5, as shown, the sum of the diagonals is 1 + 3 + 5 + 7 + 9 + 13 + 17 + 21 + 25 = 101)

import math
from time import time

def getNonPowers(x):
    ar = []
    npar = []
    for i in range(1,x):
        ar.append([i+1, 0])
    for i in range(0,x-1):
        if ar[i][1] == 0:
            npar.append(i+2)
            for k in range(i+1,x-1):
                if math.log(k+2, i+2) == int(math.log(k+2, i+2)): 
                   # print(k+2, i+2)
                    ar[k][1] = 1
    return npar

def genPowersUnder(base, cap):
    par = []
    product = base
    while product <= cap:
         par.append(product)
         product *= base
    return par

def getGoodFactors(x):
    flist = []
    ctr = 2
    done = 0
    while not(done):
        if not(x%ctr):
            sf = ctr
            bf = int(x/ctr)
            if sf < bf:
                flist.append(sf)
                flist.append(bf)
            elif sf == bf:
                flist.append(sf)
            else:
                done = 1
        ctr += 1

    return flist

def findColsInFamily(fam, cap):
    powers = genPowersUnder(fam, cap)
    familyArray = []
    maxExp = len(powers)
    for i in powers:
        familyArray.append([])
        for k in range(2,cap+1):
            familyArray[-1].append([i,k,0])
    
    for i in range(0, len(familyArray) - 1):
        for k in familyArray[i]:
            if k[2] == 0:
                factors = getGoodFactors(k[1])
                for j in factors:
                    if j <= maxExp and j-1+i < len(familyArray):
                        #print(i, k, j, int(k[1]/j), familyArray[j-1+i][int(k[1]/j)-2])
                        familyArray[j-1+i][int(k[1]/j)-2][2] = 1
                        #print(familyArray[j-1+i][int(k[1]/j)-2])
    total = 0
    for i in familyArray:
        for k in i:
            #print(k)
            if k[2] == 1:
                
                total += 1
    return total

def main():
    #This is quite easy -- the diagonals are sums of odd squares minus a multiple of 2, which is (2n-1)(2n)(2n+1)/6
    #We jsut count up the square sums and subtract off the multiples of 2, and subtract 3 because having one 1 in the center 
    #is weird and throws things off. Takes 0.0 seconds to execute
    tic = time()
    num = 100
    uniques = (num-1)*(num-1)
    nonPowers = getNonPowers(num) 
    for i in nonPowers:
        if i <= int(math.ceil(math.sqrt(num))):
           uniques -= findColsInFamily(i,num) 
    print("Time Elapsed: ", time() - tic)
    print(uniques)

main()