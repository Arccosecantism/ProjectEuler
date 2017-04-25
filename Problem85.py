
#Problem: What is the area of the rectagnle that, when tiled with unit squares, contains the closest to
#           2 million rectangles if you consider any amount of squares
import math
from time import time

def getTriangleNumbers(cap):
    #generates a list of triangle numbers
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
    #The strategy: the number of rectangels in an n by m rectangel tiled with unit squares is n(n+1)/2*m(m+1)/2
    #we establish a min and max value by simply checking some triangle numbers on the calculator so we can get close to 2 million
    #Then, we simply check all triangles numbers and record the ones that fall in the range.
    #Then, we pick the one with the smallest distance from 2 million and derive the area.
    #Executes in .0312 seconds
    t0 = time()
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
    print("Elapsed Time:", time()-t0)
    print(closestArea)

main()