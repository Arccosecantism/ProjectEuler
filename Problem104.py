import math
from time import time

def getFirstNineDigitsNthFib(n,consts):
	pc = max(0,int(math.floor(n*consts[0]+consts[1])-8))
	exp = n-consts[2]*pc
	guess = consts[3]*consts[4]**exp
	return int(math.floor(guess))


def generateFibbonacciLastNine(x):
	mnum = 10**9 
	fib = [0,1]
	for i in range(2,x):
		fib.append((fib[-1]+fib[-2])%mnum)
	return fib

def isPandigital(x):
	if x%9:
		return False
	bitmap = 0
	tx = x
	while tx:
		m = tx%10
		if m == 0:
			return False
		else:
			bitmap += 1 << (m-1)
		tx/=10
	if bitmap == 511:
		return True
	return False

def main():
	t0 = time()
	consts = (	math.log10(.5+math.sqrt(5)/2),
				-.5*math.log10(5),
				math.log(10,.5+math.sqrt(5)/2), 
				math.sqrt(5)/5,
				.5+math.sqrt(5)/2)
	cap = 1000000
	fibl = generateFibbonacciLastNine(cap)
	print("Time Elapsed:", time()-t0) 
	t1 = time()
	for i in range(1,cap):
		if isPandigital(fibl[i]):
			if isPandigital(getFirstNineDigitsNthFib(i,consts)):
				print(i)
	print("Time Elapsed:", time()-t1) 
	print("Time Elapsed:", time()-t0) 

main()