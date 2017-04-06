#Problem: 	Find the "path" (moving only down or down-right) in the trignle in "TriangleProblem67.txt" 
#			that has the maximum sum compared to all other paths. What is this sum? (It might help to look at https://projecteuler.net/problem=18)
#		
#			This problem is almopst exactly the same as problem 18, except the triangle I have to search is much bigger, so I can't check every path -- I 
#			need a better algorithm
import math
import os
from time import time

def getNumMatrix():

    #gets the list of numbers from "TriangleProblem67.txt"
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
	
def minu(a,b):
    if a < 0 and b < 0:
        if a > b:
            return a
        else:
            return b
    elif a < 0:
        return b
    elif b < 0:
        return a
    else:
        if a > b:
            return b
        else:
            return a

def testIndex(ni, numMatrix,):
    if ni[0] >= len(numMatrix) or ni[0] < 0 or ni[1]>= len(numMatrix[ni[0]]) or ni[1] < 0:
        return [-1,-1]
    return ni
        
def getDownNode(i, k, matrix):
    return testIndex([i+1,k],matrix) 

def getUpNode(i,k,matrix):
    return testIndex([i-1,k],matrix)

def getRightNode(i, k, matrix):
    return testIndex([i,k+1],matrix)

def getLeftNode(i, k, matrix):
    return testIndex([i,k-1],matrix)

def fixNodeNeighbors(i,k,markers,nm,csm):
    dnodes = []
    dnodes.append(getRightNode(i,k,nm))
    dnodes.append(getDownNode(i,k,nm))
    dnodes.append(getLeftNode(i,k,nm))
    dnodes.append(getUpNode(i,k,nm))
    for node in dnodes:
        if node != [-1,-1]:
            if csm[node[0]][node[1]] > csm[i][k] + nm[node[0]][node[1]]:
                csm[node[0]][node[1]] = csm[i][k] + nm[node[0]][node[1]]
                markers.add((node[0],node[1]))
    #markers.discard((i,k))




    
def initializeCumulativeSumMatrix(nm, csm):
    csm[0][0] = nm[0][0]
    for i in range(1,len(csm)):
        csm[i][0] = csm[i-1][0]+nm[i][0]
    for k in range(1,len(csm[0])):
        csm[0][k] = csm[0][k-1]+nm[0][k]
    for i in range(1,len(csm)):
        for k in range(1,len(csm)):
            csm[i][k] = minu(csm[i][k-1], csm[i-1][k]) + nm[i][k]
def main():
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
