#Problem: just like triangle and square numbers, there are also pentagonal numbers. The formula for the nth pentagonal
#           number is n(3n-1)/2. find the pair of pentagonal numbers such that their sum and difference are both
#           pentagonal, and the difference is minimized. What is their difference?

import math
from time import time



def isPentagonal(x):
    #determines if a number is pentagonal
    if pentToIndex(x) == -1:
        return 0
    return 1

def getFirstPentIndex(basePent, sumLength):
    #this is quite specialized and conusing. Given a pentagonal number p, and another number k, it returns the number 
    #3b+1  such that 3b+1 + 3b+4 + 3b+7 + b+10 + b+13 ... (this sum having k terms) = p. The reason why this is useful has 
    #to do with the fact that the gaps between pentagon numbers increase by 3 each term -- 
    #the discrete double-derivative-type thing of the pentagonal numbers is 3
    ansNumer = basePent-sumLength-3*int(sumLength*(sumLength-1)/2)
    ansDenom = 3*sumLength
    if ansNumer%ansDenom == 0:
        ans = int(ansNumer/ansDenom)
    else:
        ans = -1
    #print(ans)
    if ans >= 4:
        return int(ans)
    else:
        return -1
def pentToIndex(p):
    #takes a number; if it is the kth pentagonal number, then return k. otherwise, return -1 
    #obviously, if -1 is returned, that means the given number was not pentagonal
    retin = -1
    sindx = 1+math.sqrt(24*p+1) #magic pentagon-testing formula
    if sindx == int(sindx):
        if int(sindx)%6 == 0:
            retin = int(int(sindx)/6)
    if retin <= 0:
        retin = -1
    return retin
    
def main():
    #The strategy: we test each pentagonal number as a difference. That is, we check if there are any pentagonal 
    #numbers that have a difference of 1, the first pentagonal number, then we check if there are any pentagonal
    #nubmers that have a difference of 5, the second pentagonal numbers, etc. Once we find one -- the first is 35
    #and 70 -- they have a difference of 35 -- we check if the pair's sum is pentagoanl, which, for 35 and 70, 105
    #is not. But, once we find one, that pair is guarenteed to have the minimal difference.
    #By the way, if a pentagonal number p is a difference between two other pentagonal numbers a and b, finding
    #all possible pairs of a and b's is a bit convoluted. We find each way p can be written as the sum of 
    #consecutive-as-possible positive numbers that are 1 mod 3 (e.g., 7,10,13,16...) and we can determine all posible
    #a's and b's based on this. The numbers get pretty large, so the number of possibilities for the 1-mod-3 sum, if
    #brute-forced, get unweildily large. One large optimization is bounding the number of terms in the 1-mod-3 sum
    #so it won't be too large or negative. Another optimization is only checking 1-mod-3 sums with x-mod-3 terms,
    #where x%3 = p%3. This has gotten a bit rambly and confusing, so I will stop explaining.

    #Executes in about 0.77 seconds
    t0 = time()

    ctr = 1
    found = 0
    basePent = 1
    pi = 0
    pk = 0
    while not(found):
        basePent = int(ctr*(3*ctr-1)/2)
        minran = basePent%3
        if minran == 0:
            minran = 3
            
        maxran = int(math.ceil(math.sqrt(2.0*basePent/3.0+25.0/36.0)-5.0/6.0))+1 #don't ask -- based on a quadratic
        for i in range(minran,maxran,3):
            firstidx = getFirstPentIndex(basePent, i)
            if firstidx >= 1:
                firstPent = int(firstidx*(3*firstidx-1)/2)
                secondPent = basePent + firstPent
                sumPent = secondPent + firstPent
                if isPentagonal(sumPent):
                   
                    found = 1
        ctr +=1

    print("Time Elapsed:", time()-t0)
    print(basePent)
main()