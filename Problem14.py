#Problem: 	What starting number under one million produces the longest Collatz sequence? (Collatz sequence is: if x is odd -> 3x+1; otherwise -> x/2)

import math


def doCollatz(num):
	#determines next number of x according to collatz sequence
	c = num
	if c%2:
		c = c*3+1
	else:
		c = int(c/2)
	return c

def generateTreePositions(size):
	#creates a list of numbers and their collatz sequence lengths of length <size>
	tr = []
	for i in range(0, size):
		tr.append([i+1, 0])
	return tr


def findNextCollatzUnder(x, cap):
	#finds the next collatz number under a cap
	c = doCollatz(x)
	ctr = 1
	
	while c > cap:
		c = doCollatz(c)
		ctr += 1
	return [c, ctr] 


def lengthCollatz(collatzTree, num):
	#finds the collatz sequence length of a number (and stores all of the other numbers reached but below the size of the tree)
	treeLength = len(collatzTree)
	if num > 1:

		tmp = findNextCollatzUnder(num, treeLength)
		colNum = tmp[0]
		extraLength = tmp[1]

		if collatzTree[num-1][1] <= 0:

			if collatzTree[colNum-1][1] <= 0 and colNum > 1:
				lengthCollatz(collatzTree, colNum)
			
			collatzTree[num-1][1] = extraLength+collatzTree[colNum-1][1]
			#print("here2", num, collatzTree[num-1][1])
		
	



def main():
	#we just check every number, remembering all of the other numbers we hit: this allows
	#us to not have to recheck any. Remembering only happens under the size we care about (1 million): if a number gets too high
	#we have to resize the tree and we end up storing way too many things
	#then we find the longest
	
	maxLength = 1000000

	collatzTree = generateTreePositions(maxLength)
	#print(findNextCollatzUnder(3, 9))

	for i in range(1,maxLength+1):
		lengthCollatz(collatzTree, i)
		
	longest = [0,0]
	
	for i in range(0,maxLength):
		if collatzTree[i][1] > longest[1]:
			longest = [i+1, collatzTree[i][1]]
	print("result:", longest)




main()


