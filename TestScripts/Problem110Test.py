import math
from time import time


def sieveOfEratosthenes(x):
    #Produces a list of numbers under x, also tells if they are prime.
    #this is to create an O(1) prime checker for primes under x 
    ar = []
    flick = True
    for i in range(-1,x):
        ar.append(flick)
        flick = not(flick)
    ar[1] = True
    ar[2] = False
    ub = int(math.ceil(math.sqrt(len(ar)))+1)
    for i in range(2,ub):
        if not(ar[i]):
            for k in range(i*i,x,i):
                ar[k] = True
    return ar


def getPrimeList(soe):
    #gets a prime list from sieve
    primelist = []
    for i in range(0,len(soe)):
        if soe[i] == False:
            primelist.append(i)
    return primelist


def primeFactor(x):
	facs = []
	dctr = 2
	while x > 1:
		if not (x%dctr):
			nf = dctr
			mctr = 0
			while not(x%dctr):
				x/=dctr
				mctr+=1
			facs.append((nf,mctr))
		dctr +=1
	return facs

def gcd(x,y):
	a = max(x,y)
	b = x+y-a
	while b != 0:
		c = a%b
		a = b
		b = c
	return a

def testCoprime(a,b):
	return gcd(a,b) == 1



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
			if testCoprime(j[0],j[1]):
				combos.append((i[1],j[0],j[1]))
		if i[0] != i[1]:
			nfacs = getPairwiseFactorsL(i[1],ftab)
			for j in nfacs:
				if testCoprime(j[0],j[1]):
					combos.append((i[0],j[0],j[1]))
	return combos

def testCombination(ctrip):
	ra = (ctrip[0]*ctrip[1])*(ctrip[1]+ctrip[2])
	rb = (ctrip[0]*ctrip[2])*(ctrip[1]+ctrip[2])
	return (ra,rb,int(1.0/(1.0/ra+1.0/rb)))

	"""def countUniqueFactorCombinations(x, ftab):
		combos = getDiophantineFactorCombinations(x, ftab)
		gset = set([])
		for i in combos:
			ri = testCombination(i)
			if ri[0] > ri[1]:
				gset.add((ri[1],ri[0]))
			else:
				gset.add((ri[0],ri[1]))
		return len(gset)"""

def countUniqueFactorCombinations(x, ftab):
	return len(getDiophantineFactorCombinations(x, ftab))

def testNumSet(lst, ftab):
	for i in lst:
		print(i, countUniqueFactorCombinations(i, ftab))

def testExponentListTwo(lst, ftab):
	for i in lst:
		num = (2**i[0])*(3**i[1])
		print(i, num, countUniqueFactorCombinations(num, ftab), i[0]*(i[1] + 1)+i[1]*(i[0] + 1)+1)

def testExponentListThree(lst, ftab):
	for i in lst:
		num = (2**i[0])*(3**i[1])*(5**i[2])
		print(i, num, countUniqueFactorCombinations(num, ftab))

def testExponentListTwoAsList(lst,ftab):
	sol = []
	for i in lst:
		sol.append(countUniqueFactorCombinations((2**i[0])*(3**i[1]),ftab))
	print(sol)

def testExponentListThreeAsList(lst,ftab):
	sol = []
	for i in lst:
		sol.append(countUniqueFactorCombinations((2**i[0])*(3**i[1])*(5**i[2]),ftab))
	print(sol)

def testExponentListFourAsList(lst,ftab):
	sol = []
	for i in lst:
		sol.append(countUniqueFactorCombinations((2**i[0])*(3**i[1])*(5**i[2])*(7**i[3]),ftab))
	print(sol)


