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
    f = open("TextFiles\\MatrixThreeWayProblem82.txt", 'r')
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
	
def minList(numlist):
    minVal = numlist[0]
    for i in numlist:
        if i < minVal:
            minVal = i
    return minVal

def testIndex(ni, numMatrix, blockMatrix):
    if ni[0] >= len(numMatrix) or ni[0] < 0 or ni[1]>= len(numMatrix[ni[0]]) or ni[1] < 0:
        return [ni, 0]
    elif blockMatrix[ni[0]][ni[1]] == True:
        return [ni, 1]
    return [ni,2]
        
def getDownNode(i, k, matrix, blockMatrix):
    #gets the coordinates of the lower node
    #print(i+1,k)
    #for j in blockMatrix:
    #   print(j)
    #print(i+1, k, blockMatrix)
    return testIndex([i+1,k],matrix, blockMatrix) 

def getUpNode(i,k,matrix, blockMatrix):
    return testIndex([i-1,k],matrix, blockMatrix)

def getRightNode(i, k, matrix, blockMatrix):
    #gets the coordinates of the right child (straight right)
    #print(i,k+1)
    #for j in blockMatrix:
    #   print(j)
    #print(i+1, k, blockMatrix)
    return testIndex([i,k+1],matrix, blockMatrix)

def getLeftNode(i, k, matrix, blockMatrix):
    return testIndex([i,k-1],matrix,blockMatrix)

def findLeastSumBlocked(i, k, numMatrix, bsumMatrix, blockMatrix, msum, csum):
    #recursively finds the greatest sum: it looks at the sums in [i][k]'s two children 
    #and picks the bigger one and adds its value to it to figure out its own max sum
    #If the children don't know their sum, recurse once on each child.
    #So it's not total brute-force: it remembers values that it has already calculated
    if i >= 0 and i < len(numMatrix) and k >= 0 and k < len(numMatrix[i]):
        #print(i,k)
        blockMatrix[i][k] = True
        csum += numMatrix[i,k]
        #for j in blockMatrix:
        #    print(j)
        #print("")
        #for j in bsumMatrix:
        #   print(j)
        #print("--")
        
        if bsumMatrix[i][k] == 0:

            if (k == len(numMatrix[-1])-1):
                bsumMatrix[i][k] = numMatrix[i][k]

            else:
                dirNodes = []
                testDirNodes = [[-1,-1],[-1,-1],[-1,-1],[-1,-1]]
                dlen = len(testDirNodes)

                testDirNodes[0] = getDownNode(i,k,numMatrix,blockMatrix,msum,csum)
                testDirNodes[1] = getRightNode(i,k,numMatrix,blockMatrix,msum,csum)
                testDirNodes[2] = getUpNode(i,k,numMatrix,blockMatrix,msum,csum)
                testDirNodes[3] = getDownNode(i,k,numMatrix,blockMatrix,msum,csum)

                for j in range(dlen):
                    if testDirNodes[j][1] == 0:
                        dirNodes.append([-1,-1])
                    elif testDirNodes[j][1] == 1:
                        dirNodes.append([-1,-1])
                        #toUnblock.append(testDirNodes[j][0])
                    elif testDirNodes[j][1] == 2:
                        dirNodes.append(testDirNodes[j][0])


                #if k == 0:
                #    dirNodes[0] = [-1,-1]
                #   dirNodes[2] = [-1,-1]
                #print(i,k,dirNodes)
                for j in dirNodes:
                    if j != [-1,-1]:
                        findLeastSumBlocked(j[0],j[1],numMatrix,bsumMatrix,blockMatrix)
                
                #print("see",dirNodes[1])

                for j in dirNodes:
                    if j != [-1,-1]:
                        blockMatrix[j[0]][j[1]] = False


                dirVals = [-1,-1,-1]
                for j in range(0,dlen):
                    if dirNodes[j] != [-1,-1]:
                        dirVals[j] = bsumMatrix[dirNodes[j][0]][dirNodes[j][1]]
                        if dirVals[j] == -1:
                            bsumMatrix[dirNodes[j][0]][dirNodes[j][1]] = 0

                blocked = True
                mtl = []
                for j in dirVals:
                    if j != -1:
                        blocked = False
                        mtl.append(j)
                if blocked:
                    bsumMatrix[i][k] = -1
                else:
                    #print(i,k,mtl, dirNodes, dirVals)
                    minVal = minList(mtl)
                    bsumMatrix[i][k] = numMatrix[i][k]+minVal

    else:
        print("ERROR:", i,k, len(numMatrix), len(numMatrix[i]))
        #print((i >= 0 and i < len(numMatrix) and k >= 0 and k < len(numMatrix[i])))

def resetBlockedSumMatrixCollumn(bsm, tsm, bkm, col, head):
    for i in range(head,len(tsm)):
        bsm[i][col] = tsm[i][col]
        bkm[i][col] = False

'''def resetBlockedMatrix(bsm):
    for a in range(len(bsm)):
        for b in range(len(bsm[a])):
            bsm[a][b] = False'''


def main():
	#see findGreatestSum for algorithm -- main simply calls it and prints the answer. THe way I solved the problem the first time
	#worked for this problem, because I used some caching -- the program remembered previously calculated sums
	#Executes in .09 seconds
    t0 = time()
    numberMatrix = getNumMatrix()
    pathMatrix = []
    backtrackMatrix = []
    blockedPathMatrix = []

    for i in range(0,len(numberMatrix)):
        backtrackMatrix.append([])
        pathMatrix.append([])
        blockedPathMatrix.append([])
        for j in range(0,len(numberMatrix[i])):
            backtrackMatrix[-1].append(False)
            pathMatrix[-1].append(0)
            blockedPathMatrix[-1].append(0)
	#pathMatrix[3][1] = 2


    
    for i in range(0,len(numberMatrix)):
        pathMatrix[i][-1] = numberMatrix[i][-1]
    resetBlockedSumMatrixCollumn(blockedPathMatrix, pathMatrix, backtrackMatrix, len(numberMatrix)-1, 0) 
    for j in range(1,len(numberMatrix[0])+1):
        tj = len(numberMatrix[0])-j
        for i in range(0,len(numberMatrix)):
            findLeastSumBlocked(i,tj, numberMatrix, blockedPathMatrix, backtrackMatrix)
            pathMatrix[i][tj] = blockedPathMatrix[i][tj] 
            resetBlockedSumMatrixCollumn(blockedPathMatrix, pathMatrix, backtrackMatrix, tj, i) 
    
    smallestSum = pathMatrix[0][0]
    for i in range(0,len(pathMatrix)):
        if pathMatrix[i][0] < smallestSum:
            smallestSum = pathMatrix[i][0]
        
    print("Time Elapsed:", time()-t0)
    '''for i in numberMatrix:
        print(i)
    print("")
    for i in pathMatrix:
        print(i)
    print("")
    for i in backtrackMatrix:
        print(i)
    print("")'''
    print(smallestSum)
	
main()


