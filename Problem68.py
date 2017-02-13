import math
from time import time


def generateSubsetsWeird(siz, numlist):
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
                nextstep = generateSubsetsWeird(siz-1, numlist)
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

def generateCleanSubsets(siz, numlist):
    nlist = []
    for i in numlist:
        nlist.append([i,1])
    badSets = generateSubsetsWeird(siz, nlist)
   
    return badSets

def getPermutations(nlist):
    results = []
    empty = True
    for i in range(0,len(nlist)):
        empty = False
        val = nlist[0]
        del(nlist[0])
        nr = getPermutations(nlist)
        for j in nr:
            results.append(list([val]+j))
        nlist.append(val)
    if empty:
        return [[]]
    else:
        return results

            
def getCyclicalPermutations(nlist):
    cperm = []
    start = nlist[0]
    tnl = nlist[1:]
    nr = getPermutations(tnl)
    for i in nr:
        cperm.append(list([start]+i))
    return cperm

def getSubsetsAddingToN(num,siz,numlist):
    subsets = generateCleanSubsets(siz,numlist)
    goodSubsets = []
    for i in subsets:
        tsum = sum(i)
        if tsum == num:
            goodSubsets.append(list(i))
    return goodSubsets

def getComplement(sl, bl):
    comp = []
    for i in bl:

        dup = False
        for j in sl:
            if i == j:
                dup = True
        if not(dup):
            comp.append(i)
    return comp
def checkRings(inner, outer):

    ssum = outer[0]+inner[0]+inner[1]
    allGood = True
    for i in range(1,5):
        if outer[i]+inner[i]+inner[(i+1)%5] != ssum:
            allGood = False
    
    return allGood


def sortConcatenations(concs):
    smallest = 11
    smallIndex = 0
    for i in range(0,5):
        fd = int(concs[i]/100)
        if fd < smallest:
            smallest = fd
            smallIndex = i
    nconc = ""
    for i in range(0,5):
        nconc += str(concs[(i+smallIndex)%5])
    
    return int(nconc)
        

def main():
    ten_list = [1,2,3,4,5,6,7,8,9,10]
    innerCircleSubsets = []
    for i in range(15, 36, 5):
        innerCircleSubsets += getSubsetsAddingToN(i,5,ten_list[:-1])
    print(innerCircleSubsets)
    innerCircles = []
    for i in innerCircleSubsets:
        innerCircles = list(innerCircles + getCyclicalPermutations(i))
    outerCircles = []
    for i in innerCircles:
        outerCircles.append(getPermutations(getComplement(i,ten_list)))
    
    concs = []
    for i in range(0,len(innerCircles)):
        for k in outerCircles[i]:
            if checkRings(innerCircles[i],k):
                nc = []
                for h in range(0,5):
                    nc.append(int((str(k[h])+str(innerCircles[i][h])+str(innerCircles[i][(h+1)%5]))))
                concs.append(nc)

    nconcs = []
    for i in concs:
        nconcs.append(sortConcatenations(i))

    print(nconcs)
 
    
main()

