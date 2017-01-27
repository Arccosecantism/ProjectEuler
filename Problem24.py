#Problem: 	Take the numbers 0-9. If we list all the orderings in ascending order, we get 0123456789, 0123456798, 0123456879, 0123456897, etc.
#			let s(n) be the nth term in this series. So s(3) = 0123456879 and s(4) = 0123456897
#			What is s(1000000)?

import math
from time import time


def fac(x):
	#factorial
	if x == 0:
		return 1
	else:
		return x*fac(x-1)


def arrayToString(digar):
	#converts array of digits to string: [0,4,2,5] becomes "0425"
	return ''.join(map(str, digar))
	
def main():
	#love this one: store (1000000 divided by 9!) = 2, mod 1000000 by 9!, store (274240 divided by 8!) = 6, mod by 8!, ... repeat down to 0!
	#then, remove the collisions -- make sure the same order is preserved, but the numbers are not the same. And, surprisingly enough, that is the answer
	#takes 18 ms on my computer
	
	tic = time()
	
	
	dnum = 10
	digitList = [i for i in range(0,dnum)]
	snum = 1000000
	num = snum - 1
	
	resList = []

	
	for i in range(0,dnum):
		ti = dnum-1-i
		quo = int(num/fac(ti))
		resList.append(digitList[quo])
		num %= fac(ti)
		del digitList[quo]

	
	numStr = arrayToString(resList)
	print("Time Elapsed: ", time() - tic)
	print(numStr)
	
main()


