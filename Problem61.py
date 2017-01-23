import math
from time import time

def getFigurateNumbersUnderFourDigit(fig):
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
    lastTwo = x%100
    firstTwo = int(y/100)
    return (lastTwo == firstTwo)

def getFigIndex(x,y):
    if x < y:
        return x
    else:
        return x+1

def getCombos(findex, figRest):
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
        #print("here_A")
        ti = getFigIndex(i,searchStart[0])
        if listIndexes[ti] == 1:
           # print("here_B")
            listIndexes[ti] = 0
            if startingPoint[i] != []:
               # print("here_C")
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
                    #print("here_D")
                    for k in range(0,len(startingPoint[i])):
                        
                        nsearch = searchFigurateNumbers(figIndexes, listIndexes, [ti,startingPoint[i][k]], getBack, osp)
                        if nsearch != []:
                            #print(i,k, startingPoint)
                            #print(startingPoint[i][k])
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
