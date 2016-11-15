#Problem: 	2520 is the smallest number divisible by 1,2,3,...10.
#			What is the smallest number divisible by 1-20 (more generally, 1-n)?

import math

def greatestLesserPower(x,y):
	#findsthe greatest power of x less than or equal to y
	if x > y:
		return 0
	product = 1
	while product <= y:
		product *= x
	return product/x

def isPrime(x):
	if (x == 2 or x == 3 or x ==5 or x == 7):
		return 1
	test = 1
	for i in range(2, int(math.ceil(math.sqrt(x))+1)):
		if not(x%i):
			test = 0
			break
	return test


def lowerPrimes(x):
	#generates the list of all primes less than or equal to x
	plist = []
	for i in range(2,x+1):
		if isPrime(i):
			plist.append(i)
	return plist

	
	
def main():
	#strategy: find the product of the greatest powers less than num of each prime number less than num

	'''print(isPrime(27), isPrime(31), isPrime(3), isPrime(4), isPrime(11))
	print(lowerPrimes(25), lowerPrimes(31))
	print(greatestLesserPower(5,7), greatestLesserPower(2,40))'''
	
	num = 20
	plist = lowerPrimes(num)
	product = 1
	for i in plist:
		product *= greatestLesserPower(i, num)
	print(product)

main()