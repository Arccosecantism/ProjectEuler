#Problem: 	Same problem as 82, but you can move in all directions
import math
import os
from time import time

def getNumMatrix():

    #gets the list of numbers from "MatrixFourWayProblem83.txt
    print(os.getcwd())
    f = open("TextFiles\\MatrixFourWayProblem83.txt", 'r')
    lines = f.readlines()
    flines = []
    for i in lines:
        if i[-1] == "\n":
            flines.append(i[:-1])
        else:
            flines.append(i)
    nlines = [[int(i) for i in k.split(",")] for k in flines]
    #for i in nlines:
    #	print(i)
    return nlines

def testIndex(ni, numMatrix):
    #tests if an index is in bounds
    if ni[0] >= len(numMatrix) or ni[0] < 0 or ni[1]>= len(numMatrix[ni[0]]) or ni[1] < 0:
        return (-1,-1)
    return ni
        
def getDownNode(i, k, matrix):
    return testIndex((i+1,k),matrix) 

def getUpNode(i,k,matrix):
    return testIndex((i-1,k),matrix)

def getRightNode(i, k, matrix):
    return testIndex((i,k+1),matrix)

def getLeftNode(i, k, matrix):
    return testIndex((i,k-1),matrix)

def fixNodeNeighbors(i,k,markers,nm,csm):
    #compares a node to its neighbors. If one of it's neighbors cumulative sum values + its actual value is smaller than
    #its current cumulative sum, change the csum accordingly, and mark all the neighbor nodes to be checked later
    dnodes = []
    dnodes.append(getRightNode(i,k,nm))
    dnodes.append(getDownNode(i,k,nm))
    dnodes.append(getLeftNode(i,k,nm))
    dnodes.append(getUpNode(i,k,nm))
    for node in dnodes:
        if node != (-1,-1):
            if csm[node[0]][node[1]] > csm[i][k] + nm[node[0]][node[1]]:
                csm[node[0]][node[1]] = csm[i][k] + nm[node[0]][node[1]]
                markers.add((node[0],node[1]))
    
def initializeCumulativeSumMatrix(nm, csm):
    #this goes through from top left to bottom right, in a diagonal manner, picking a good starting guess
    #for the cumulative sums; it's simply based on the top and left node; whichever is smaller
    csm[0][0] = nm[0][0]
    for i in range(1,len(csm)):
        csm[i][0] = csm[i-1][0]+nm[i][0]
    for k in range(1,len(csm[0])):
        csm[0][k] = csm[0][k-1]+nm[0][k]
    for i in range(1,len(csm)):
        for k in range(1,len(csm)):
            csm[i][k] = min(csm[i][k-1], csm[i-1][k]) + nm[i][k]
def main():
    #The Strategy: This problem can't be solved in the same way as 82 easily. Instead, we consider running cumulative sums.
    #We first generate a matrix with good guesses at the cumulative sums. Then, we fix the cumulative sums, considering all the surrounding cumulative sums.
    #Then we check all the neighbors, as their cumulative sum maybe could be better. We do this until there are no more squares to check. It's sort
    #of a process by decent -- each "fix" reduces the matrix to a more correctly ordered state.
    #Executes in .868 seconds
    t0 = time()
    numberMatrix = getNumMatrix()
    cSumMatrix = []
    for i in range(0,len(numberMatrix)):
        cSumMatrix.append([0]*len(numberMatrix[i]))
    initializeCumulativeSumMatrix(numberMatrix,cSumMatrix)
    fixMarkers = set([])

    for i in range(0,len(cSumMatrix)):
        for k in range(0,len(cSumMatrix[i])):
            fixNodeNeighbors(i,k,fixMarkers,numberMatrix,cSumMatrix)
 
    while len(fixMarkers) != 0:
        ti = fixMarkers.pop()
        fixNodeNeighbors(ti[0],ti[1],fixMarkers,numberMatrix,cSumMatrix)
    minPathSum = cSumMatrix[-1][-1]
    print("Elapsed Time:", time()-t0)
    print(minPathSum)
    


main()
