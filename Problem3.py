#Problem: find greatest prime factor of 600851475143

import math

def main():
#simple approach: cut by the smallest factor (always a prime) until the number is 1. record the largest factor, which is prime -- that is that largest prime factor
	largest = 0;
	prime = 0
	num = 600851475143
	while num > 1:
		for i in range(2,math.ceil(math.sqrt(num))+1):
		#only need to check up to the squareroot -- a bit extra for avoiding rounding errors
			if (num % i == 0):
				num /= i
				if (i > largest):
					largest = i
	if largest == 0:
		print(num)
	else:
		print(largest)
				
				


main()