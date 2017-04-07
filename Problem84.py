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
    return pm

def randomCards(prob, cardSquare, probRow):
    
    one_sixteenth = 1.0/16
    probRow[0] += prob*one_sixteenth
    probRow[10] += prob*one_sixteenth
    if cardSquare == 2:
        probRow[2] += 14*prob*one_sixteenth
    elif cardSquare == 17:
        probRow[17] += 14*prob*one_sixteenth
    elif cardSquare == 33:
        probRow[33] += 14*prob*one_sixteenth
    else:
        probRow[11] += prob*one_sixteenth
        probRow[24] += prob*one_sixteenth
        probRow[39] += prob*one_sixteenth
        probRow[5] += prob*one_sixteenth
        if cardSquare == 7:
            probRow[15] += 2*prob*one_sixteenth
            probRow[12] += prob*one_sixteenth
            probRow[4] += prob*one_sixteenth
            probRow[7] += 6*prob*one_sixteenth
        elif cardSquare == 22:
            probRow[25] += 2*prob*one_sixteenth
            probRow[28] += prob*one_sixteenth
            probRow[19] += prob*one_sixteenth
            probRow[22] += 6*prob*one_sixteenth
        elif cardSquare == 36:
            probRow[5] += 2*prob*one_sixteenth
            probRow[12] += prob*one_sixteenth
            randomCards(prob*one_sixteenth, 33, probRow)
            probRow[36] += 6*prob*one_sixteenth

def checkEndOfTurnSquares(prob, square, probRow):
    if square == 2 or square == 17  or square == 33  or square == 7  or square == 22  or square == 36:
        randomCards(prob, square, probRow)
    elif square == 30:
        probRow[10] += prob
    else:
        probRow[square] += prob

def getRollProbability(outcome, sideNum):
    return max(0,-abs(outcome-sideNum-1)+sideNum)*1.0/(sideNum**2)

    
def generateSquareMarkovRow(square, sideNum):
    tripleDoubleProb = sideNum**-3
    nomalRollProb = 1-tripleDoubleProb
    probRow = [0] * 40
    probRow[10] += tripleDoubleProb
    for i in range(2,2*sideNum+1):
        checkEndOfTurnSquares(nomalRollProb*getRollProbability(i,sideNum),(square+i)%40,probRow)
    return probRow

def deepCopyMatrix(ma, mb):
    ma = []
    for i in mb:
        ma.append(list(i))
    return ma
    
def main():
    sideNum = 3
    monopolyMatrix = []
    #print(generateSquareMarkovRow(0,6))
    for i in range(0,40):
        monopolyMatrix.append(generateSquareMarkovRow(i,sideNum))
    #print(monopolyMatrix)
    limAmt = 100
    resMat = []
    resMat = deepCopyMatrix(resMat, monopolyMatrix)
    #print(resMat)
    for i in range(0,limAmt):
        resMat = matrixMultiply(resMat,monopolyMatrix)

    alik = 0
    asq = -1
    for i in range(len(resMat[0])):
        if resMat[0][i] > alik:
            alik = resMat[0][i]
            asq = i

    blik = 0
    bsq = -1
    for i in range(len(resMat[0])):
        if resMat[0][i] > blik and resMat[0][i] < alik:
            blik = resMat[0][i]
            bsq = i

    clik = 0
    csq = -1
    for i in range(len(resMat[0])):
        if resMat[0][i] > clik and resMat[0][i] < blik:
            clik = resMat[0][i]
            csq = i
    print(asq, bsq, csq)


main()
