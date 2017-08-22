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

	if collumn >= len(seed[0]):
		if seed[1] > goal: 
			return [seed]
		else:
			return []
	possibilties = []

	ctr = seed[0][collumn]
	done = False
	tg = copyGuess(seed)

	while not(done):
		if ctr != seed[0][collumn]:
			tg = getNextGuess(tg, collumn)
		if comparePrimeFactorizations(tg, maxex, plist):
			done = True
		else:
			possibilties += generateRecursivePrimeFactorGuesses(tg, collumn+1, plist, maxex, goal)


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
	seed = getGoodSeedHeuristic()
	guesses = generateRecursivePrimeFactorGuesses(seed, 0, primeList, [[1]*15,7174454], 4000000)
	minGuess = findMinimumGuess(guesses, primeList)
	print(minGuess, convertToNumber(minGuess, primeList))
	

main()