#Problem: 	Find the "path" (moving only down or right) in the 80x80 number matrix in "MatrixTwoWayProblem81.txt" that has the minimum sum of contained nodes
import math
import os
from time import time

def getNumMatrix():

	#gets the number matrix from "MatrixTwoWayProblem81.txt"
	print(os.getcwd())
	f = open("TextFiles\\MatrixTwoWayProblem81.txt", 'r')
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
	
def getDownNode(i, k, matrix):
	#gets the coordinates of the lower node
	if i+1 >= len(matrix) or i < 0:
		return [-1,-1]
	elif k >= len(matrix[i]) or k < 0:
		return [-1,-1]
	return [i+1, k] 

def getRightNode(i, k, matrix):
	#gets the coordinates of the right child (straight right)
	if i >= len(matrix) or i < 0:
		return [-1,-1]
	elif k+1 >= len(matrix[i]) or k < 0:
		return [-1,-1]
	return [i, k+1] 

def findSmallestSum(i, k, numMatrix, sumMatrix):
	#recursively finds the smallest sum: it looks at the sums in [i][k]'s two children 
	#and picks the one with the smaller min path sum and adds its matrix value to it to figure out its own min sum
	#If the children don't know their sum, recurse once on each child.
	#So it's not total brute-force: it remembers values that it has already calculated
	
	if i >= 0 and i < len(numMatrix) and k >= 0 and k < len(numMatrix[i]):

		if sumMatrix[i][k] == 0:
			if i == len(numMatrix) - 1 and k == len(numMatrix[-1])-1:
				sumMatrix[i][k] = numMatrix[i][k]
				
			else:
				
				dn = getDownNode(i,k,numMatrix)
				rn = getRightNode(i,k,numMatrix)
				
				if dn != [-1,-1]:
					findSmallestSum(dn[0],dn[1],numMatrix,sumMatrix)
				if rn != [-1,-1]:
					findSmallestSum(rn[0],rn[1],numMatrix,sumMatrix)
				
				dval = -1
				if dn != [-1,-1]:
					dval = sumMatrix[dn[0]][dn[1]]
				rval = -1
				if rn != [-1,-1]:
					rval = sumMatrix[rn[0]][rn[1]]
				
				#print(i,k,numTriangle[i][k][0],vlc,vrc)
				minVal = 0
				
				if not(dval == -1 and rval == -1):
					if dval == -1:
						minVal = rval
					elif rval == -1:
						minVal = dval
					else:
						minVal = min(rval,dval)
						
					sumMatrix[i][k] = numMatrix[i][k]+minVal
	else:
		print("ERROR")
			



def main():
	#see findSmallestSum for algorithm -- main simply calls it and prints the answer. The way I solved the problem the first time
	#worked for this problem, because I used some caching -- the program remembered previously calculated sums
	#Executes in .09 seconds
	t0 = time()
	numberMatrix = getNumMatrix()
	pathMatrix = []
	for i in range(0,len(numberMatrix)):
		pathMatrix.append([])
		for j in range(0,len(numberMatrix[i])):
			pathMatrix[-1].append(0)
	#pathMatrix[3][1] = 2
	findSmallestSum(0,0,numberMatrix, pathMatrix)
	print("Time Elapsed:", time()-t0)
	'''for i in numberMatrix:
		print(i)
	for i in pathMatrix:
		print(i)'''
	print(pathMatrix[0][0])
			



main()


