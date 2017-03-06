#Problem: 	Find the "path" (moving only down or down-right) in the trignle in "TriangleProblem67.txt" 
#			that has the maximum sum compared to all other paths. What is this sum? (It might help to look at https://projecteuler.net/problem=18)
#		
#			This problem is almopst exactly the same as problem 18, except the triangle I have to search is much bigger, so I can't check every path -- I 
#			need a better algorithm
import math
import os
from time import time

def getNumList():

	#gets the list of numbers from "TriangleProblem67.txt"
	print(os.getcwd())
	f = open("TextFiles\TriangleProblem67.txt", 'r')
	lines = f.readlines()
	nlines = []
	for i in lines:
		nlines.append(i.split())
	
	numar = []
	for i in nlines:
		numar.append([])
		for k in i:
			numar[len(numar)-1].append([int(k), 0])
	return numar
	
	
def getLeftChild(i, k, tri):
	#gets the coordinates of the left child (straight down)
	if i+1 >= len(tri) or i < 0:
		return [-1,-1]
	elif k >= len(tri[i]) or k < 0:
		return [-1,-1]
	return [i+1, k] 
	
def getRightChild(i, k, tri):
	#gets the coordinates of the right child (straight right)
	if i+1 >= len(tri) or i < 0:
		return [-1,-1]
	elif k >= len(tri[i]) or k < 0:
		return [-1,-1]
	return [i+1, k+1] 

def findGreatestSum(i, k, numTriangle):
	#recursively finds the greatest sum: it looks at the sums in [i][k]'s two children 
	#and picks the bigger one and adds its value to it to figure out its own max sum
	#If the children don't know their sum, recurse once on each child.
	#So it's not total brute-force: it remembers values that it has already calculated
	
	if i >= 0 and i < len(numTriangle) and k >= 0 and k < len(numTriangle[i]):

		if numTriangle[i][k][1] == 0:
			if i == len(numTriangle) - 1:
				numTriangle[i][k][1] = numTriangle[i][k][0]
				#print("bottom: ", numTriangle[i][k][0])
				
			else:
				
				lc = getLeftChild(i,k,numTriangle)
				rc = getRightChild(i,k,numTriangle)
				
				findGreatestSum(lc[0],lc[1],numTriangle)
				findGreatestSum(rc[0],rc[1],numTriangle)
				
				vlc = numTriangle[lc[0]][lc[1]]
				vrc = numTriangle[rc[0]][rc[1]]
				
				#print(i,k,numTriangle[i][k][0],vlc,vrc)
				maxVal = 0
				
				if  vlc[1] > vrc[1]:
					maxVal = vlc[1]
				else:
					maxVal = vrc[1]
					
				numTriangle[i][k][1] = numTriangle[i][k][0]+maxVal
	else:
		print("ERROR")
			



def main():
	#see findGreatestSum for algorithm -- main simply calls it and prints the answer. THe way I solved the problem the first time
	#worked for this problem, because I used some caching -- the program remembered previously calculated sums
	#Executes in .09 seconds
	t0 = time()
	numTriangle = getNumList()
	#print(numTriangle)
	findGreatestSum(0,0,numTriangle)
	print("Time Elapsed:", time()-t0)
	print(numTriangle[0][0][1])
			



main()


