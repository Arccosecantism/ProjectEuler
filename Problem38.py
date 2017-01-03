from time import time
import math


def isPandigital1to9(x):
    ar = [0,0,0,0,0,0,0,0,0,0]
    digs = list(str(x))
    for i in digs:
        ar[int(i)] += 1

    pandigital = 1
    ls = ar[1:]
    for i in ls:
        if i != 1:
            pandigital = 0
            break
    return pandigital

def main():
    t0 = time()
    minval = 918273645
    for i in range(9200,9999):

        conc = int(str(i)+str(2*i))
        if isPandigital1to9(conc):
            if conc > minval:
                minval = conc
                print(i)
    
    print("Time Elapsed:", time()-t0)
    print(minval)
    
main()