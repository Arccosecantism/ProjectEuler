#how many n-digits numbers are nth powers of integers? (e.g. 125 is a 3rd power and is 3 digits long)

import math
from time import time

def main():
    #The Strategy: We use some maht to solve this. So what does n-digt mean, mathematically? It means this: if a number q is k-digts long,
    #that means k-1 <= log10(q) < k. So in this case, we have 
    #    n-1 <= log10(x^n) < n
    #    n-1 <= n*log10(x) < n
    #    1-1/n <= log10(x) < 1
    #    1/n >= 1-log10(x) > 0
    #    1/(1-log10(x)) >= n > 0
    #This means that for any positive integer x, all positive ntegers n less than or equal to 1/(1-log10(x)) will satisfy x^n is n digits long.
    #Clearly the maxinum number for x is 10: at this point, 1/(1-log10(x)) is undefined, and if x is any greater, 1/(1-log10(x)) will be negative
    #So I simply add up the 1/(1-log10(x)) from x = 1 to 9.
    #Executes in 
    t0 = time()
    ans = 0
    for i in range(1,10):
        ans += int(1/(1-math.log10(i)))
    print("Time Elapsed:", time()-t0)    
    print(ans)

main()