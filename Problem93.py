import math


def getPermutations(nlist):
    #returns all orderings of a list
    results = []
    empty = True
    for i in range(0,len(nlist)):
        empty = False
        val = nlist[0]
        del(nlist[0])
        nr = getPermutations(nlist)
        for j in nr:
            results.append(list([val]+j))
        nlist.append(val)
    if empty:
        return [[]]
    else:
        return results


def generateOperationList():
    ol = []
    for i in range(0,4):
        for j in range(0,4):
            for k in range(0,4):
                ol.append((i,j,k))
    return ol

def addf(a,b):
    return a+b
def subtractf(a,b):
    return a-b
def multiplyf(a,b):
    return a*b
def dividef(a,b):
    if b == 0:
        return 9.183602
    return a/b
def evaluate(func,a,b):
    return func(a,b)

def generatePossibleNumbersChain(valList,opPrecs,opList,opMap):
    possibleNumsSet = set([])
    numOrderings = getPermutations(valList)
    for v in numOrderings:
        for i in opList:
            for j in opPrecs:

                changeOne = False
                tval = list(v)
                for k in j:
                    nk = 0
                    if k == 0:
                        nk = 0
                        changeOne = True
                    if k == 2:
                        nk = len(tval)-2
                    if k == 1:
                        nk = 1
                        if changeOne:
                            nk = 0
                    #print("here", k, nk)
                    ktv = evaluate(opMap[i[k]],tval[nk],tval[nk+1])
                    #if v == [4,3,1,2] and i == (2,1,2) and j == (0,1,2):
                    #    print("here", ktv, tval[nk], tval[nk+1])
                    del tval[nk]
                    del tval[nk]
                    tval.insert(nk,ktv)
                
                if tval[0] == int(tval[0]):
                    if tval[0] >= 1:
                        possibleNumsSet.add(tval[0])

    possibleNums = list(possibleNumsSet)
    possibleNums.sort()
    
    #print(possibleNums)
    chain = 0
    maxChainFound = False
    expected = 1 
    for i in possibleNums:
        if not(maxChainFound):
            if i == expected:
                chain += 1
                expected += 1
            elif i != expected - 1:
                maxChainFound = True
        else:
            break

    return chain
    
def main():
    funcList = [addf,subtractf,multiplyf,dividef]
    operationList = generateOperationList()
    operationPrecedences = [(0,1,2),(0,2,1),(1,0,2),(1,2,0),(2,0,1),(2,1,0)]
    print(generatePossibleNumbersChain([1,2,5,8],operationPrecedences,operationList,funcList))
    '''bestChain = 0
    bestTuple = (-1,-1,-1,-1)
    for a in range(0,7):
        for b in range(a+1,8):
            for c in range(b+1,9):
                for d in range(c+1,10):
                    tchain = generatePossibleNumbersChain([a,b,c,d],operationPrecedences,operationList,funcList)
                    if tchain > bestChain:
                        bestChain = tchain
                        bestTuple = (a,b,c,d)
                        print(bestTuple, bestChain)
    print(bestTuple, bestChain)'''
main()