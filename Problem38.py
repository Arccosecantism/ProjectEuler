#Problem: Take the number 192 and multiply it by each of 1, 2, and 3:

#            192 × 1 = 192
#            192 × 2 = 384
#            192 × 3 = 576
#           By concatenating each product we get the 1 to 9 pandigital, 192384576. We will call 192384576 the concatenated product of 192 and (1,2,3)
#           The same can be achieved by starting with 9 and multiplying by 1, 2, 3, 4, and 5, giving the pandigital, 918273645, which is the concatenated product of 9 and (1,2,3,4,5).
#           What is the largest 1 to 9 pandigital 9-digit number that can be formed as the concatenated product of an integer with (1,2, ... , n) where n > 1?


from time import time
import math


def isPandigital1to9(x):
    #checks if a number is pandigital
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
    #The strategy: we know the number has to be 4 digits long. If we create a table:

    #       Number of Digits | Possible ways to get to 9 digits when multiplying and concatenating  | Bounds on the number
    #       -----------------|----------------------------------------------------------------------|---------------------
    #               1        |      {1,2,2,2,2}, {1,1,1,1,1,1,1,1,1}                                | {n>=5}, {n=1} 
    #               2        |      {2,2,2,3}                                                       | {n <= 33}
    #               3        |      {3,3,3}                                                         | {n <= 333}
    #               4        |      {4,5}                                                           | {n>=5001}
    #               5        |      {}
    #               6...
    #
    #     We see that to make the concatenated number greater than 918273645, our base case, we need the first digit of n to be > 9
    #     the only case where this works is 1 digit and n = 9, which actually is our base case, and 4 digits where n > 9182
    #     We simply check all of the possible numbers (there are only 1000) and we check if the concatenateion of the number and 2 x the number is pandigital
    #     and we keep track of the biggest larger than 918273645. Executes in 0.01 seconds 

    t0 = time()
    maxval = 918273645
    for i in range(9183,10000):

        conc = int(str(i)+str(2*i))
        if isPandigital1to9(conc):
            if conc > maxval:
                maxval = conc
                print(i)
    
    print("Time Elapsed:", time()-t0)
    print(maxval)
    
main()