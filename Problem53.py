import math
from time import time

def main():
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