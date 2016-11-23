#Problem: 	The sum of the digits in 2^15 = 3+2+7+6+8 = 26. What is the sum of the digits in 2^1000
import math



def main():
	#this problem is quite simple: start with 1, double it 1000 times while keeping track of digits and carrying.
	#one thing that makes this problem easy is that the maximum amount of carrying you will have is 1 because 9*2 = 18 and 9 * 2 + 1 (assuming it was carried) = 19
	num = 1000
	digitList = [1]
	for i in range(0, num):
		tl = len(digitList)
		carry = 0
		for k in range(0,tl):
			digitList[k] *= 2
			if carry: 
				digitList[k] += 1
				carry = 0
			if digitList[k] >= 10:
				carry = 1
				digitList[k] -= 10
		if carry:
			digitList.append(1)
	
	sum = 0
	for i in digitList:
		sum += i
		
	print(sum)
			



main()


