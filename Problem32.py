#Problem:  What is the sum of all different c's that satisfy this: take the numbers 1-9, arrange them in any order, and put a multiplication sign
#           and an equals sign in between two pairs of numbers such that the reulst is a true multiplication equation a*b=c?


import math
from time import time


def addLists(listlist):
    #combines a list of lists into one list with all the elements
    #for a([[3,4,5],[1,6],[],[0,0]]), the result is [3,4,5,1,6,0,0]
    retlist = []
    for i in range(0,len(listlist)):
        for k in range(0,len(listlist[i])):
            retlist.append(listlist[i][k])
    return retlist

def getOrderings(seed, length, numbers):
    #produces all orderigns of 5 numbers from 1-9 (no duplicates): 
    #[1,9,6,8,3] and [8,4,3,7,2] and [4,8,3,7,2] are three elements of the returned list, for example
    newOrderings = []
    if length > 0:
        npord = []
        for k in numbers:
            tmpList = list(seed)
            tmpList.append(k)
            tmpNumbers = list(numbers)
            tmpNumbers.remove(k)
            #print("a", tmpList, tmpNumbers)
            npord.append(getOrderings(tmpList,length-1,tmpNumbers))
            #print("b", npord)
        newOrderings = addLists(npord)
    else:
        newOrderings.append(seed)
    return newOrderings

def genProduct(intar, spotAfter):
    #takes a 5-element list and where a multiplication sign should go and returns the product
    nstr = ''
    for i in range(0,spotAfter+1):
        nstr += str(intar[i])
    fnum = int(nstr)
    nstr = ''
    for i in range(spotAfter+1, len(intar)):
        nstr += str(intar[i])
    snum = int(nstr)
    prod = fnum*snum
    return prod

def isPandigital(intar, num):
    #Checks if the list and the product contain the digits 1-9 exactly once
    digitList = [0,0,0,0,0,0,0,0,0,0]
    
    for i in intar:
        digitList[i] += 1
    strnum = str(num)
    for i in strnum:
        digitList[int(i)] += 1

    allDigits = 1
    for i in range(1,10):
        if digitList[i] != 1:
            allDigits = 0
            break;

    if digitList[0] != 0:
        allDigits = 0

    return allDigits


def main():
    #The strategy: get all of the possible multipliers, and test all of them if they give a pandigital situation
    # when they are multiplied . Make sure not to count the same product twice. Executes in 1.7-ish seconds.
    t0 = time()
    oneThruNine = [1,2,3,4,5,6,7,8,9]
    lenFpart = 5 
    fpart = getOrderings([],lenFpart,oneThruNine)
    products = []
    #print(genProduct([3,4,5], 0))
    for i in fpart:
        for k in range(0,len(i)-1):
            prod = genProduct(i,k)
            if isPandigital(i,prod) and not(prod in products):
                products.append(prod)

    ssum = sum(products)
    print("Time Elapsed:", time()-t0)
    print(ssum)


main()