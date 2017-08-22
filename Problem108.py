import math
from time import time

def getPairwiseFactors(x):
	if x == 2:
		return [(1,2)]
	if x == 1:
		return [(1,1)]
	if x <= 0:
		return [(0,0)]
	
	pairwiseFactors = []
	sqx = int(math.ceil(math.sqrt(x)))+1
	for i in range(1, sqx):
		if not(x%i):
			pa = i 
			pb = x/i
			if pa <= pb:
				pairwiseFactors.append((pa,pb))
			

	return pairwiseFactors		 



def generateFactorTable(n):

	table = []
	for i in range(0,n+1):
		table.append(getPairwiseFactors(i))
	return table

def getPairwiseFactorsL(x,ftab):
	facPairs = []
	if x < len(ftab):
		facPairs = ftab[x]
	else:
		facPairs = getPairwiseFactors(x)
	return facPairs

def getDiophantineFactorCombinations(x, ftab):
	facPairs = getPairwiseFactorsL(x,ftab)
	combos = []
	for i in facPairs:
		nfacs = getPairwiseFactorsL(i[0],ftab)
		for j in nfacs:
			combos.append((i[1],j[0],j[1]))
		if i[0] != i[1]:
			nfacs = getPairwiseFactorsL(i[1],ftab)
			for j in nfacs:
				combos.append((i[0],j[0],j[1]))
	return combos

def testCombination(ctrip):
	ra = (ctrip[0]*ctrip[1])*(ctrip[1]+ctrip[2])
	rb = (ctrip[0]*ctrip[2])*(ctrip[1]+ctrip[2])
	return (ra,rb,int(1.0/(1.0/ra+1.0/rb)))

def countUniqueFactorCombinations(x, ftab):
	combos = getDiophantineFactorCombinations(x, ftab)
	gset = set([])
	for i in combos:
		ri = testCombination(i)
		if ri[0] > ri[1]:
			gset.add((ri[1],ri[0]))
		else:
			gset.add((ri[0],ri[1]))
	return len(gset)
def main():

	factorTable = generateFactorTable(10000)
	done = False
	ctr = 11988
	highest = 0
	while not(done):
		ctr += 12
		count = countUniqueFactorCombinations(ctr, factorTable)
		if count > highest:
			print(count, ctr)
			highest = count
		if count > 1000:
			done = True
	print(ctr, countUniqueFactorCombinations(ctr, factorTable))

main()