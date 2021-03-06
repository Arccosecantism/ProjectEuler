
#Problem:  https://projecteuler.net/problem=98
import math
from time import time

def getWords():
    #gets toe words from a text file
    f = open("TextFiles\\WordListProblem98.txt", 'r')
    lines = f.read()
    words = lines.split("\",\"")
    words[0] = words[0][1:]
    words[-1] = words[-1][:-1]
    return words

def mergeList(alist, blist, compFunc):
    #merges two lists -- part of merge sort.
    #compares using an arbitrary compare function
    actr = 0
    bctr = 0
    nlist = []
    while actr < len(alist) or bctr < len(blist):

        if actr == len(alist):
            cb = blist[bctr]
            nlist.append(cb)
            bctr += 1
        elif bctr == len(blist):
            ca = alist[actr]
            nlist.append(ca)
            actr += 1
        else:
            ca = alist[actr]
            cb = blist[bctr]
            if compFunc(ca,cb):
                nlist.append(ca)
                actr+=1
            else:
                bctr += 1
                nlist.append(cb)
    return nlist

def mergeSort(alist, compFunc):
    #A general merge sort 
    if len(alist) > 1:
        hp = len(alist)//2
        leftList = alist[:hp]
        rightList = alist[hp:len(alist)]
        leftList = mergeSort(leftList, compFunc)
        rightList = mergeSort(rightList, compFunc)
        return mergeList(leftList, rightList, compFunc)
    else:
        return alist

def compareFunction(a,b):
    #greater than compare function
    if a > b:
        return False
    return True

def getAlphaValue(cx):
    #gets alphabetical value of a character: 'a'->0, 'b'->1
    #'A' -> 0, 'Z' -> 25, numbers are "greater" than letters 
    if cx >= 'a' and cx <= 'z':
        return ord(cx)-ord('a')
    elif cx >= 'A' and cx <= 'Z':
        return ord(cx)-ord('A')
    elif cx >= '0' and cx <= '9':
        return ord(cx)-ord('0')+26
    else:
         return ord(cx)+36

def checkFirstAlphabetically(strx, stry):
    #checks if a string is previous alphabetically to another string -- 
    #if two identical strings are input, it will treat it as "not previous"
    if stry == "":
        return False
    elif strx == "":
        return True

    avx = getAlphaValue(strx[0])
    avy = getAlphaValue(stry[0])
    if  avx > avy:
        return False
    elif avx < avy:
        return True
    else:
        return checkFirstAlphabetically(strx[1:], stry[1:])

def checkOrderedAlpha(strx,stry):
    #checks for two strings, when completely orderered alphabetically, which one is first alphabetically 
    sx = ''.join(mergeSort(strx, checkFirstAlphabetically))
    sy = ''.join(mergeSort(stry,checkFirstAlphabetically))
    return checkFirstAlphabetically(sx,sy)

def specialAlphaCompare(valx, valy):
    #cpompares a string based on the alphabetic predcedence of the seconds char
    return checkFirstAlphabetically(valx[1], valy[1])

def getOrderedStr(strx):
    #returns a string, sorted alphabetically by letter
    return ''.join(mergeSort(strx, checkFirstAlphabetically))


def getReducedAnagrams(alist):
    #from a list of anagrams, gets all position transformations -- generalizes the concept of an anagram
    reducedAnagramList = []
    for i in alist:
        for par in range(2):
            wa = i[0+par]
            wb = i[1-par]
            assigner = []
            for j in wa:
                if not(j in assigner):
                    assigner.append(j)
 
            transList = []
            for j in wb:
                val = -1
                for k in range(len(assigner)):
                    if j == assigner[k]:
                        val = k
                transList.append(val)

            signature = []
            for j in wa:
                val = -1
                for k in range(len(assigner)):
                    if j == assigner[k]:
                        val = k
                signature.append(val)
                
            reducedAnagramList.append([signature,transList])
    return reducedAnagramList


def getWordAnagrams(wordList):
    #from a word list, gets all anagrams
    maxWordLength = 0
    for i in wordList:
        if len(i) > maxWordLength:
            maxWordLength = len(i)


    lengthWordLists = [[]]
    for i in range(maxWordLength):
        lengthWordLists.append([])
    anagramList = []
    

    for i in wordList:
        lengthWordLists[len(i)].append(i)
    for i in range(len(lengthWordLists)):
        orderList = []
        for j in lengthWordLists[i]:
            orderList.append((j,getOrderedStr(j)))
        orderList = mergeSort(orderList, specialAlphaCompare)
        for j in range(len(orderList)-1):
            if orderList[j][1] == orderList[j+1][1]:
                anagramPair = (orderList[j][0], orderList[j+1][0])
                anagramList.append(anagramPair)
    return anagramList
    



def generateSquares(maxLength):
    #generates a list of squares, separated by digit-amount, up to a maximum length
    lenctr = 0
    squareLists = [[]]
    for i in range(maxLength):
        squareLists.append([])
    sqctr = 0
    fd = 1
    sd = 2
    while len(str(sqctr)) <= maxLength:
        tl = len(str(sqctr))
        squareLists[tl].append(str(sqctr))
        sqctr += fd
        fd += sd
    print(len(squareLists))
    return squareLists


def testReducedAnagram(ang, squarestr):
    #tests if a square, after undergoig a character transformation that would result in an anagram if applied to another word, is still a square 
    if len(ang[0]) != len(squarestr):
        return False
    numAsg = []
    for i in squarestr:
        if not(i in numAsg):
            numAsg.append(i)
    
    numSig = []
    for i in squarestr:
        val = -1
        for j in range(len(numAsg)):
            if i == numAsg[j]:
                val = j
        numSig.append(val)
    

    if numSig != ang[0]:
        return False

    newNumStr = ""
    for i in ang[1]:
        newNumStr += numAsg[i]
    newNum = int(newNumStr)
    sqn = math.sqrt(newNum)
    if abs(sqn-int(sqn)) < .000001:
        if len(str(newNum)) != len(squarestr):
            return False
        return True
    return False 
    
def main():
    #The strategy: we get all the words, find all the anagram pairs, reduce the lsit to the actual transfrmations from one anagram to the next, and 
    #see if those transformations also apply to square numbers, transforming them into other squares. Keep track of the largest square
    #Executes in 3.156 seconds
    t0 = time()
    reducedAnagrams = getReducedAnagrams(getWordAnagrams(getWords()))
    maxLength = 0
    for i in reducedAnagrams:
        if len(i[0]) > maxLength:
            maxLength = len(i[0])
    
    squareLists = generateSquares(maxLength)
    print(testReducedAnagram([[0,1,2,3],[2,1,0,3]], "9216"))
    maxNum = 0
    for i in reducedAnagrams:
        tl = len(i[0])
        for j in squareLists[tl]:
            ix = int(j)
            if ix > maxNum:
                testResult = testReducedAnagram(i,j)
                if testResult:
                    print(i, ix, math.sqrt(ix))
                    maxNum = ix
    print("Time Elapsed:  " + str(time()-t0))
    print(maxNum)

   
main()

