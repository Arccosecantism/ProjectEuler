#Problem: If you mash the numbers from 1-n together, the limit as n goes to infinity is 1234567891011121314151616718192021...9899100101102103...998999100010011002...
#         Let this number = k and d(n) = the nth digit of k, from the right. So d(1) = 1, d(2) = 2, d(10) = 1, d(11) = 0, d(12) = 1
#         what is d(1)*d(10)*d(100)*d(1000)*d(10000)*d(100000)*d(1000000)?
#         (by the way, if the value of k were a decimal, 0.12345678910111213.., it is called Champernowne's constant -- this is how Project Euler phrases the problem)

from time import time
import math


def numberOfDigits(x):
    #gives the number of digits of a number: n(10456) = 5
    return len(str(x))

def getDigitChamp(num):
    #finds the num'th digit of 123456789101112131415...
    #we find this by first finding if num is in the units, in the tens, in the hundreds, in the thousands, ... , or in the millions.
    #Then, we start at the first possible number (if the num was in the interval [10000, 99999], we start at 10000) and count up (num - the first digit place of the starting digit) times
    #skipping by the largest digit, then by the second largest, then by the third largest, etc. keeping track of the number im on along the way:
    #example: if num happened to be somewhere in 43546, we start with 10000. then we count: 20000, 30000, 40000, 41000, 42000, 43000, 43100, 43200, 43300, 43400, 43500, 43510, 43520, 43530, 
    #43540, 43541, 43542, 43543, 43544, 43545, 43546. It's a bit confusing, but it made sense when I wrote it, and it's not too inefficient.
    #Executes in 

    digitNumberJumps = []
    for i in range(0,6):
        info = []
        ti = i+1
        info.append(9*(10**(ti-1)))
        info.append(ti*info[-1])
        if i == 0:
            info.append(9)
        else:
            info.append(digitNumberJumps[i-1][2]+info[-1])
        digitNumberJumps.append(info)

    placeJumps = []
    for i in range(0,6):
        info = []
        ti = i+1
        for k in range(0,ti):
            info.append(ti*(10**(ti-k-1)))
        
        placeJumps.append(info)

    dignum = 0
    for i in range(0,6):
        if num <= digitNumberJumps[i][2] and dignum == 0:
            dignum = i+1
            break
    
    incnum = 10**(dignum-1)
    countnum = digitNumberJumps[dignum-1][2]-digitNumberJumps[dignum-1][1]

    for i in placeJumps[dignum-1]:
        adder = 10**(numberOfDigits(i)-1)
        while countnum + i < num:
            incnum += adder
            countnum += i
    dif = num-countnum
    val = int(str(incnum)[dif-1])
    return val

def main():
    #the strategy: incredibly obvious, now that we've defined d(n), simply find d(1)*d(10)*d(100)*d(1000)*d(10000)*d(100000)*d(1000000)
    t0 = time()

    prod = 1
    for i in range(0,7):
       prod *= getDigitChamp(10**i)

    print("Time Elapsed:", time()-t0)
    print(prod)
main()