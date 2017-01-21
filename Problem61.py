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
    if y < x:
        return y
    else:
        return y+1

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

def searchFigurateNumbers(figs, figIndexes, listIndexes, searchStart):

    progress = []
    done = False
    startingPoint = figIndexes[searchStart[0]][searchStart[1]]
    for i in range(0,len(startingPoint])):
        ti = getFigIndex(i,searchStart[0])
        if listIndexes[ti] == 1:
            listIndexes[ti] == 0
            if startingPoint[i] != []:
                for k in startingPoint[i]:
                   nsearch = searchFigurateNumbers(figs, figIndexes, listIndexes,[ti,k])
                   if nsearch != []:
                       progress = nsearch
                       done = True
                       break
                if done:
                    break
    return progress



    
def main():
    figurateNumbers = []
    for i in range(3,9):
        figurateNumbers.append(getFigurateNumbersUnderFourDigit(i))
    figCombos = []
    for i in range(0,6):
        figCombos.append(getCombos(i,figurateNumbers))
    
    listIndexes = [[i,1] for i in range(0,6)]
    listIndexes[0] = [0,0]

    lindx = 0
    done = 0

    print(listIndexes)
   # for i in range(0,4):
    #    for k in range(0,4-i)
    for i in figCombos:
        for k in i:
            print(k)
            print("^")
        print("---")
                


    

main()
