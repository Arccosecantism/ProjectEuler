import math
from time import time

def generatePairSumTable():
	dartVals = [0]
	for i in range(1,21):
		dartVals.append(i)
		dartVals.append(2*i)
		dartVals.append(3*i)
	dartVals.append(25)
	dartVals.append(50)

	sumArray = [0]*121
	ldv = len(dartVals)
	for i in range(ldv):
		for k in range(i,ldv):
			#if dartVals[i]+dartVals[k] == 3:
			#	print(dartVals[i],dartVals[k],i,k)
			sumArray[dartVals[i]+dartVals[k]] += 1
	return sumArray


def testCheckoutForDouble(sx, stab, maxCheckout):
	dx = 2*sx
	if maxCheckout-dx < 0:
		return 0

	return sum(stab[0:maxCheckout-dx+1])


def testCheckoutForDoubleFixed(sx, stab, checkout):
	dx = 2*sx
	if checkout-dx < 0:
		return 0
	print(sx, dx, checkout-dx, stab[checkout-dx])

	return stab[checkout-dx]

def main():
	sumTable = generatePairSumTable()
	maxCheckout = 99
	psum = 0
	for i in range(1,21):
		psum += testCheckoutForDouble(i, sumTable, maxCheckout)
	psum += testCheckoutForDouble(25, sumTable, maxCheckout)
	print(psum)
main()