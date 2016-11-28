#Problem: 	What is the sum of the digits in 100 factorial?

import math



def getFArray(num):
	#returns an array filled with 1-num. But, it removes factors of 10, so when you multiply facArray, there should not be 0s at the end
	facArray = []
	needTwo = 0
	for i in range(1,num+1):
		test = i
		while not(test%10):
			test/=10
		if not(test%5):
			test /= 5
			needTwo = 1
		if needTwo and not(test%2):
			needTwo = 0
			test /= 2
		if test > 1:
			facArray.append(test)
	if needTwo:
		facArray[1] = 1
	return facArray
			
def getNumberOfDigits(x):
	#gets number of digits in a number
	if (x == 0):
		return 0
	else:
		return len(str(x))

def getNthDigit(x,n):
	#gets the nth digit of x, starting from the back (1st digit of 1234 is 4)
	indx = getNumberOfDigits(x) - n
	return  int(str(x)[indx])

	
def main():
	#Get an array that gives you no factors of 10, so we dont have 30 zeros at the end.
	#then, we just dothe multiplications on a number represented by an array of digits. Multiply and carry
	#until finished. then, just count up the digits
	num = 100
	far = getFArray(num)
	digArray = [1]
	carry = 0
	for i in far:
		tl = len(digArray)
		for k in range(0,tl):
			mult = digArray[k] * i + carry
			up = mult%10 
			tp = int((mult - up)/10)
			digArray[k] = up
			carry = tp
		for j in range(0, getNumberOfDigits(carry)):
			digArray.append(getNthDigit(carry, j+1))
		carry = 0

	#print(digArray)	
	
	sum = 0
	for i in digArray:
		sum += i
	print(sum)


main()


