#The Problem: consider the function s(x) where s(x) is the sum of the divisors of x. An amicable chain is a sequence of numbers a1,a2,a3,...,an
#               such that a2=s(a1), a3=s(a2) ... a((k+1)%n)=s(a(k)) for k<=n (wraps around). Find the smallest member of the amicable chain
#               of the greatest length with all terms under 1 million
#  
from time import time
def getFactorList(x):
    #Produces a list of numbers under x, also shows all factors of those numbers.
    ar = []
    flick = True
    for i in range(-1,x):
        if flick and i != -1:
            ar.append([1,2])
        else:
            ar.append([1])
        flick = not(flick)
    
    ub = int(x/2)+1
    for i in range(3,ub):
        for k in range(2*i,x,i):
            ar[k].append(i)
    return ar

def main():
    #The strategy: we first create a list of numbers that contain another number: s(x) Now we can traverse the list easily and we never have to find s(x)
    #               again. Then, we simply check every number whose factor sum s(x) is greater than itself -- all abundant numbers, and we try to find
    #               the chain length. We keep track of the largest chain and return the smallest element of that chain

    #Executes in 17.7 seconds
    t0 = time()
    cap = 1000000
    bigFactorList = getFactorList(cap+10)
    factorSums = [0]*(cap+1)
    chainLengths = [0]*(cap+1)
    for i in range(0,cap+1):
        factorSums[i] = sum(bigFactorList[i])
    for i in range(2,cap+1):
        if factorSums[i] > i:
            val = i
            returnCheck = set([])
            returnTo = i
            ctr = 0
            done = False
            fail = False
            while not(done):
                
                
                ctr += 1
                val = factorSums[val]
                #print(val)
                if val > cap:
                    done = True
                    fail = True
                elif val in returnCheck:
                    done = True
                    fail = True
                elif val == returnTo:
                    done = True
                if done == False:
                    returnCheck.add(val)
            if not(fail):
                for j in returnCheck:

                    chainLengths[j] = ctr
    #print(chainLengths)
    mcl = 0
    for i in chainLengths:
        if i > mcl:
            mcl = i
    #print(mcl)
    firstIndx = 0
    for i in range(0,len(chainLengths)):
        if chainLengths[i] == mcl and firstIndx == 0:
            firstIndx = i
            break
    #print(chainLengths[284])
    #print(chainLengths[12496])
    print("Time Elapsed:  " + str(time()-t0))
    print(firstIndx)

main()