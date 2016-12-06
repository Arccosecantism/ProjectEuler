#Problem:	A prime is cyclic if every number formed by ccling its digits is also prime: so 197 is a cyclic prime becasue 197, 971, and 719 are all prime
#			but 23 is not a cyclic prime because while 23 is prime, 32 is not prime. How many cyclic primes are there under 1000000 (one million)?
#			By the way, 2,3,5,7 are all cyclic primes.

import math
from time import time

def digitsToInt(intList):
	#converts a list of digits to integers: d([4,6,1,3]) = 4613
	strnum = ""
	for i in intList:
		strnum += str(i)
	return int(strnum)


def addLists(listlist):
	#combines a list of lists into one list with all the elements
	#for a([[3,4,5],[1,6],[],[0,0]]), the result is [3,4,5,1,6,0,0]
	retlist = []
	for i in range(0,len(listlist)):
		for k in range(0,len(listlist[i])):
			retlist.append(listlist[i][k])
	return retlist

def generatePalindromes(length):
	halfLength = int(length/2)
	odd = length%2
	repParts = getNumberMultisets(halfLength, 9)
	revRepParts = []
	for i in range(0,len(repParts)):
		tmpList = getReverseList(repParts[i])
		revRepParts.append(tmpList)
	
	palindromsLists = []
	for i in range(0,len(repParts)):
		if odd:
			for k in range(0,10):
				tmpLista = []
				tmpLista.append(repParts[i])
				sl = []
				sl.append(k)
				tmpLista.append(sl)
				tmpLista.append(revRepParts[i])
				palindromsLists.append(digitsToInt(addLists(tmpLista)))
		else:
				tmpLista = []
				tmpLista.append(repParts[i])
				tmpLista.append(revRepParts[i])
				palindromsLists.append(digitsToInt(addLists(tmpLista)))
	return palindromsLists 

def getReverseList(flist):
	revlist = []
	for i in range(0,len(flist)):
		revlist.append(flist[len(flist)-1-i])
	return revlist
	
def getAsReversedBinaryList(x):
	tx = x
	revBinList = []
	while tx > 0:
		revBinList.append(int(tx) & 1)
		tx = int(tx/2)
	return revBinList

def checkListPalindrome(flist):
	hl = int(len(flist)/2)
	good = 1
	for i in range(0,hl):
		if flist[i] != flist[len(flist)-1-i]:
			good = 0
	return good
	
def getNumberMultisets(amt, maxNum):
	#recursively produces a list of <amt> integers taken from numList. So, g(2,[1,2,4]) = [[1,1],[1,2],[1,4],[2,1],[2,2],[2,4],[4,1],[4,2],[4,4]]
	#(not necessarily in this order)
	startSet = [[]]
	endSet = []
	ctr = 0
	first = 1
	while ctr < amt:
		for i in range(0,len(startSet)):
			for k in range(first,maxNum+1):
				
				tmpset = list(startSet[i])
				tmpset.append(k)
				endSet.append(tmpset)
		if first:
			first = 0
		startSet = list(endSet)
		endSet = []
		ctr += 1	  
	return startSet


def main():
	#The strategy: we generate all possible cyclical primes under 1 million that are constituted entirely of 1,3,7,9 as their digits (one of the cycles
	#will end with each digit). Then we check all of those possible primes and see if they are actually cyclical primes. Execution time is a bit annoying:
	#4.89 seconds
	t0 = time()
	cap = 1000000
	tplist = []
	for i in range(1, 7):
		tplist.append(generatePalindromes(i))
	palList = addLists(tplist)
	
	ssum = 0
	for i in palList:
		if checkListPalindrome(getAsReversedBinaryList(i)):
			ssum += i
			print(i)
	
	print("Time Elapsed", time()-t0)
	print(ssum)
main()