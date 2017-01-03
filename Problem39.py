from time import time
import math



def main():
    t0 = time()
    best = [12,1]
    for p in range(12,1002,2):
        pnum = 0
        mina = 3
        if p%2:
            mina = 2
        maxa = p/3-1
        for a in range(mina,maxa+1):
            minb = max(a,(p/2)-a)+1
            maxb = int(math.ceil((p-a)/2))
            for b in range(minb, maxb+1):
                c = p-a-b
                if (a*a+b*b) == (c*c):
                    print(a,b,c,":",p)
                    pnum += 1
        if pnum > best[1]:
            best = [p,pnum]
    print("Time Elapsed:", time()-t0)
    print(best)
main()