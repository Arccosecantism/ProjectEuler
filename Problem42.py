#Problem: a triangle number is a number that can be written as n(n+1)/2. For a word, the word value is the sum of the alphabetical 
#placement of the letters in the word. So "SKY" is 19+11+25 = 55. This happens to be a triangle number. How many of the words in the given list
#of words have triangular word values?

import math
import os
from time import time


def removeNonAlphabetical(str):
	#remove non-alphabetic characters from a string
	nstr = ""
	for i in str:
		if (i >= 'a' and i <= 'z') or (i >= 'A' and i <= 'Z'):
			nstr += i
	return nstr
	
def getWordList():
	#reads the files and provides the list of strings
	print(os.getcwd())
	f = open("TextFiles\WordListProblem42.txt", 'r')
	lines = f.read()
	names = lines.split('\",\"')
	for i in range(0, len(names)):
		names[i] = removeNonAlphabetical(names[i])
	return names

def isTriangular(x):
    if math.sqrt(8*x+1)%2 == 1:
        return 1
    return 0

def getWordSum(word):
    ssum = 0
    for i in word:
        ssum += ord(i)-ord('A')+1
    return ssum

def main():
    t0 = time()
    wordList = getWordList()
    #print(wordList)
    #print(triagleList)
    count = 0
    for i in wordList:
        if isTriangular(getWordSum(i)):
            count += 1
    print("Time Elapsed:", time()-t0)
    print(count)

main()