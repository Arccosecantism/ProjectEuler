
#Problem: 	When you create a spiral of numbers: like 
#                    21 22 23 24 25
#                    20 7  8  9  10
#                    19 6  1  2  11
#                    18 5  4  3  12
#                    17 16 15 14 13
#           what is the sum of the numbers on the diagonals when the size of the spiral is 1001 by 1001?
#           (for 5, as shown, the sum of the diagonals is 1 + 3 + 5 + 7 + 9 + 13 + 17 + 21 + 25 = 101)

import math
from time import time

def main():
    #This is quite easy -- the diagonals are sums of odd squares minus a multiple of 2, which is (2n-1)(2n)(2n+1)/6
    #We jsut count up the square sums and subtract off the multiples of 2, and subtract 3 because having one 1 in the center 
    #is weird and throws things off 
    tic = time()
    n = 1001
    rn = (n+1)/2
    oddsq = (2*rn-1)*(2*rn)*(2*rn+1)/6
    evenoff = 6*rn*(rn-1)
    ans = 4*oddsq-evenoff-3

    print("Time Elapsed: ", time() - tic)
    print(oddsq, evenoff, ans)

main()