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
    f = open("TextFiles\\MatrixThreeWayProblem82Test2.txt", 'r')
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

def getDownNode(i, k, matrix, blockMatrix):
    #gets the coordinates of the lower node
    #print(i+1,k)
    #for j in blockMatrix:
    #   print(j)
    #print(i+1, k, blockMatrix)
    if i+1 >= len(matrix) or i < 0:
        return [-1,-1]
    elif k >= len(matrix[i]) or k < 0:
        return [-1,-1]
    elif blockMatrix[i+1][k] == True:
        return [-1,-1]
    
    return [i+1, k] 

def getUpNode(i,k,matrix, blockMatrix):
    if i-1 >= len(matrix) or i-1 < 0:
        return [-1,-1]
    elif k >= len(matrix[i]) or k < 0:
        return [-1,-1]
    elif blockMatrix[i-1][k] == True:
        return [-1,-1]
    return [i-1,k]

def getRightNode(i, k, matrix, blockMatrix):
    #gets the coordinates of the right child (straight right)
    #print(i,k+1)
    #for j in blockMatrix:
    #   print(j)
    #print(i+1, k, blockMatrix)
    if i >= len(matrix) or i < 0:
        return [-1,-1]
    elif k+1 >= len(matrix[i]) or k < 0:
        return [-1,-1]
    elif blockMatrix[i][k+1] == True:
        return [-1,-1]
    return [i, k+1] 

def findLeastSum(i, k, numMatrix, sumMatrix, blockMatrix):
    #recursively finds the greatest sum: it looks at the sums in [i][k]'s two children 
    #and picks the bigger one and adds its value to it to figure out its own max sum
    #If the children don't know their sum, recurse once on each child.
    #So it's not total brute-force: it remembers values that it has already calculated
    if i >= 0 and i < len(numMatrix) and k >= 0 and k < len(numMatrix[i]):
        #print(i,k)
        blockMatrix[i][k] = True

        if sumMatrix[i][k] == 0:

            if (k == len(numMatrix[-1])-1):
                sumMatrix[i][k] = numMatrix[i][k]

            else:

                dirNodes = [[-1,-1],[-1,-1],[-1,-1]]
                dlen = len(dirNodes)

                dirNodes[0] = getDownNode(i,k,numMatrix,blockMatrix)
                dirNodes[1] = getRightNode(i,k,numMatrix,blockMatrix)
                
                dirNodes[2] = getUpNode(i,k,numMatrix,blockMatrix)
                #if k == 0:
                #    dirNodes[0] = [-1,-1]
                #   dirNodes[2] = [-1,-1]
                print(i,k,dirNodes)
                for j in dirNodes:
                    if j != [-1,-1]:
                        findLeastSum(j[0],j[1],numMatrix,sumMatrix,blockMatrix)
                
                print("see",dirNodes[1])

                for j in dirNodes:
                    blockMatrix[j[0]][j[1]] = False

                dirVals = [-1,-1,-1]
                for j in range(0,dlen):
                    if dirNodes[j] != [-1,-1]:
                        dirVals[j] = sumMatrix[dirNodes[j][0]][dirNodes[j][1]]
                        if dirVals[j] == -1:
                            sumMatrix[dirNodes[j][0]][dirNodes[j][1]] = 0

                blocked = True
                mtl = []
                for j in dirVals:
                    if j != -1:
                        blocked = False
                        mtl.append(j)
                if blocked:
                    sumMatrix[i][k] = -1
                else:
                    #print(i,k,mtl, dirNodes, dirVals)
                    minVal = minList(mtl)
                    sumMatrix[i][k] = numMatrix[i][k]+minVal

    else:
        print("ERROR:", i,k, len(numMatrix), len(numMatrix[i]))
        #print((i >= 0 and i < len(numMatrix) and k >= 0 and k < len(numMatrix[i])))


def main():
	#see findGreatestSum for algorithm -- main simply calls it and prints the answer. THe way I solved the problem the first time
	#worked for this problem, because I used some caching -- the program remembered previously calculated sums
	#Executes in .09 seconds
    t0 = time()
    numberMatrix = getNumMatrix()
    pathMatrix = []
    backtrackMatrix = []

    for i in range(0,len(numberMatrix)):
        backtrackMatrix.append([])
        pathMatrix.append([])
        for j in range(0,len(numberMatrix[i])):
            backtrackMatrix[-1].append(False)
            pathMatrix[-1].append(0)
	#pathMatrix[3][1] = 2

    smallestSum = 0
    findLeastSum(0,0,numberMatrix, pathMatrix,backtrackMatrix)
    smallestSum = pathMatrix[0][0]
    for i in range(1,len(numberMatrix)):
        findLeastSum(i,0,numberMatrix, pathMatrix,backtrackMatrix)
        nft = pathMatrix[i][0]
        if nft < smallestSum:
            smallestSum = nft
        for a in range(len(backtrackMatrix)):
            for b in range(len(backtrackMatrix[a])):
                backtrackMatrix[a][b] = False
    print("Time Elapsed:", time()-t0)
    for i in numberMatrix:
        print(i)
    print("")
    for i in pathMatrix:
        print(i)
    print("")
    for i in backtrackMatrix:
        print(i)
    print("")
    print(smallestSum)
	
main()


