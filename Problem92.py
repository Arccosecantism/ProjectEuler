

def getDigitSquareSum(x):

    #gets the sum of the factorials of x's digits
    
    ssum = 0
    sx = str(x)
    for i in sx:
        ssum += int(i)*int(i)
    return ssum

def factorial(x):
    #factorial function
    if x == 0 or x == 1:
        return 1
    else:
        return x*factorial(x-1)

def digitFamilyToNum(fam):
    #gets a member of a "family" of numbers that contains all numbers that are just reorderings of digits 
 
    ssum = 0
    for k in range(0,len(fam)):
        exp = len(fam)-k-1
        ssum+=(fam[k]*(10**exp))

    return ssum

def getNumberOfOrders(digar):
    #from a list of numbers, tells how many unique reorderings of the numbers there are
    
    bl = len(digar)
    prod = factorial(bl)
    
    sd = list(digar)
    sd.sort()

    reps = [0] * len(digar)
    lastval = sd[0]
    val = -1
    chain = 0
    for i in range(0,len(sd)):
        val = sd[i]
        if lastval == val:
            chain += 1
        else:
            reps[chain-1] += 1
            chain = 1
        lastval = val
    reps[chain-1]+=1
    for i in range(0,len(reps)):
        if reps[i]:
            prod //= (factorial(i+1)**reps[i])
    #print(reps)
    return prod


def generateSubsets(siz, numlist):
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
                nextstep = generateSubsets(siz-1, numlist)
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
    
def getDigitsStarsBars(stars):
    #hard to explain -- gets all possible digit lists of a certain length that can be reordered to obtain
    #all possible numbers that are <stars> long
    bars = 10
    proList = [0]*(stars+bars-1)
    nlist = [[i,1] for i in range(0,stars+bars-1)]
    subs = generateSubsets(bars-1, nlist)
    digitLists = []
    for i in subs:
        tl = list(proList)
        for k in i:
            tl[k]=1 
        td = []
        ctr = 0
        
        requireda = False
        requiredb = False
        for k in range(0,len(tl)):
            if tl[k] == 0:
                td.append(ctr)
            else:
                ctr+=1
        
        digitLists.append(td)
    return digitLists

def main():
    
    digitFamilies = getDigitsStarsBars(7)
    squareSumList = [0]*244
    for i in range(1,244):
        if i == 89:
            squareSumList[i] = 89
        else:
            squareSumList[i] = getDigitSquareSum(i)

    for i in range(1,244):
        while squareSumList[i] != 89 and squareSumList[i] != 1:
            squareSumList[i] = squareSumList[squareSumList[i]]
    #print(squareSumList)

    ssum = 0
    #testAr = [0,0,0,0,0,1,1]
    #print(testAr, getNumberOfOrders(testAr))
    for i in digitFamilies:
        fac = getNumberOfOrders(i)
        occ = digitFamilyToNum(i)
        #print(i,occ,fac)
        start = getDigitSquareSum(getDigitSquareSum(occ))
        if squareSumList[start] == 89:
            ssum += fac
    print(ssum)
main()