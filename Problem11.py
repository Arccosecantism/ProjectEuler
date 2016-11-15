#Problem: 	What is the greatest product of four numbers in a line (up, down, left, right, diagonal) 
#			in the table shown in yellow at line 29?

import math



def twoDigStrToInt(str):
	if len(str) != 2:
		return 0
		
	return 10*ctoi(str[0])+ctoi(str[1])

def ctoi(cha):
	#char to int
	return ord(cha) - ord('0')

def removeNonNumerics(str, spec):
	nstr = ""
	for i in str:
		if (ord(i) >= ord('0') and  ord(i) <= ord('9')) or i == spec :
			nstr+=i
	return nstr

def getNumArray():
	#this function is really cancerous and gimmicky and shows
	#that I don't know a lot of the functions and syntax in python
	#It just converts the (string) list of number to an actual array of ints
	begStr = 	'''08 02 22 97 38 15 00 40 00 75 04 05 07 78 52 12 50 77 91 08c
				49 49 99 40 17 81 18 57 60 87 17 40 98 43 69 48 04 56 62 00c
				81 49 31 73 55 79 14 29 93 71 40 67 53 88 30 03 49 13 36 65c
				52 70 95 23 04 60 11 42 69 24 68 56 01 32 56 71 37 02 36 91c
				22 31 16 71 51 67 63 89 41 92 36 54 22 40 40 28 66 33 13 80c
				24 47 32 60 99 03 45 02 44 75 33 53 78 36 84 20 35 17 12 50c
				32 98 81 28 64 23 67 10 26 38 40 67 59 54 70 66 18 38 64 70c
				67 26 20 68 02 62 12 20 95 63 94 39 63 08 40 91 66 49 94 21c
				24 55 58 05 66 73 99 26 97 17 78 78 96 83 14 88 34 89 63 72c
				21 36 23 09 75 00 76 44 20 45 35 14 00 61 33 97 34 31 33 95c
				78 17 53 28 22 75 31 67 15 94 03 80 04 62 16 14 09 53 56 92c
				16 39 05 42 96 35 31 47 55 58 88 24 00 17 54 24 36 29 85 57c
				86 56 00 48 35 71 89 07 05 44 44 37 44 60 21 58 51 54 17 58c
				19 80 81 68 05 94 47 69 28 73 92 13 86 52 17 77 04 89 55 40c
				04 52 08 83 97 35 99 16 07 97 57 32 16 26 26 79 33 27 98 66c
				88 36 68 87 57 62 20 72 03 46 33 67 46 55 12 32 63 93 53 69c
				04 42 16 73 38 25 39 11 24 94 72 18 08 46 29 32 40 62 76 36c
				20 69 36 41 72 30 23 88 34 62 99 69 82 67 59 85 74 04 36 16c
				20 73 35 29 78 31 90 01 74 31 49 71 48 86 81 16 23 57 05 54c
				01 70 54 71 83 51 54 69 16 92 33 48 61 43 52 01 89 19 67 48'''
	spec = 'c'    #there must be a better way to do this
	begStr = removeNonNumerics(begStr, spec)

	numStrArray = [[]]
	ctr = 0
	tstr = ""
	
	for i in begStr:
		
		if i == spec:
			numStrArray.append([])
			ctr+= 1

			
		else:	
			tstr += i
			if len(tstr) == 2:
				numStrArray[ctr].append(tstr)
				tstr = ""
			
	numArray = []
	ctr = 0
	for i in numStrArray:
		numArray.append([])
		
		for k in i:
			
			numArray[ctr].append(twoDigStrToInt(k))
			
		ctr += 1
		
	return numArray
			
#----------------------------------



def isInBounds(r, c, tdArray):

	return not(r < 0 or r >= len(tdArray) or c < 0 or c >= len(tdArray[0]))
			
def main():
	#go through each cell, check all the products in all directions, essentially
	
	
	
	#print(removeNonNumerics("asd78362  jksad234998 ty .,dsds}431"))
	dist = 4
	numArray = getNumArray()
	largest = 0
	product = 1
	
	directions = [[0,1], [1,1], [1,0], [-1, 1]]
	for i in range(0, len(numArray)):
		for k in range(0, len(numArray[i])):
			for d in directions:
				if isInBounds((i+(dist-1)*d[0]), (k+(dist-1)*d[1]), numArray):
					for c in range(0,dist):
						ip = i + c*d[0]
						kp = k + c*d[1]
						product *= numArray[ip][kp]
					if product>largest:
						largest = product
					product = 1	
	print(largest)
						
	



main()


