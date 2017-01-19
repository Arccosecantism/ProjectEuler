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

def getCombos(numlista, numlistb):
    combos = []
    for i in range(0,len(numlista)):
        for k in range(0,len(numlistb)):
            if isCombo(numlista[i],numlistb[k]):
                combos.append([i,k])

    return combos

def main():
    figurateNumbers = []
    for i in range(3,9):
        figurateNumbers.append(getFigurateNumbersUnderFourDigit(i))
    figCombos = []
    for i in range(0,6):
        figCombos.append([])
        for k in range(0,6):
            if k != i:
                figCombos[-1].append(getCombos(figurateNumbers[i],figurateNumbers[k]))
    
    listIndexes = [[i,1] for i in range(0,6)]
    listIndexes[0] = [0,0]

    lindx = 0
    done = 0
    while not(done):
        for i in range(0,figCombos[lindx]):
            listIndexes[getFigIndex(0,)]

    print(listIndexes)
   # for i in range(0,4):
    #    for k in range(0,4-i)
    for i in figCombos:
        print(i)
        print("^")
                


    

main()
