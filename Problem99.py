import math

def getBaseExponentPairs():
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