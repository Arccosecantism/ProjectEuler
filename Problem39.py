
#Problem:   If p is the perimeter of a right angle triangle with integral length sides, {a,b,c}, there are exactly three solutions for p = 120.
#           {20,48,52}, {24,45,51}, {30,40,50}
#           For which value of p ≤ 1000, is the number of solutions maximised?

from time import time
import math



def main():
    #The stratey: we just do a really inefficient n^3 algorithm, but with many optimizations based on triangle sum theorem, the fact that the numbers are integers and that  
    #increase in length the side lengths strictly. We simply try every perimeter and find the amount of pythag triples that add to it. we store the biggest case. 
    #Executes in 0.862 executes

    t0 = time()
    best = [12,1]
    for p in range(12,1002,2):
        pnum = 0
        mina = int(3)
        if p%2:
            mina = 2
        maxa = int(p/3.0-1)
        for a in range(mina,maxa+1):
            minb =int(max(a,(p/2)-a)+1)
            maxb = int(math.ceil((p-a)/2))
            for b in range(minb, maxb+1):
                c = p-a-b
                if (a*a+b*b) == (c*c):
                    #print(a,b,c,":",p)
                    pnum += 1
        if pnum > best[1]:
            best = [p,pnum]
    print("Time Elapsed:", time()-t0)
    print(best)
main()