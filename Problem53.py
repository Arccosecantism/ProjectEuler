#Problem: How many value pairs of n and k for 1 <= n <= 100, 0 <= k <= n are there
#           such that (n choose k) (n!/(k!(n-k)!)) is over 1000000 (one million)?
import math
from time import time

def main():
    #The Strategy: We first notice that in Pascal's triangle, if a value x is greater than some y,
    #all values in a triangle pattern below x are also greater than y. So we start with the initial number 
    #of values > 1000000 by finding the first value, 23choose10, and making a trapezoid shape out of this.
    #Then we go through the remainingrows of Pascls triangle, and iff a new value is greater than 1000000
    #outside the trapezoid, we tack on two strips that abut the trapezoid. We do this untill all rows are completed.
    # 
    #Execution time is 0.001 seconds
    t0 = time()
    bn = 23
    bk = 10
    close = bk
    cap = 100
    maxnum = 1000000
    ssum = (cap-bn+(bn+1-2*bk))*(cap-bn+(bn+1-2*bk)+1)/2 - (bn+1-2*bk)*(bn+1-2*bk-1)/2
    print(ssum)
    for n in range(bn+1,cap+1):
        start = 1
        for k in range(1,close):
            start*=(n-k+1)
            start/= (k)
            if start > maxnum:
                ssum += 2*(cap-n+1)*(close-k)
                close = k
    print("Time Elapsed:", time()-t0)
    print(ssum)
main()