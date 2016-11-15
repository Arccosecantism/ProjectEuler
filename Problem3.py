#Problem: find greatest prime factor of 600851475143

import math

def main():
#simple approach: cut by the smallest factor (always a prime) until the number is 1. record the largest factor, which is prime -- that is that largest prime factor
	largest = 0;
	prime = 0
	num = 600851475143
	while num > 1:
		for i in range(2,math.ceil(math.sqrt(num))+1):
		#only need to check up to the squareroot , but ceiling-ed and raised by 1 to avoid rounding errors
			if (num % i == 0):
				#cut the num by its factors
				num /= i
				
				if (i > largest):
					#keep track of the biggest
					largest = i
	if largest == 0:	
		#if there were no factors, num itself must be prime
		largest = num
	print(largest)
				
				


main()