#Problem: 	Take the numbers 0-9. If we list all the orderings in ascending order, we get 0123456789, 0123456798, 0123456879, 0123456897, etc.
#			let s(n) be the nth term in this series. So s(3) = 0123456879 and s(4) = 0123456897
#			What is s(1,000,000)?

import math
from time import time


def fac(x):
	#factorial
	if x == 0:
		return 1
	else:
		return x*fac(x-1)

		
def avoidCollisions(dnum, ar):
	#kind of hard to explain: takes [2200], returns [2301] -- [0,1,*2,3], [0,1,*3], [*0,1], [*1]
	#moves the numbers up and down to avoid being the same as a previous number
	dar = []
	for i in range(0,dnum):
		dar.append([i,0])
	retar = []
	for i in range(0,len(ar)):
		ctr = 0
		indx = 0
		set = 0
		for k in range(0,len(dar)):
			if dar[k][1] == 0:
				ctr += 1
			if ctr == ar[i] + 1 and set == 0:
				indx = k
				set = 1
				dar[k][1] = 1
		retar.append(indx)
	return retar
	
def arrayToString(digar):
	#converts array of digits to string: [0,4,2,5] becomes "0425" 
	xstr = ''
	for i in digar:
		xstr += str(i)
	return xstr
	
def main():
	#love this one: store (1000000 divided by 9!) = 2, mod 1000000 by 9!, store (274240 divided by 8!) = 6, mod by 8!, ... repeat down to 0!
	#then, remove the collisions -- make sure the same order is preserved, but the numbers are not the same. And, surprisingly enough, that is the answer
	#takes 18 ms on my computer
	
	tic = time()
	
	dnum = 10
	snum = 1000000
	#snum = 9
	num = snum - 1
	
	
	
	resArray = []
	for i in range(0,dnum):
		resArray.append(0)
	
	for i in range(0,dnum):
		ti = dnum-1-i
		resArray[i] = int(num/fac(ti))
		num %= fac(ti)
		
	uncollided = avoidCollisions(dnum, resArray)
	numUnc = arrayToString(uncollided)
	print("Time Elapsed: ", time() - tic)
	print(numUnc)
	
main()


