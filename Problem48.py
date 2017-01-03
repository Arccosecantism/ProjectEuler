import math
from time import time

def addDigits(d1, d2):
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
    ndig = []
    for i in range(0,10):
        ndig.append(x%10)
        x = int(x/10)
    return ndig

def getReverseList(flist):
	#gives the reverse of a list: g([5,3,4]) = [4,3,5] 
	revlist = []
	for i in range(0,len(flist)):
		revlist.append(flist[len(flist)-1-i])
	return revlist

def main():
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


    
