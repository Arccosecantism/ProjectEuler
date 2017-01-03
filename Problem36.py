#Problem:	What is the sum of all numbers under 1000000 (one million) that are palindromic in both base 10 and in base 2?

import math
from time import time

def digitsToInt(intList):
	#converts a list of digits to integers: d([4,6,1,3]) = 4613
	#print(intList)
	strnum = ""
	for i in intList:
		strnum += str(i)
		
	return int(strnum)

def intToDigits(x):
	#converts a number to a list of digits: I(4613) = [4,6,1,3]
	revdigs = []
	tx = x
	while tx > 0:
		revdigs.append(tx%10)
		tx = int(tx/10)
	return(getReverseList(revdigs))

def addLists(listlist):
	#combines a list of lists into one list with all the elements
	#for a([[3,4,5],[1,6],[],[0,0]]), the result is [3,4,5,1,6,0,0]
	retlist = []
	for i in range(0,len(listlist)):
		for k in range(0,len(listlist[i])):
			retlist.append(listlist[i][k])
	return retlist

def intPow(x,y):
	#returns x^y as an integer if x and y are integers. removes rounding errors.
	product = 1
	for i in range(0,y):
		product *= x
	return product


def generateBinaryPalindromes(length):
	#generates all binary digit-lists of binary numbers that are palindromic and are <length> digits long
	halfLength = int(length/2)
	odd = length%2
	repParts = getNDigitBinaries(halfLength)
	#print(length, halfLength, repParts)
	revRepParts = []
	for i in range(0,len(repParts)):
		tmpList = getReverseList(repParts[i])
		revRepParts.append(tmpList)
	
	palindromesLists = []
	for i in range(0,len(repParts)):
		if odd:
			for k in range(0,2):
				tmpLista = []
				tmpLista.append(repParts[i])
				sl = []
				sl.append(k)
				tmpLista.append(sl)
				tmpLista.append(revRepParts[i])
				#print(tmpLista)
				palindromesLists.append(addLists(tmpLista))
		else:
				tmpLista = []
				tmpLista.append(repParts[i])
				tmpLista.append(revRepParts[i])
				#print(tmpLista)
				palindromesLists.append(addLists(tmpLista))
	return palindromesLists 

def getReverseList(flist):
	#gives the reverse of a list: g([5,3,4]) = [4,3,5] 
	revlist = []
	for i in range(0,len(flist)):
		revlist.append(flist[len(flist)-1-i])
	return revlist
	
def getAsReversedBinaryList(x):
	#gives a number as a reversed binary digit-list: R(11) = [1,1,0,1] (11 is 1011 in binary)
	tx = x
	revBinList = []
	while tx > 0:
		revBinList.append(int(tx) & 1)
		tx = int(tx/2)
	return revBinList


def getAsBase10(binList):
	#takes a binary digit list and returns the base 10 number it represents: B([1,0,1,1]) = 11
	btnum = 0
	mult = 1
	for i in range(0, len(binList)):
		btnum += binList[len(binList)-1-i]*mult
		mult *= 2
	return btnum

def checkListPalindrome(flist):
	#checks if a list is palindromic
	hl = int(len(flist)/2)
	good = 1
	for i in range(0,hl):
		if flist[i] != flist[len(flist)-1-i]:
			good = 0
	return good
	
def getNDigitBinaries(digit):
	#creates all n-digit binary numbers
	binar = []
	if digit >= 1:
		mink = intPow(2,digit-1)
		maxk = 2*mink
		for i in range(mink, maxk):
			newRevBin = getAsReversedBinaryList(i)
			newBin = getReverseList(newRevBin)
			binar.append(newBin)
	else:
		binar.append([])
	return binar
	
def main():
	#The strategy: We generate all binary palindromes as a digit-list (there are fewer binary palindromes than decimal
	#palindromes under any given number). Then, for eacg digit-list, we check if the decimal number it represents is under
	#one million and is palindromic. Executes in 0.11 seconds.
	t0 = time()
	cap = 1000000
	tplist = []
	maxBin = int(math.log(cap,2))+1
	for i in range(1, maxBin+1):
		tplist.append(generateBinaryPalindromes(i))
	palList = addLists(tplist)
	
	ssum = 0
	for i in palList:
		btNum = getAsBase10(i)
		if btNum < cap:
			if checkListPalindrome(intToDigits(btNum)):
				ssum += btNum
				print(i, btNum)
	
	print("Time Elapsed", time()-t0)
	print(ssum)

main()