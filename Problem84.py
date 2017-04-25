#Problem: What is the first, second, and third most common square to land on in Monopoly if you are playing with 
#          two four-sided dice

#           You must consider Chance, Community Chest, and the fact that three doubles in a row lands the player in jail
#           Also, assume that the player pays their jail fee immediately.

import math
from time import time

def matrixMultiply(ma, mb):
    #multiplies two matrices
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
    #does probabilties for landing on Chance or Community Chest
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
    #deals with landing on chance, Community chance, or go to jail
    if square == 2 or square == 17  or square == 33  or square == 7  or square == 22  or square == 36:
        randomCards(prob, square, probRow)
    elif square == 30:
        probRow[10] += prob
    else:
        probRow[square] += prob

def getRollProbability(outcome, sideNum):
    #gets probabilities for rolling two n-sided dice
    return max(0,-abs(outcome-sideNum-1)+sideNum)*1.0/(sideNum**2)

    
def generateSquareMarkovRow(square, sideNum):
    #generates the probabilties from getting from a given square to all other square that are possible to move to
    #assumes that the probability for a triple double in a row is equal to 1/n^3 where n is the side number of the die
    #This is not true, as this allows for two triple doubles to be rolled in a row, which doesn't make sense.
    tripleDoubleProb = sideNum**-3
    nomalRollProb = 1-tripleDoubleProb
    probRow = [0] * 40
    probRow[10] += tripleDoubleProb
    for i in range(2,2*sideNum+1):
        checkEndOfTurnSquares(nomalRollProb*getRollProbability(i,sideNum),(square+i)%40,probRow)
    return probRow

def deepCopyMatrix(ma, mb):
    #copies a matrix without referencing it
    ma = []
    for i in mb:
        ma.append(list(i))
    return ma
    
def main():
    #The Strategy: this is a Markov chain problem. All we do is this: for each square in Monopoly, we calculte the probability
    #of getting to every other square. this generates a large matrix. Then, we raise the matrix to the 100 (should be lim ans n-> inf)
    #to get a very accurate approximation of the actual probabilities of landing on each square. then, we find the three most common. I'm
    #looking at you, Jail, Pennsylvania railroad and Virginia Avenue.
    #executes in 5.18 seconds
    t0 = time()
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
    print("Elapsed Time:", time()-t0)
    print(asq, bsq, csq)


main()
