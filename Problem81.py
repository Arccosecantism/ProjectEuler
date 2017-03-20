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

def findGreatestSum(i, k, numMatrix, sumMatrix):
	#recursively finds the greatest sum: it looks at the sums in [i][k]'s two children 
	#and picks the bigger one and adds its value to it to figure out its own max sum
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
					findGreatestSum(dn[0],dn[1],numMatrix,sumMatrix)
				if rn != [-1,-1]:
					findGreatestSum(rn[0],rn[1],numMatrix,sumMatrix)
				
				dval = -1
				if dn != [-1,-1]:
					dval = sumMatrix[dn[0]][dn[1]]
				rval = -1
				if rn != [-1,-1]:
					rval = sumMatrix[rn[0]][rn[1]]
				
				#print(i,k,numTriangle[i][k][0],vlc,vrc)
				maxVal = 0
				
				if not(dval == -1 and rval == -1):
					if dval == -1:
						maxVal = rval
					elif rval == -1:
						maxVal = dval
					else:
						maxVal = min(rval,dval)
						
					sumMatrix[i][k] = numMatrix[i][k]+maxVal
	else:
		print("ERROR")
			



def main():
	#see findGreatestSum for algorithm -- main simply calls it and prints the answer. THe way I solved the problem the first time
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
	findGreatestSum(0,0,numberMatrix, pathMatrix)
	print("Time Elapsed:", time()-t0)
	'''for i in numberMatrix:
		print(i)
	for i in pathMatrix:
		print(i)'''
	print(pathMatrix[0][0])
			



main()


