#Problem: 	What is the sum of the 100 50-digit bumbers in Problem13Numbers.txt in TextFiles?

import math
import os


def ctoi(cha):
	#char to int
	return ord(cha) - ord('0')
	
def removeNonNumeric(xstr):
	#removes non-numeric characters from a string
	rstr = ""
	for i in xstr:
		if ord(i) >= ord('0') and ord(i) <= ord('9'):
			rstr += i
			
	return rstr

def getNumList():

	#gets the list of numbers as an array of strings
	print(os.getcwd())
	f = open("TextFiles\Problem13Numbers.txt", 'r')
	lines = f.readlines()
	nlines = []
	for i in lines:
		nlines.append(removeNonNumeric(i))
	return nlines
		
		
	
def sumTenPlace(tp, numList, carry):
	#sums up the tens place at digit tp (from the back) of numList, wich a carry value of carry
	sum = carry
	for i in numList:
		sum += ctoi(i[tp])
	
	print(sum)
	retar = []
	retar.append(sum%10)
	retar.append(int((sum-(sum%10))/10))
	return retar

			
def main():
	#sum up each digit, right to left, keeping track of the carry and the digit obtained
	#At the end, tack on the remaining carry and grab the last ten numbers in reverse order from the digits array

	numList = getNumList()
	size = len(numList)
	length = len(numList[0])
	
	digits = []
	carry = 0
	for i in range(0, length):
		ip = length-i-1
		sum = sumTenPlace(ip, numList, carry)
		carry = sum[1]
		digits.append(sum[0])
	
	while carry > 1:
		digits.append(carry%10)
		carry = int(carry/10)
	
	firstTen = []

	for i in range (1,11):
		firstTen.append(digits[len(digits)-i])
		
	print(firstTen)
		
	



main()


