#Problem: 	Let the letter-sum of a name be the sum of the positions of its letters: so "RILEY" would be 18+9+12+5+25 = 69
#			Now, sort alphabetically the list of names in NamesProblem22.txt and let the score of a name be its position in the list
#			multiplied by its letter-sum. What is the sum of the scores of all the names in the list?

import math
import os


def removeNonAlphabetical(str):
	#remove non-alphabetic characters from a string
	nstr = ""
	for i in str:
		if (i >= 'a' and i <= 'z') or (i >= 'A' and i <= 'Z'):
			nstr += i
	return nstr
	
def getNameArray():
	#reads the files and provides the list of strings
	print(os.getcwd())
	f = open("TextFiles\NamesProblem22.txt", 'r')
	lines = f.read()
	names = lines.split('\",\"')
	for i in range(0, len(names)):
		names[i] = removeNonAlphabetical(names[i])
	return names

def isNameFormer(stra, strb):
	#determines relative greatness based on alphabetic order: 'aab' is 'less' than 'bac'
	done = 0
	yes = 0
	ctr = 0
	while not(done):
		if stra[ctr] < strb[ctr]:
			yes = 1
			done = 1
		elif stra[ctr] > strb[ctr]:
			yes = 0
			done = 1
		else:
			ctr += 1
			if ctr >= len(stra) or ctr >= len(strb):
				if len(stra) >= len(strb):
					yes = 0
					done = 1
				else:
					yes = 1
					done = 1
	return yes
				
				
def mergeSortNames(nameArray):
	#merge sort cuz bubble sort is garbage -- at 5000 names, it may make a difference
	if len(nameArray) > 1:
		ar1 = []
		ar2 = []
		hwp = int(len(nameArray)/2)
		for i in range(0,hwp):
			ar1.append(nameArray[i])
		for i in range(hwp, len(nameArray)):
			ar2.append(nameArray[i])
		
		ar1 = mergeSortNames(ar1)
		ar2 = mergeSortNames(ar2)
		
		nar = []
		ctr1 = 0
		ctr2 = 0
		while ctr1 < len(ar1) and ctr2 < len(ar2):
			if isNameFormer(ar1[ctr1], ar2[ctr2]):
				nar.append(ar1[ctr1])
				ctr1 += 1
			else:
				nar.append(ar2[ctr2])
				ctr2 += 1
		if ctr1 < len(ar1):
			for i in range(ctr1, len(ar1)):
				nar.append(ar1[i])
		elif ctr2 < len(ar2):
			for i in range(ctr2, len(ar2)):
				nar.append(ar2[i])
		return nar
	else:
		return nameArray


	
def main():
	#merge sort the names, go through the list, construct the scores, and sum them
	
	names = getNameArray()
	names = mergeSortNames(names)
	bsum = 0
	for i in range(0,len(names)):
		lsum = 0
		for k in names[i]:
			lsum += ord(k) - ord('A') + 1
		ltot = lsum * (i + 1)
		bsum += ltot
	print(bsum)

main()


