import math
from time import time

def main():

    t0 = time()
    ans = 0
    for i in range(1,10):
        ans += int(1/(1-math.log10(i)))
    print("Time Elapsed:", time()-t0)    
    print(ans)

main()