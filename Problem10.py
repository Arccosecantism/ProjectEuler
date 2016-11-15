#Problem: 	What is the sum of all primes less than two million?

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
	#I don't think there is a non-brute force way to do this. I've seen people try to use a
	#seive of eratosthanes, but I think that is just a trade off of memory for speed
	
	#this solution is simple: just count up, if the number is a prime, add it to the sum.
	#On my computer, takes 30-60 seconds to execute
	cap = 2000000
	sum = 5
	sixm = 1
	p = 5
	ctr = 0
	while p < cap:
		

			
		if isPrime(p):
			sum += p
			#print(sum, p)
			
		if 	p == sixm*6 - 1:
			p = sixm*6 + 1
		elif p == sixm*6 + 1:
			sixm += 1
			p = sixm*6 - 1
	'''	ctr+= 1
		if (ctr % 10000 == 1):
			print(p)'''
	print(sum)
	


main()