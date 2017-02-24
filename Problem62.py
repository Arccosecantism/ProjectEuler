 
import math
from time import time

def intToDigitAmounts(x):
    #converts an integer to a list of digits
    diglist = [0]*10
    tx = x
    while tx >= 1:
        diglist[tx%10] += 1
        tx = int(tx/10)
    return diglist


def main():
    #The Strategy: we essentally count up the natural numbers, storing them and the amount of each number 0-9 in their cubes' digits.
    #But before we store, if there was already a number with the same digits in the cube, we remember that. We use some clever storage using the 
    #number of digits in the cube and the largest digit in the digits of the cube to make it easier to search the list, because we have to do this
    #every time we look at a new integer. Executes in 1.51 seconds
    t0 = time()
    done = False
    goodIndex = [-1,-1,-1]
    cubeCtr = 1
    digitLists = [[]]
    while not(done):
        tdl = intToDigitAmounts(cubeCtr*cubeCtr*cubeCtr)
        
        digLen = 0
        longestDigit = 0
        for i in range(0,len(tdl)):
            digLen += tdl[i]
            if tdl[i] >= longestDigit:
                longestDigit = i
       # print(cubeCtr, tdl, longestDigit, digLen)

        if len(digitLists) == digLen:
            digitLists.append([[],[],[],[],[],[],[],[],[],[]])
        found = False
        for i in range(0,len(digitLists[digLen][longestDigit])):
            if digitLists[digLen][longestDigit][i][0] == tdl:
                found = True
                digitLists[digLen][longestDigit][i][2] += 1
                digitLists[digLen][longestDigit][i][1].append(cubeCtr)
                if digitLists[digLen][longestDigit][i][2] == 5:
                    done = True
                    goodIndex = [digLen,longestDigit,i]
                break
        if not(found):
            digitLists[digLen][longestDigit].append([list(tdl), [cubeCtr], 1])
        cubeCtr += 1

    ans = digitLists[goodIndex[0]][goodIndex[1]][goodIndex[2]][1][0]**3
    print("Time Elapsed:", time()-t0)
    print(ans)
main()