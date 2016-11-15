#Problem: 	what is the 10001st prime number?

import math

def isPrime(x):
	if (x == 2 or x == 3 or x ==5 or x == 7):
		return 1
	test = 1
	for i in range(2, int(math.ceil(math.sqrt(x))+1)):
		if not(x%i):
			test = 0
			break
	return test
	
def main():
	#literally just counts up, checking for primes
	ctr = 2
	sixm = 0
	p = 1
	while ctr < 10001:
		
		#this stuff is based on the fact that primes are multiples of 6 +- 1
		if 	p == sixm*6 - 1:
			p = sixm*6 + 1
		elif p == sixm*6 + 1:
			sixm += 1
			p = sixm*6 - 1
			
			
		if isPrime(p):
			ctr+= 1
		
		

	
	print(p)
	


main()