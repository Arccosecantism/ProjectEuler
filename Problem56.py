#Problem: what integer n of the form a^b where 1<=a<=100; 1<=b<=100; a,b in Integers has the maximum
#           sum of its digits

import math
from time import time


def scalarMultiplyDigits(dig, num):
    #multiplies an array of digits by a scalar and returns an array of digits -- these arrays are backwards
    ld = len(dig)
    carry = 0
    ndig = []
    for i in range(0,ld):
        sp = (dig[i]*num+carry)%10
        bp = int((dig[i]*num+carry-sp)/10)
        ndig.append(sp)
        carry = bp
    while carry:
        ndig.append(carry%10)
        carry = (carry/10)
    return ndig

def main():
    #The Strategy: Brute-force, using arrays of digits to store large numbers. Simply find all of the values
    #and keep track of the largest

    #Executes in 0.738 seconds
    t0 = time()
    cap = 100
    maxsum = 0
    for a in range(2,cap+1):
        if a%10:
            start = [1]
            for b in range(1,cap+1):
                start = scalarMultiplyDigits(start,a)
                tsum = sum(start)
                if tsum > maxsum:
                    maxsum = tsum
    print("Time Elapsed:", time()-t0)
    print(maxsum)


main()
