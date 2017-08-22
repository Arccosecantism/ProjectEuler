import math
from time import time

def readSets():
	f = open("TextFiles\\SetsProblem105.txt", 'r')
	lines = f.readlines()
	sets = []
	for i in lines:
		sets.append(map(int, i[:-1].split(",")))
	return sets

def getNumberOfOnesBinary(x):
	numOnes = 0
	while x:
		numOnes += x&1
		x >>= 1
	return numOnes

def getNUmberOfZerosBinary(x, lgh):
	return lgh - getNumberOfOnesBinary(x)

def getSubsetBlueprints(lgh):
	subsetBlueprints = []

	amt = (1,1<<(lgh-1))


	for i in range(amt[0],amt[1]):
		subsetBlueprints.append(i)

	return subsetBlueprints

def getSubsetBlueprintPairs(lgh):
	
	nonduplicates = [False]*(1<<(lgh<<1))
	#print(len(nonduplicates))

	pairs = []
	leftSubs = getSubsetBlueprints(lgh)
	for i in leftSubs:
		for j in range(1,1<<lgh):
			if not(j&i):
				a = i
				b = j
				if j > i:
					b = i
					a = j
				cnum = (a << lgh) + b
				if not(nonduplicates[cnum]):
					nonduplicates[cnum] = True
					pairs.append((i,j)) 
	return pairs

def getCardinalityTable(lgh):
	table = []
	for i in range(1<<lgh):
		table.append(getNumberOfOnesBinary(i))
	return table

def getSumTable(fset):
	lgh = len(fset)
	cap = 1<<(lgh)
	table = []
	for i in range(cap):
		x = i
		subsum = 0
		for j in range(lgh):
			if x&1:
				subsum += fset[j]
			x >>= 1
		table.append(subsum)
	return table

def testSetCoarse(lst):
	if len(set(lst)) != len(lst):
		return False
	return True

def testSetMedium(lst):
	pairSums = []
	for i in range(len(lst)-1):
		for j in range(i+1, len(lst)):
			pairSums.append(lst[i]+lst[j])
	if not(testSetCoarse(pairSums)):
		return False

	for i in pairSums:
		for j in lst:
			if i == j:
				return False
	return True

def testSetFine(blueprints, sumTable, cardTable):

	for i in blueprints:
		lsum = sumTable[i[0]]
		rsum = sumTable[i[1]]
		lnt = cardTable[i[0]]
		rnt = cardTable[i[1]] 
		if lsum == rsum:
			return False
		if lnt > rnt and not(lsum > rsum):
			return False
		if rnt > lnt and not(rsum > lsum):
			return False

	return True

def testSet(lst, blueprints, cardTable):
	if testSetCoarse(lst):
		#print("coarse Y")
		if testSetMedium(lst):
			#print("smoother Y")
			if testSetFine(blueprints, getSumTable(lst), cardTable):
				#print("fine Y")
				return True
	#print("fails coarse ?")
	return False


def main():
	t0 = time()
	sets = readSets()
	for i in sets:
		print(i)
	cardTables = []
	blueprints = []
	for i in range(7,13):
		cardTables.append(getCardinalityTable(i))
		blueprints.append(getSubsetBlueprintPairs(i))
	sumsum = 0
	for i in sets:
		sl = len(i)-7
		if testSet(i,blueprints[sl],cardTables[sl]):
			sumsum += sum(i)
	print(sumsum)
	print("Time Elapsed:", time()-t0) 
main()
