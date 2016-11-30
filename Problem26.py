#Problem: 	What interger in [1,1000] has the longest period of repitition when its reciprocal is represented as a decimal?
#			For instance: 
# 			1/2  = .5 (period of 0)
# 			1/3  = .3'3'3-- (period of 1)
# 			1/4  = .25 (period of 0)
# 			1/5  = .2 (period of 0)
# 			1/6  = .16'6'6--- (period of 1)
# 			1/7  = .142857'142857'142857--- (period of 6)

import math
from time import time

def spotPrevInArray(key, ar):
	#finds the index in an array at which the key appeared earliest. So f(5, [1,3,5,6]) = 2
	#return -1 if key is not an element of array
	rv = -1
	for i in range(0,len(ar)):
		if ar[i] == key:
			rv = i
			break
	return rv

def findReciprocalCycleLength(x):
	#finds the period of repitition of the reciprocal of the integer x

	#first, we cut all numbers that will not have infinite decimals: that is, numbers which are 2^n*5^m for any integers n and m
	twoandfive = 0
	tx = x
	done = 0
	cycleLength = 0
	while not(done):
		if not(tx%5):
			tx /= 5
		elif not(tx%2):
			tx /= 2
		else:
			done = 1
			if int(tx) == 1:
				twoandfive = 1
	if not(twoandfive or x == 1): 
		#if it goes on forever, we essentially do long division until we sense a repeat
		done = 0
		start = 1
		quo = 0
		prod = 0
		spot = 0
		startlist = [1]
		while not(done):
			quo = int(start/x)
			prod = x * quo
			#print(start, x, quo, prod)
			start = start - prod
			start *= 10
			
			#print(start, startlist)
			if quo > 0:
				spot = spotPrevInArray(start, startlist)
				if spot >= 0:
					cycleLength = len(startlist) - spot
					done = 1
					#print("done")
			startlist.append(start)
			#print(start, startlist)
	return cycleLength

		
def main():
	#There are two parts to this one. 1) Most importantly, we need to be able to figure out the period length of a reciprocal of any integer.
	#We accomplish this by long division as seen in findReciprocalCycleLength(x). 2) then, we just count up to the cap (1000), finding all period lengths
	#along the way and we keep track of the number that produced the biggest. Executes in 1.83 seconds.
	tic = time()
	cap = 1000
	longest = 0
	lonNum = 0
	for i in range(1,cap+1):
		tf = findReciprocalCycleLength(i)
		#print(tf)
		if tf > longest:
			longest = tf
			lonNum = i
	print("Time Elapsed: ", time() - tic)
	print("Number: ", lonNum, "Cycle Length: ",  longest)
	
main()


