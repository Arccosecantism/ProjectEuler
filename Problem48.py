#Problem: What are the last ten digits (smallest digits) of x 
#           where x is 1^1 + 2^2 + 3^3 + 4^4 + ... + 999^999 + 1000^1000


import math
from time import time

def addDigits(d1, d2):
    #adds two arrays of 10 integers that represent the last ten digits of a number, reversed
    l = 10
    carry = 0
    d3 = []
    for i in range(0,l):
        sp = (d1[i]+d2[i]+carry)%10
        bp = int((d1[i]+d2[i]+carry-sp)/10)
        d3.append(sp)
        carry = bp
    return d3

def scalarMultiplyDigits(dig, num):
    #multiplies an array of 10 integers by a scalar as if the array were a ten-digit number in reverse
    l = 10
    carry = 0
    ndig = []
    for i in range(0,l):
        sp = (dig[i]*num+carry)%10
        bp = int((dig[i]*num+carry-sp)/10)
        ndig.append(sp)
        carry = bp
    return ndig


def intTo10Digits(x):
    #gets the last 10 digits of a number
    ndig = []
    for i in range(0,10):
        ndig.append(x%10)
        x = int(x/10)
    return ndig

def getReverseList(flist):
	#gets the reverse of a list: g([5,3,4]) = [4,3,5] 
	revlist = []
	for i in range(0,len(flist)):
		revlist.append(flist[len(flist)-1-i])
	return revlist

def main():
    #The strategy: the only thing holdin us back is that the numbers get really large. We just need to
    #keep track of the last 10 digits, so we use arrays to store the digits, and make an add and multiply
    #function so we can manipulate the arrays. We simply just add the last-10-digit arrays for n^n up from
    #n in [1,1000] in Integers.

    #Executes in 3.526 seconds
    t0 = time()
    powers = []
    for i in range(1,1001):
        start = [1,0,0,0,0,0,0,0,0,0]
        ub = int(i/2)
        for k in range(0, ub):
            start = list(scalarMultiplyDigits(start,i*i))
        if i%2 == 1:
            start = list(scalarMultiplyDigits(start,i))
        powers.append(start)
    #print(powers)

    ssum = [0,0,0,0,0,0,0,0,0,0]
    for i in powers:
        ssum = list(addDigits(ssum, i))
    
    print(ssum)
    ssum = list(getReverseList(ssum))
    print("Time Elapsed:", time()-t0)
    print(ssum)
main()


    
