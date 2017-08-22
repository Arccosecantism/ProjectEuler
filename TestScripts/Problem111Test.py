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


def getPrimeListBetween(soe, minv, maxv):
    #gets a prime list from sieve
    primelist = []
    for i in range(0,len(soe)):
        if soe[i] == False:
			if i >= minv and i <= maxv:
				primelist.append(i)
    return primelist

def main():
	sieve = sieveOfEratosthenes(10**6)
	primeList = getPrimeListBetween(sieve, 10**4, 10**6)
	minValue = 10**9
	maxValue = 10**10
	valset = set([])
	print(primeList[0])
	done = False
	for i in range(len(primeList)):
		for j in range(i,len(primeList)):
			pi = primeList[i]
			pj = primeList[j]
			print(pi, pj)
			if pi*pj >= minValue:
				if pi*pj < maxValue:
					valset.add(pi*pj)

				else:
					if pj == pi:
						done = True
					break
		if done == True:
			break
	print(valset, len(valset))

	

main()