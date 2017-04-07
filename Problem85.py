import math
from time import time

def getTriangleNumbers(cap):
    triList = []
    num = 0
    fd = 0
    sd = 1
    while num < cap:
        triList.append(num)
        fd += sd
        num += fd
    return triList

def main():
    maxProd = 2130000
    minProd = 1970000
    closeGuesses = []
    sqnum = 0
    for i in range(1,2100):
        sqnum = 0
        kctr = 0
        while sqnum < maxProd and kctr < i-1:
            kctr += 1
            sqnum = (i*kctr*(i+1)*(kctr+1))/4
            if sqnum > minProd:
                closeGuesses.append((sqnum,i*kctr,i,kctr))
    closestDif = 200000
    closestArea = 0
    for i in closeGuesses:
        if abs(i[0]-2000000) < closestDif:
            closestDif = abs(i[0]-2000000)
            closestArea = i[1]
            
    print(closestArea)

main()