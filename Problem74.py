import math
from time import time

def getDigitFactorialSumTrue(x):
    facs = [1]
    for i in range(1,10):
        facs.append(i*facs[-1])
    
    sx = str(x)
    ssum = 0
    for i in sx:
        ssum += facs[int(i)]
    return ssum


    

def main():
    longest = 0
    longestVal = 0

    ar = []
    for i in range(0,2200001):
        if not(i%10000):
            print (i)
        ar.append([0,0])
    print(ar[0])
    for i in range(1,1000001):
        ctr = 1
        nnum = i
        end = False
        visitedNumbers = []
        while not(end):
        
            if nnum >= len(ar):
                print("bigger?")
                nnum = getDigitFactorialSumTrue(nnum)
            else:
                if ar[nnum][1] == 1:

                    if nnum == 0:
                            print(i,nnum,"Zero?")
                    #print("a",i,nnum,ar[nnum])
                    end = True
                    ar[0][1] = 0
                    for j in visitedNumbers:
                        
                        ar[j][1] = 0
                        #print ("b",i,ar[j])
                    

                else:       
                    if ar[nnum][0] == 0:
                        ar[nnum][1] = 1
                        #print("c",i,nnum,ar[nnum])
                        pn = nnum
                        #print(pn)
                        nnum  = getDigitFactorialSumTrue(nnum)
                        #print(pn,nnum)
                        if nnum == 0:
                            print(i,nnum,"Zero?")
                        ar[pn][0] = nnum
                        #print("d",i,nnum,ar[pn])
                    else:
                        ar[nnum][1] = 1
                        nnum = ar[nnum][0]
                        if nnum == 0:
                            print(i,nnum,"Zero?")
                    
                    visitedNumbers.append(nnum)
                    ctr += 1
    
            
                
        if ctr > longest:
            longestVal = nnum
            longest = ctr 
        if not(i%10000):
            print(i)
    print(longestVal)


main()