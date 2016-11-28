#Problem: 	Let S(x) be the sum of all proper divisors of x. So S(10) = 1+2+5=8. A number x is perfect if x=S(x). 6 and 28 are perfect.
#			A number n is abundant is S(n)>n The first abundant number is 12. What is the sum of all integers that are not the sum of two abundant numbers?
#			Also, we know that all integers > 28123 are the sum of two abundant numbers.

import math
from time import time


def sumFactors(x):
	#sums of factors
	if x == 1:
		return 1
	ctr = 1
	done = 0
	sum = 1

	while not(done):
		ctr += 1
		if not(x%ctr):
			
			if ctr >= int(x/ctr):
				done = 1
				if ctr == int(x/ctr):
					sum += ctr
			else:
				sum += ctr
				sum += int(x/ctr)
	return sum

def isAbundant(x):
	#tells if a number is abundant or not. Also, if a number is neither divisible by 2 or 3, it is not abundant.
	#This is not always true, but the first number that breaks this rule is 5391411025. This conditional can be removed,
	#but it helps speed by a noticeable amount and is somewhat scalable.
	if x%2 and x%3:
		return 0
	elif sumFactors(x) > x:
		return 1
	else:
		return 0

		
def checkOffLargerMultiples(nar, x):
	#Think sieve of Eratosthenes: checks off all numbers in a list of numbers that are multiples of x and larger than x
	msiz = len(nar)
	mult = 2*x
	while  mult <= msiz:
		nar[mult-1] = 1
		mult += x
	
	
def main():
	#kind of a tough one: There are two parts.
	#First step: make an array with size <cap> and full of 0s. Then, check off (make 1) all multiples of perfect numbers, as these are all abundant
	#Then go through the list. If you find a number that hasn't been checked off, test if it's abundant. If it is, check off all of its multiples, as 
	#they are also abundant. If a number is checked off, or is abundant, add it to an array of abundant numbers under the cap
	#
	#Second Step: refresh the number array -- uncheck everything. Then go through each pair of abundant numbers and check all of the numbers that are the sum of the pair
	#(this sucks, this is O(n^2), and with an array size as big as 7000, on my computer, it takes about 10 seconds to complete.)
	#Then sum up the unchecked ones, and there is the answer
	
	#In total, 13.23 seconds to execute on my computer
	tic = time()
	
	cap = 28123
	#cap = 10000
	abundantArray = []
	
	baseArray = [6,28,496,8128]
	
	numArray = []
	for i in range(0,cap):
		numArray.append(0)

	
	for i in baseArray:
		checkOffLargerMultiples(numArray, i)
	
	
	for i in range(0,len(numArray)):
		if numArray[i] == 1:
			abundantArray.append(i+1)
		elif isAbundant(i+1):
			abundantArray.append(i+1)
			checkOffLargerMultiples(numArray, i+1)
	#print(abundantArray, len(abundantArray))
	#print("here")
	
	for i in range(0,len(numArray)):
		numArray[i] = 0
	
	for i in range(0,len(abundantArray)):
		for k in range(i, len(abundantArray)):
			if abundantArray[i]+abundantArray[k] <= len(numArray):
				numArray[abundantArray[i]+abundantArray[k]-1] = 1
	
	sum = 0
	for i in range(0,len(numArray)):
		if numArray[i] == 0:
			sum += i+1
	print("Time Elapsed: ", time() - tic)
	print(sum)
	
main()


