
def getFactorList(x):
    #Produces a list of numbers under x, also tells if they are prime.
    #this is to create an O(1) prime checker for primes under x 
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
    print(firstIndx)

main()