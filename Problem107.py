import math
from time import time

def getGraphMatrix():
	f = open("TextFiles\\GraphProblem107.txt", 'r')
	lines = f.readlines()
	#print(lines)
	rows = []
	for i in lines:
		rows.append(map(int, i[:-1].replace("-", "-1").split(",")))
	return rows

def minListA(l, maxnum):
	lg = len(l)
	mv = maxnum
	mvi = 0
	for i in range(lg):
		if l[i]>=0:
			if l[i]<mv:
				mv = l[i]
				mvi = i
	print(mvi, mv)
	return(mvi,mv)

def minListB(l, maxnum):
	lg = len(l)
	mv = maxnum
	mvia = 0
	mvib = 0
	for i in range(lg):
		if l[i][1]>=0:
			if l[i][1]<mv:
				mv = l[i][1]
				mvia = l[i][0]
				mvib = i
	return(mvia, mvib, mv)

def addClosestNode(nodeSet, matrix, maxnum):
	candidates = []
	for i in nodeSet:
		candidates.append(minListA(matrix[i], maxnum))
		print(candidates)
	winner = minListB(candidates, maxnum)
	nodeSet.add(winner[0])
	for i in range(len(matrix)):
		matrix[i][winner[0]] = -1
	matrix[winner[0]][winner[1]]= -1
	return winner[2]
	

def buildMST(gmat, maxnum):
	siz = len(gmat)
	nodeSet = {0}
	csum = 0
	while len(nodeSet) < siz:
		csum += addClosestNode(nodeSet, gmat, maxnum)
		print(nodeSet)
		print("---")
	return csum
	


def main():
	matrix = getGraphMatrix()

	initSum = 0
	for i in matrix:
		for j in i:
			if j >= 0:
				initSum += j
	initSum/=2

	finalSum = buildMST(matrix, 5000)

	saving = initSum-finalSum
	print(saving)

main()
	