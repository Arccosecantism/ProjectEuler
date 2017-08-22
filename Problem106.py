import math
from time import time

def getBinaryExpansion(x):
	sx = ""
	while x:
		sx += str(x&1)
		x>>=1
	rx = ""
	for i in range(len(sx)):
		rx += sx[-(i+1)]
	return rx

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

def getEqualSubsetBlueprintPairs(lgh, cardTable):
	olist = getSubsetBlueprintPairs(lgh)
	nlist = []
	for i in olist:
		if cardTable[i[0]] > 1:
			if cardTable[i[0]] == cardTable[i[1]] :
				nlist.append(i)
	return nlist
	
def testBlueprints(ebps):
	numToTest = 0
	for i in ebps:
		a = min(i[0],i[1])
		b = i[0]+i[1]-a
		csum = 0
		while ((csum >= 0) and (b > 0)):
			if b&1:
				csum -= 1
			elif a&1:
				csum += 1
			b>>=1
			a>>=1
		if csum < 0:
			numToTest += 1
		
	return numToTest


def main():
	t0 = time()
	length = 12
	cardTable = getCardinalityTable(length)
	blueprints = getEqualSubsetBlueprintPairs(length, cardTable)
	print(testBlueprints(blueprints))
	print("Time Elapsed:", time()-t0) 

main()
