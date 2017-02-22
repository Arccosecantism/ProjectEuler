import math
from time import time

def getFigurateNumbersUnderFourDigit(fig):
    #generates all 4-digit <fig>-sided figurate numbers(e.g., fig = 3 is triangular numbers, fig = 4 is squares, fig = 5 is pentagonal, etc.)
    figlist = []
    fd = 1
    sd = fig-2
    ctr = 0
    while ctr < 10000:
        if ctr >= 1000:
            figlist.append(ctr)
        ctr += fd
        fd += sd
    return figlist

def isCombo(x, y):
    #Tells if the last two digits of x is the first two digits of y -- the numbers overlap by 2
    lastTwo = x%100
    firstTwo = int(y/100)
    return (lastTwo == firstTwo)

def getFigIndex(x,y):
    #does something weird that is specified for the recursive search
    if x < y:
        return x
    else:
        return x+1

def getCombos(findex, figRest):
    #searches a list of figurate numbers and, for each element, lists the indices of all the others it is a combonation with

    combos = []
    for i in range(0,len(figRest[findex])):
        combos.append([])
        for j in range(0,len(figRest)):
            if j != findex:
                combos[-1].append([])
                for k in range(0,len(figRest[j])):
                    if isCombo(figRest[findex][i],figRest[j][k]):
                        combos[-1][-1].append(k)
    return combos

def searchFigurateNumbers(figIndexes, listIndexes, searchStart, getBack, osp):
    #This is really confusing -- it does a depth first search through a sort of weird data structure that holds 
    #all of the possible connections between figurate numbers. It runs untill it hits the 6-cycle
    progress = []
    done = False
    final = True
    for i in listIndexes:
        if i:
            final = False

    if final:
        listIndexes[getBack] = 1

    startingPoint = figIndexes[searchStart[0]][searchStart[1]]
    #print(listIndexes)
    for i in range(0,len(startingPoint)):
        ti = getFigIndex(i,searchStart[0])
        if listIndexes[ti] == 1:
            listIndexes[ti] = 0
            if startingPoint[i] != []:
                if final:
                    for k in range(0,len(startingPoint[i])):
                        if osp[0] == ti and osp[1] == startingPoint[i][k]:
                            #print("done")
                            progress = [[startingPoint[i][k],ti]]
                            done = True
                            listIndexes[ti] = 0
                            break
                    if done:
                        break
                else:
                    for k in range(0,len(startingPoint[i])):
                        
                        nsearch = searchFigurateNumbers(figIndexes, listIndexes, [ti,startingPoint[i][k]], getBack, osp)
                        if nsearch != []:
                            progress = list([[startingPoint[i][k],ti]] + nsearch)
                            done = True
                            break
            listIndexes[ti] = 1
            if final:
                listIndexes[ti] = 0
        if done:
            break
            
    return progress



    
def main():
    #The Strategy -- we pregenerate all the connections between 4-digit figurate numbers nad store them in a weird data structure. Then, we
    #try to piece them together in order to find a 6-cycle. Executes in .250 seconds
    t0 = time()
    figurateNumbers = []
    for i in range(3,9):
        figurateNumbers.append(getFigurateNumbersUnderFourDigit(i))
    figCombos = []
    for i in range(0,6):
        figCombos.append(getCombos(i,figurateNumbers))
    
    listIndexes = [1]*6
    listIndexes[0] = 0

    lindx = 0
    done = 0


    fcycle = []
    for i in range(0, len(figCombos[0])):
        ncycle = searchFigurateNumbers(figCombos, listIndexes, [0,i], 0, [0,i])
        if ncycle != []:
            fcycle = ncycle
            break
    
    numCycle = []
    for i in fcycle:
        numCycle.append(figurateNumbers[i[1]][i[0]])

    ssum = sum(numCycle)

    
    print(numCycle, fcycle)
    print("Time Elapsed:", time()-t0)
    print(ssum)    


    

main()
