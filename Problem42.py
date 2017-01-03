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

def getTriangleList(x):
    ar = []
    for i in range(0,x):
        ar.append(0)
    ctr = 0
    tri = 0
    while tri < x:
        ar[tri]=1
        ctr+=1
        tri+=ctr
    return ar

def isTriangular(x,trilist):
    trian = 0
    if trilist[x] == 1:
        trian = 1
    return trian

def getWordSum(word):
    ssum = 0
    for i in word:
        ssum += ord(i)-ord('A')+1
    return ssum

def main():
    t0 = time()
    wordList = getWordList()
    triagleList = getTriangleList(600)
    #print(wordList)
    #print(triagleList)
    count = 0
    for i in wordList:
        if isTriangular(getWordSum(i), triagleList):
            count += 1
    print("Time Elapsed:", time()-t0)
    print(count)

main()