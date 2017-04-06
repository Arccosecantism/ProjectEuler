import math
from time import time

def matrixMultiply(ma, mb):
    if len(ma[0]) != len(mb):
        return -1
    pm = []
    for i in range(0,len(ma)):
        pm.append([])
        for j in range(0,len(mb[0])):
            sm = 0
            for k in range(0,len(mb)):
                sm += ma[i][k]*mb[k][j]
            pm[-1].append(sm)
    return [pm]

def main():
    matrixA = [[1,3],[-4,2],[2,2]]
    matrixB = [[0,0,5,4], [1,-4,2,1]]
    print(matrixMultiply(matrixA,matrixB))

main()
