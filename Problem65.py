#Problem: just see it -- it's too hard to give context: https://projecteuler.net/problem=65
#           What is the sum of the numerator of the 100th continued fraction convergent of e?

import math
from time import time

def sumDigits(x):
    #Sums the digits of a large number
    sx = str(x)
    ssum = 0
    for i in sx:
        ssum += int(i)
    return ssum

def main():
    #The strategy: One odd thing to notice about continued fractions (yes I had to look this up for the next problem) is that
    #the numerator of a convergent follows a pattern: if the numerator of the kth convergent is p(k) and a(m) is the mth coefficient of 
    #the continued fraction, p(0) = a(0), p(1) = a(0)*a(1)+1, and p(n) = a(n)*p(n-1)+p(n-2). Using this recursive identity, we simply generate
    #the first 100 coefficients for the continued fraction of e and iteratively go up and find p(100). Then, we sum the digitsm, and that's the answer
    #executes in "0.0 seconds" (thanks garbage time library)
    t0 = time()
    e_list = []
    maxVal = 100
    for i in range(2,1+maxVal):
        if i%3:
            e_list.append(1)
        else:
            e_list.append(int(2*i/3))
    
    num = 3
    pnum = 2
    for i in range(1,len(e_list)):
        nnum = e_list[i]*num+pnum
        pnum = num
        num = nnum

    numeratorSum = int(sumDigits(num))
    print("Time Elapsed:", time()-t0)
    print(numeratorSum)

main()