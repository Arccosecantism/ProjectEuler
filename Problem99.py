#Problem: in the text file, there are 6-digit numbers raied to other 6th digit powers. On each line, there is 1 base-exponent pairs
#           We need to find which line has the biggest base-exponent pair

import math

def getBaseExponentPairs():
    #gets the pairs from the text file
    f = open("TextFiles\\BaseExponentPairsProblem99.txt", 'r')
    lines = f.read()
    nums = lines.split("\n")
    #print(nums)
    pairs = []
    for i in nums:
        tp = i.split(",")
        pairs.append((int(tp[0]),int(tp[1])))
    
    return pairs


def main():
    #The Strategy: very easy problem here: use ln(ln(b^c)) = ln(c)+ln(ln(b)) to continuously reduce the base-exponent pair to a reasonable size,
    #then compare
    pairList = getBaseExponentPairs()
    maxVal = 0
    maxIndx = -1
    for i in range(len(pairList)):
        val = math.log(math.log(pairList[i][0]))+math.log(pairList[i][1])
        if val > maxVal:
            maxVal = val
            maxIndx = i
    print(maxIndx+1)
main()