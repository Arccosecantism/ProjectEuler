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
    #simply calls generateSubsetsWeird but the numlist is easier: [5,6,7,8] is an acceptable input,
    #and it gets translated to [[5,1],[6,1],[7,1],[8,1]]
    nlist = []
    for i in numlist:
        nlist.append([i,1])
    badSets = generateSubsetsWeird(siz, nlist)
   
    return badSets

def generateDiceArrangements():
    return generateCleanSubsets(6,[0,1,2,3,4,5,6,7,8,9])

def testTwoDice(da, db):
    squares = [(0,1),(0,4),(0,9),(1,6),(2,5),(3,6),(4,9),(6,4),(8,1)]
    sats = []
    for i in range(0,9):
        sats.append(set([]))
    for i in da:
        for j in range(0,len(squares)):
            for b in range(0,2):
                #print(i,squares[j][b])
                if (i == 6 or i == 9) and (squares[j][b] == 6 or squares[j][b] == 9):
                    #print("nine")
                    sats[j].add((0,b))
                    
                elif i == squares[j][b]:
                    #print("norm")
                    sats[j].add((0,b))
                #print(sats[j])
                #print("---")

    for i in db:
        for j in range(0,len(squares)):
            for b in range(0,2):
                
                if (i == 6 or i == 9) and (squares[j][b] == 6 or squares[j][b] == 9):
                    sats[j].add((1,b))
                elif i == squares[j][b]:
                    sats[j].add((1,b))
    #print(sats)
    good = 1
    for i in sats:
        if good:
            if not(((1,0) in i and (0,1) in i) or ((0,0) in i and (1,1) in i)):
                good = 0

    return good
def main():
    diceA = generateDiceArrangements()
    diceB = list(diceA)
    print(testTwoDice([0, 1, 2, 3, 4, 5], [0, 1, 2, 4, 5, 6]))
    ssum  = 0
    for i in range(0,len(diceA)):
        for j in range(i,len(diceB)):
            #print(i,j)
            ssum += testTwoDice(diceA[i],diceB[j])
    print(ssum)

main()
