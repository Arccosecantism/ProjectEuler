from time import time
import math

def intPow(x,y):
    p = 1
    for i in range(0,y):
        p *= x
    return p

def numberOfDigits(x):
    return len(str(x))

def getDigitChamp(num):
    digitNumberJumps = []
    for i in range(0,6):
        info = []
        ti = i+1
        info.append(9*intPow(10,ti-1))
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
            info.append(ti*intPow(10,ti-k-1))
        
        placeJumps.append(info)
    


    dignum = 0
    for i in range(0,6):
        if num <= digitNumberJumps[i][2] and dignum == 0:
            dignum = i+1
            break
    
    incnum = intPow(10,dignum-1)
    countnum = digitNumberJumps[dignum-1][2]-digitNumberJumps[dignum-1][1]

    for i in placeJumps[dignum-1]:
        adder = intPow(10,numberOfDigits(i)-1)
        while countnum + i < num:
            incnum += adder
            countnum += i
    dif = num-countnum
    val = int(str(incnum)[dif-1])
    return val

def main():
    t0 = time()

    prod = 1
    for i in range(0,7):
       prod *= getDigitChamp(intPow(10,i))

    print("Time Elapsed:", time()-t0)
    print(prod)
main()