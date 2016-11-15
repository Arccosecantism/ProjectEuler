#Problem: 	What is the greatest product of four numbers in a line (up, down, left, right, diagonal) 
#			in the table shown in yellow at line 29?

import math
import os


def max(x,y):
	if x > y:
		return x
	return y
	
def min(x,y):
	if x < y:
		return x
	return y

def ctoi(cha):
	#char to int
	return ord(cha) - ord('0')
	
def removeNonNumeric(xstr):
	rstr = ""
	for i in xstr:
		if ord(i) >= ord('0') and ord(i) <= ord('9'):
			rstr += i
			
	return rstr

def getNumList():
	print(os.getcwd())
	f = open("TextFiles\Problem13Numbers.txt", 'r')
	lines = f.readlines()
	#print(lines)
	nlines = []
	for i in lines:
		nlines.append(removeNonNumeric(i))
		#print(nlines[len(nlines)-1])
	#print(nlines)
	return nlines
		
	
def intPow(x,y):
	#recursive integer exponentiation function -- used to avoid rounding errors
	if y <= 0:
		return 1
	else:
		return x * intPow(x,y-1)


def numberOfDigits(x):
	dignum = int(math.ceil(math.log10(x+1)))
	return dignum
	


	
def getMaxSize(length, number):
	return numberOfDigits(number) + length 
	
def getZeroArray(size):
	zar = []
	for i in range(0,size):
		zar.append(0)
	return zar


def addArrays(ara, arb):
	nar = []
	if len(ara) != len(arb):
		return nar
	
	for i in range(0,len(ara)):
		nar.append(ara[i]+arb[i])
	return nar
			
		
def itoar(x, digits, offset):
	dig = numberOfDigits(x)
	retar = getZeroArray(digits)
	ctr = dig
	while ctr > 0:
		fac = intPow(10,ctr-1)
		ntens = x/fac
		retar[len(retar)-ctr-offset] = ntens
		#print(len(retar)-ctr-offset)
		x = x % fac
		ctr -= 1
		
	
	return retar
	
def sumTenPlace(tp, numList, carry, ub):
	col = tp
	#print(carry)
	sum = carry
	for i in numList:
		sum += ctoi(i[col])
	#print(sum)
	return itoar(sum, ub, len(numList[0]) - 1 - col) 

			
def main():
	#go through each cell, check all the products in all directions, essentially
	
	
	#print(removeNonNumeric("\n\n\n"))

	numList = getNumList()
	size = len(numList)
	length = len(numList[0])
	upperBound = getMaxSize(length, size)
	
	#print(upperBound)
	#print(addArrays([0,0,1,5,6,3,0], [1,2,0,0,4,1,0]))
#	print(itoar(1234, upperBound, 10))
	#print(size)
	carries = getZeroArray(upperBound)
	digits = getZeroArray(upperBound)
	for i in range(0, length):
		ip = length-i-1
		sum = sumTenPlace(ip, numList, carries[len(carries)-i-1], upperBound)
		carries = addArrays(sum, carries)
		digits[len(digits)-i-1] = sum[len(sum)-i-1]
	#	print(carries, sum)
		#print(sumTenPlace(ip, numList, carries[len(carries)-i-1], upperBound), carries)
		
		
	#print(sumTenPlace(49,numList,carries[0]))
	print(digits, carries)
		
	



main()


