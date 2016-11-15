#Problem: 	What starting number under one million produces the longest Collatz sequence? (Collatz sequence is: if x is odd -> 3x+1; otherwise -> x/2)

import math
import os


def doCollatz(collatzArray):
	c = list(collatzArray)
	if c[0]%2:
		c[0] = c[0]*3+1
	else:
		c[0] = int(c[0]/2)
	c[1] += 1
	return c

def generateTreePositions(size):
	tr = []
	for i in range(0, size):
		tr.append([i+1,-1])
	return tr


def lengthCollatz(collatzTree, collatzArray):
	
	indx = -1
	for i in range(0, len(collatzTree))
		if collatzTree[i][0] == collatzArray[0]:
			indx = i
			break
	if ind
	collatzArray[1] += 1+lengthCollatzCollatz(collatzTree, collatzArray)[1]
	#while not(collatzArray[0] in collatzTree):
	#	doCollatz(collatzArray)



def main():
	#sum up each digit, right to left, keeping track of the carry and the digit obtained
	#At the end, tack on the remaining carry and grab the last ten numbers in reverse order from the digits array
	c = [4,0]
	doCollatz(c)
	print(doCollatz(c), c)
	collatzTree = []
	#for i in range(1,1000000):

		
	



main()


