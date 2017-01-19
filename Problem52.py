#Problem: Project euler explains this well: Copy-paste:
#           It can be seen that the number, 125874, and its double, 251748, contain exactly the same digits, 
#           but in a different order.

#           Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x, contain the same digits.


import math
from time import time

def digitListListToNumList(diglistlist):
    #Converts a list of digit-lists to a list of ints
    nlist = []
    for i in diglistlist:
        num = int(''.join(map(str,list(i))))
        nlist.append(num)
    return nlist

def removeDuplicates(lst):
    #gives a new list that removes all duplicates from a list
    #RD([1,3,3,4,3,5,5]) = [1,4,3,5] -- does preserve order, but in a backwards way
    nlist = []
    for i in lst:
        dup = 0
        for k in nlist:
            if i == k:
                dup = 1
                break
        if not(dup):       
            nlist.append(i)
    return nlist


def generateCoreNumbers(length, start):
    #recursively generates all the possible non-first digits of a number that would work
    #This is based on what the first digits of x, 2x, 3x, 4x, 5x, 6x can be
    pos = []
    if length <= 1 or start > 9:
        pos = [[]]
    else:

          
        nextLayerNoSkip = generateCoreNumbers(length-1, start+1)
        for i in nextLayerNoSkip:
            
            pos.append(list([start]+list(i)))

        if start <= 7 and nextLayerNoSkip != [[]]:
            nextLayerSkip = generateCoreNumbers(length-1, start+2)
            for i in nextLayerSkip:
                pos.append(list([start]+list(i)))

    return pos

def generateSubsets(siz, numlist):
    #generates subsets of size <siz> from a list of numbers. This list of numbers is in a weird
    #format that helps the recursion 
    newlist = []
    if siz > 0:
        for i in range(0,len(numlist)):
            if numlist[i][1] == 1 and len(numlist)-i >= siz:
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

def getStartingNumbers(length):
    #Gets the full list of numbers that, in some order, combine to make the a possible number
    snum = []
    if length > 6:
        cores = generateCoreNumbers(6,2)
        numlist = [[x,1] for x in range(0,10)]
        extras = generateSubsets(length-6, numlist)
        
        for i in cores:
            for k in extras:
                tmp = list(list(i)+list(k))
                tmp.sort()
                snum.append(tmp)
        #print(cores, extras, numlist)
        snum = removeDuplicates(snum)
    else:
        snum = generateCoreNumbers(length, 2)
    return snum


def getSpecialIntListPermutations(numlist, sixIssue):
    #Gets all permutations (orderings) of a number list, with a bit of specialization for this problem
    perms = []
    empty = 1
    for i in numlist:
        if i[1] > 0:
            ni = i[0]
            empty = 0
            if not(sixIssue) or (sixIssue and not(ni > 6)):
                i[1] -= 1
                nl = []
                if sixIssue and ni == 6:
                    nl = getSpecialIntListPermutations(numlist, 1)
                else:
                    nl = getSpecialIntListPermutations(numlist, 0)
                for k in nl:
                    perms.append(list([ni]+list(k)))
                i[1] += 1
    if empty:
        perms = [[]]
    return perms

def generatePossibleNumbers(length):
    #Generates all candidate numbers -- Numbers that are under 16666..., have possible digits, etc.
    starters = getStartingNumbers(length)
    reformStart = []
    for i in starters:
        tmp = []
        for k in i:
            if len(tmp) > 0:
                if tmp[-1][0] == k:
                    #print("one")
                    tmp[-1][1] += 1
                else:
                    tmp.append([k,1])
            else:
                tmp.append([k,1])
        reformStart.append(tmp)
    #print(reformStart)
    pos = []
    for i in reformStart:
        perms = getSpecialIntListPermutations(i, 1)
       # print("here", i, perms)
        for k in perms:
            pos.append(list([1]+list(k)))
    dig =  digitListListToNumList(pos)
    retdig = []
    for i in dig:
        if i <= int(math.floor((10**length)/6)):
            retdig.append(i)
    return retdig

def testSameDigits(x,y):
    #Tests if two numbers have the same digits
    lx = list(str(x))
    lx.sort()
    ly = list(str(y))
    ly.sort()
    if lx == ly:
        return 1
    return 0

def testNumber(x):
    #tests a number x to see if x, 2x, 3x, 4x, 5x, and 6x all share the smae digits
    t0 = time()
    mult = 2
    good = 1
    while mult < 7 and good == 1:
        good = testSameDigits(x,mult*x)
        mult += 1
    return good


def main():
    #Strategy: For each amoutn of digits, from 6 to 9, iclusive, generate all possible numbers and then test them.
    #Keep track of the smallest
    # 
    # Executes in .032 seconds 
    t0 = time()
    for dig in range(6,10):
        possibleNums = generatePossibleNumbers(dig)
        smallest = 10**dig
        for i in possibleNums:
            if testNumber(i):
                if i < smallest:
                    smallest = i
        if smallest != 10**dig:
            break

    print("Time Elapsed", time()-t0)
    print(smallest)
main()