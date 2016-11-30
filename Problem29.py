
#Problem: 	for all a and b : 2<=a<=100, 2<=b<=100; how many distinct values are there of a^b? see https://projecteuler.net/problem=29

import math
from time import time

def getNonPowers(x):
	#gives the array of all non-squares, cubes, hypercubes, etc. under x  and greater than 1.
	#so g(10) = [2,3,5,6,7,10]
	ar = []
	npar = []
	for i in range(1,x):
		ar.append([i+1, 0])
		
	for i in range(0,x-1):
		if ar[i][1] == 0:
			npar.append(i+2)
			for k in range(i+1,x-1):
				if math.log(k+2, i+2) == int(math.log(k+2, i+2)): 
					# print(k+2, i+2)
					ar[k][1] = 1
	return npar

def genPowersUnder(base, cap):
	#gives all of the powers of base under or equal to cap
	#so g(2,20) = [2,4,8,16]
	par = []
	product = base
	while product <= cap:
		par.append(product)
		product *= base
	return par

def getGoodFactors(x, power):
	#gives all "good" factors -- pertty confusing: it's very specified for the problem at hand
	#what it really gives is all other integer powers >2 that equal (k^power)^x. So, g(12, 2) = [1.5,2,3,4,6] 
	# because (k^2)^12 = (k^(2*1.5))^8, (k^(2*2))^6, (k^(2*3))^4, and (x^(2*6))^2
	flist = []
	tx = power * x
	ctr = 2
	done = 0
	while not(done):
		if not(tx%ctr):
			#print(tx, ctr)
			sf = ctr
			bf = int(tx/ctr)
			if sf < bf:
				flist.append(sf)
				flist.append(bf)
			elif sf == bf:
				flist.append(sf)
			else:
				done = 1
		ctr += 1
	nflist = []
	for i in range(0,len(flist)):
		tmp = float(flist[i])/power
		if tmp > 1:
			nflist.append(tmp)
	return nflist

def findUniquesInFamily(fam, cap):
	#Finds the number of uniques powers in a given power family under a cap.
	#For instance, when considering the power of 2 family under 10, that is f(2,10), 
	#this will exclude 4^2, because it = 2^4. It ill also exclude 4^3, 4^4, 4^5, as they are 2^6, 2^8, 2^10
	#this will also exclude 8^2, because 8^2 = 2^6, etc. It finds all of the duplicates and counts the unique ones
	powers = genPowersUnder(fam, cap)
	familyArray = []
	maxExp = len(powers)
	for i in powers:
		familyArray.append([])
		for k in range(2,cap+1):
			familyArray[-1].append([i,k,0])
 
	for i in range(0, len(familyArray) - 1):
		for k in familyArray[i]:
			if k[2] == 0:
				factors = getGoodFactors(k[1], i+1)
				for j in factors:
					ni = int((i+1)*j -1)
					if j <= maxExp and ni < len(familyArray):
						#print(i, k, int(j), int(k[1]/j), familyArray[ni][int(k[1]/j)-2])
						familyArray[ni][int(k[1]/j)-2][2] = 1
						#print(familyArray[ni][int(k[1]/j)-2])
	total = 0
	for i in familyArray:
		for k in i:
			#print(k)
			if k[2] == 0:
				total += 1
	return total


def main():
 #This is quite easy -- the diagonals are sums of odd squares minus a multiple of 2, which is (2n-1)(2n)(2n+1)/6
 #We jsut count up the square sums and subtract off the multiples of 2, and subtract 3 because having one 1 in the center 
 #is weird and throws things off. Takes 0.0 seconds to execute
	tic = time()
	num = 100
	uniques = 0
	nonPowers = getNonPowers(num) 
	#print(getGoodFactors(12,2))
	for i in nonPowers:
		uniques += findUniquesInFamily(i,num) 
		
	print("Time Elapsed: ", time() - tic)
	print(uniques)

main()