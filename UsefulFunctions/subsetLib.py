def generateSubsetsWeird(siz, numlist):
    #Recursively gets all siz-sized subsets of a number list: so (2,[[1,1],[2,1],[3,1]])) = [[1,2],[1,3],[2,3]]
    #The number list is a bit confusing -- it is all the umbers you want in a pair with 1: so
    #If you want subsets of {3,6,7}, the number list used is [[3,1],[6,1],[7,1]] -- works better for 
    #recursion
    newlist = []
    if siz > 0:
        for i in range(0,len(numlist)):
            if numlist[i][1] == 1 and len(numlist)-i >= siz :
                for k in range(0,i+1):
                    numlist[k][1] = 0 
                nextstep = generateSubsetsWeird(siz-1, numlist)
                for k in nextstep:
                    al = [numlist[i][0]]
                    bl = list(k)
                    cl = al+bl
                    newlist.append(list(cl)) 
                for k in range(0,i+1):
                    numlist[k][1] = 1 
    else:
        newlist.append([])
    return newlist

def generateCleanSubsets(siz, numlist):
    #simply calls generateSubsetsWeird but the numlist is easier: [5,6,7,8] is an acceptable input,
    #and it gets translated to [[5,1],[6,1],[7,1],[8,1]]
    nlist = []
    for i in numlist:
        nlist.append([i,1])
    badSets = generateSubsetsWeird(siz, nlist)
   
    return badSets

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

            
def getCyclicalPermutations(nlist):
    #gets all orderings of a list, but only the ones that are different in order accross rotation:
    #so if nlist = [3,6,8], [8,3,6] is the same as [6,8,3] as two orderings, but [8,6,3] is different
    cperm = []
    start = nlist[0]
    tnl = nlist[1:]
    nr = getPermutations(tnl)
    for i in nr:
        cperm.append(list([start]+i))
    return cperm


def multiplyLists(alist, listlist):
    #confusing: takes a list and a list of lists and combines them in a multiplicative way:
    #M([3,2,1], [[0,4,5], [], [1,2]]) = [[3,2,1,0,4,5], [3,2,1], [3,2,1,1,2]]
    nlist = []
    for i in range(0,len(listlist)):
        tmplista = list(alist)
        tmplistb = list(listlist[i])
        nlist.append(list(tmplista+tmplistb))
    return nlist

def getPermutationsRepeats(numList):
    #recursively gets all permutations with no duplicates of an array describing the amount of digits.
    #So GP([[1,1],[3,2]]) = [[1,3,3], [3,1,3], [3,3,1]]
    nlist = []
    empty = 1
    for k in numList:
        if k[1] >= 1:
            empty = 0
            k[1] -= 1
            tmplist = []
            tmplist.append(k[0])
            branches = multiplyLists(tmplist,getPermutationsRepeats(numList))
            k[1] += 1   
            for j in branches:
                nlist.append(j)
    if empty == 1:
        nlist.append([])
    return nlist

def powerset(tset):
    #generates the powerset of a list without repeats
    sl = int(len(tset))
    print(sl)
    tlist = list(tset)
    print(tlist)
    pset = set([])
    for i in range(2**sl-1):
        tx = i
        subset = set([])
        ctr = 0
        while tx:
            if tx&1:
                subset.add(tlist[ctr])
            ctr += 1
            tx >>= 1
        print(i,subset)
        pset.add(frozenset(subset))
    return pset