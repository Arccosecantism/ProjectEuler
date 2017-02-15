

def gcf(x,y):
    #Euclid's method for finding greatest common factor
    a = max(x,y)
    b = x+y-a
    r = 2
    while r:
        r=a%b
        a=b
        b=r
    return a

def primeFactorSieve(x):
    #Produces a list of numbers under x, also tells if they are prime.
    #this is to create an O(1) prime checker for primes under x 
    ar = []
    for i in range(-1,x):
        ar.append([])
    
    ub = int(x/2)+1
    for i in range(2,ub):
        if ar[i] == []:
            for k in range(i,x,i):
                ar[k].append(i)
    for i in range(2,x+1):
        if ar[i] == []:
            ar[i] = [i]
    return ar

def generateSomeCoprimeNumbers(x, pfs, under):
    numList = [1]*under
    if x&1:
        for i in range(0,len(numList)):
            if not(i&1):
                numList[i] = 0
    facs = pfs[x]
    for i in facs:
        for k in range(0,len(numList)):
            if not((k+1)%i):
                numList[k] = 0
    for i in range(0, len(numList)):
        if i+1 <= x:
            numList[i] = 0
    goodList = []
    for i in range(0,len(numList)):
        if numList[i] == 1:
            goodList.append(i+1)
    return goodList
    



def main():
    sieve = primeFactorSieve(1000000)
    ptripSums = []
    for i in range(1,870):
        cnums = generateSomeCoprimeNumbers(i,sieve,870)
        for k in cnums:
            ptripSums.append(2*k*k+2*k*i)

    sumList = [0]*1500001
    for i in ptripSums:
        ssum = i
        bsum = ssum
        while bsum <= 1500000:
            sumList[bsum] += 1
            bsum += ssum
    fsum = 0
    for i in range(0,len(sumList)):
        if sumList[i] == 1:
            fsum += 1
            #print(sumList[i],i)
    print(fsum)

main()