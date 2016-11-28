#Problem: 	see https://projecteuler.net/problem=22 : What is the sum of all amicable numbers under 10000? An amicable number x
#			is a number such that, when you sum the factors (less than x) of x, you get y where the sum of y's factors is x. Then x and y are both amicable
#			Also, x =/= y -- perfect numbers are not amicable

import math

def intPow(x,y):
	#integer power function
	product = 1
	for i in range(0,y):
		product *= x
	return product

def getPrimeFactors(x):
	#returns array of arrays: inner array tells you how many prmes you have, so [[2,5],[3,1]] is 2^5*3^1 = 96
	pfacs = []
	pfamt = [2, 0]
	ctr = 2
	while x > 1:
		
		if not(x%ctr):
			x /= ctr
			pfamt[1]+= 1
		else:
			if (pfamt[1] > 0):
				pfacs.append(pfamt)
			ctr += 1
			pfamt = [ctr, 0]
	if (pfamt[1] > 0):
		pfacs.append(pfamt)
	return pfacs
			
def getFactors(x):
	#builds factors based off of prime factors
	pfacs = getPrimeFactors(x)
	facar = [1]
	for n in pfacs:
		lf = len(facar)
		for i in range(1,n[1]+1):
			for k in range(0,lf):
				facar.append(facar[k]*intPow(n[0],i))
	return facar
	
def sumFactors(x):
	#sums up all of the factors of a number
	facsx = getFactors(x)
	sum = 0
	for i in facsx:
		sum += i
	sum -= x
	return sum
	
def getAmicableComplement(x):
	#returns 0 if x is not amicable; otherwise returns the complement of the amicable number
	test = sumFactors(x)
	if sumFactors(test) == x and x != test:
		return test
	else:
		return 0
	
def main():
	#go though all numbers 1-10000, summing the amicable ones
	print(getAmicableComplement(28))
	num = 10000
	sum = 0
	
	for i in range (1, num + 1):
		sum += getAmicableComplement(i)
		
	print(sum)

main()