def comparePrimeFactorizations(vpfa, vpfb, plist):
	pfa = vpfa[0]
	pfb = vpfb[0]
	if pfa == pfb:
		return False
	lgh = len(pfa)
	if len(pfa) != len(pfb):
		return (-1)
	totala = 0
	totalb = 0
	for i in range(lgh):
		if pfa[i]:
			totala += pfa[i]*math.log(plist[i])
		if pfb[i]:
			totalb += pfb[i]*math.log(plist[i])
	#print(totala, totalb, vpfa, vpfb)
	'''epsilon = .00000001
	if abs(totala-totalb) < epsilon:
		return False'''
	return (totala > totalb)

def getNextGuess(vpfa, posi):
	prod = 1
	for i in range(len(vpfa[0])):
		if i != posi:
			prod *= 2*vpfa[0][i]+1
	nval = prod + vpfa[1]
	np = list(vpfa[0])
	np[posi] += 1
	return [np,nval]




def copyGuess(g):
	ng = []
	ng.append(list(g[0]))
	ng.append(g[1])
	return ng

def generateRecursivePrimeFactorGuesses(seed, collumn, plist, maxex, goal):
	#print(seed)
	#print("----")
	#print(collumn)
	#print("------")
	if collumn >= len(seed[0]):
		#print("break A")
		if seed[1] > goal: 
			#print("appended A", seed)
			return [seed]
		else:
			return []
	possibilties = []

	ctr = seed[0][collumn]
	done = False
	tg = copyGuess(seed)
	#print(tg)

	while not(done):
		#if tg[1] < goal:
		if ctr != seed[0][collumn]:
			#print("works?")
			tg = getNextGuess(tg, collumn)
		if comparePrimeFactorizations(tg, maxex, plist):
			#print("break B", tg)
			done = True
			#if ctr == seed[0][collumn]:
				#print("appended B", tg)
			#	possibilties.append(tg)

		else:
			#print(tg, "next")
			possibilties += generateRecursivePrimeFactorGuesses(tg, collumn+1, plist, maxex, goal)
			#print("----")
			#print("back to",collumn, tg)
			#print("------")

		'''else:
			print("break C", tg)
			#print("appended C", tg)
			#possibilties.append(tg)
			done = True'''

		ctr += 1
		if collumn > 0 and ctr > seed[0][collumn-1]:
			#print("break D", tg)
			#possibilties.append(tg)
			done = True

	return possibilties

def findMinimumGuess(guessList, plist):
	minG = guessList[0]
	for i in guessList:
		if comparePrimeFactorizations(minG,i,plist):
			minG = i
	return minG

def convertToNumber(pfac, plist):
	res = 1
	print(pfac)
	for i in range(len(pfac[0])):
		res *= plist[i]**pfac[0][i]
	return res

def getGoodSeedHeuristic():
	seed = [[1,1,1,1,1,1,1,1,1,1,1,0,0,0,0],88574]
	bseed = seed
	return bseed

def main():
	sieve = sieveOfEratosthenes(1000)
	primeList = getPrimeList(sieve)
	factorTable = generateFactorTable(10000)
	seed = getGoodSeedHeuristic()
	print(seed)
	guesses = generateRecursivePrimeFactorGuesses(seed, 0, primeList, [[1]*15,7174454], 4000000)
	minGuess = findMinimumGuess(guesses, primeList)
	#print(minGuess)
	print(minGuess, convertToNumber(minGuess, primeList))
	
	"""for q in range(0,4):

		for i in range(0,4):
			for j in range(0,4):
				nl = []
				for k in range(0,4):
					nl.append((q,i,j,k))
				testExponentListFourAsList(nl,factorTable)
			print("")
			print("")
		print("")
		print("------")
		print("")

	testExponentListThree(testList, factorTable)
	print(primeFactor(20))
	done = False
	ctr = 2
	highest = 0
	while not(done):
		ctr += 1
		count = countUniqueFactorCombinations(ctr, factorTable)
		if count > highest:
			print(count, ctr, primeFactor(ctr))
			highest = count
		if count > 1000:
			done = True
	print(ctr, countUniqueFactorCombinations(ctr, factorTable))"""

main()