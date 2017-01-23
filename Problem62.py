 
import math
from time import time

def intToDigitAmounts(x):
    diglist = [0]*10
    tx = x
    while tx >= 1:
        diglist[tx%10] += 1
        tx = int(tx/10)
    return diglist


def main():
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