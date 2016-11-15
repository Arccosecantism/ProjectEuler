#Problem: find greatest number that is both palindromic and a product of two three-digit numbers

import math

def intPow(x,y):
	#recursive integer exponentiation function -- used to avoid rounding errors
	if y <= 0:
		return 1
	else:
		return x * intPow(x,y-1)

def isPalindrome(x):
	#test if a number is a palindrome
	#overall strategy is take the left and right part (63536 would yield 63 and 36). If the reversed right 
	#part is the same as the left, the number is palindromix
	dignum = int(math.ceil(math.log10(x+1)))
	rpart = x % intPow(10,(dignum/2))
	lpart = int(x / intPow(10, (dignum+1) / 2))
	revlpart = 0
	ctr = dignum/2-1
	
	while lpart > 0:
		revlpart += lpart % 10 * intPow(10,ctr)
		lpart = int(lpart/10)
		ctr -= 1
		
	if (revlpart == rpart):
		return 1
	else:
		return 0
 
def main():
	#tests every different pair of three-digit numbers for greatness of its product
	#if it's greater than the previous record, if it is palindromic, it becomes the new record
	#at the end, the record is the greatest palindrome that is a product of two three-digit numbers
	largest = 0
	product = 0
	for i in range(100,999):
		for k in range(i,1000):
			product = i*k
			if product>largest:
				if isPalindrome(product):
					largest = product
	print(largest)

main()