import math
from time import time

def intpow(x,y):
	prod = 1
	for i in range(0,y):
		prod *= x
	return prod

def generateInitialSequence():
	leg = 15
	retlist = []
	for i in range(1,leg+1):
		retlist.append(gfunc(i))
	return retlist
def gfuncTest(n):
	return n*n*n

def gfunc(n):
	vsum = 0
	for i in range(0,11):
		vsum += intpow(-1,i)*intpow(n,i)
	return vsum

def findFit(order, seq):
	if order == 0:
		return seq[0]
	sl = len(seq)
	pseq = seq[:order+1]
	difs = []
	for i in range(0,order):
		difs.append([])


	for i in range(1,len(pseq)):
		instdif = pseq[i]-pseq[i-1]
		difs[0].append(instdif)
		for j in range(1,i):
			difs[j].append(difs[j-1][i-j]-difs[j-1][i-j-1])
	
	for i in range(0,len(difs)):
		if i == 0:
			difs[-1].append(difs[-1][-1])
		else:
			ti = len(difs)-i-1
			difs[ti].append(difs[ti][-1]+difs[ti+1][-1])
	nextVal = pseq[-1]+difs[0][-1]
	testctr = len(pseq)
	while nextVal == seq[testctr]:
		testctr+=1
		for i in range(0,len(difs)):
			if i == 0:
				difs[-1].append(difs[-1][-1])
			else:
				ti = len(difs)-i-1
				difs[ti].append(difs[ti][-1]+difs[ti+1][-1])
		nextVal = pseq[-1]+difs[0][-1]
		testctr = len(pseq)
	return nextVal

def main():
	t0 = time()
	iseq = generateInitialSequence()
	print(iseq)
	ssum = 0
	for i in range(0,10):
		ssum += findFit(i,iseq)
	print("Time Elapsed:", time()-t0)
	print(ssum)

main()