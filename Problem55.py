#Problem: Let the function f(x) take an integer x and return x plus the reverse of x in its decimal representation.
#           So, f(120) = 120 + 021 = 141. If this function is called recursively, many numbers will end up being
#           palindromic. But, for some numbers like 196, it is thought that they will never become palindromic,
#           although it's never been proved one way or the other. If a number never becomes a palindrome, it is called
#           a Lychrel number. For this problem, call a number Lychrel-ish if after 50 iterations, the number has 
#           not been a palindrome. How many Lychrel-ish numbers are there under 10000 (ten thousand)?

import math
from time import time

def isPalindromic(x):
    #Tests if a number is palindromic
    sx = str(x)
    rsx = ''
    for i in range(1,len(sx)+1):
        rsx += sx[-i]
    if sx == rsx:
        return 1
    else:
        return 0


def isLychrelish(counter, cap, num):
    #Tests if a number is Lychrel-ish by doing up to 50 iterations of reversing and adding
    if counter >= 1:
        
        if isPalindromic(num):
            #print(num)
            return 0 
        elif counter==cap:
            return 1

    rsx = ''
    tnum = num
    while tnum:
        rsx += str(tnum%10)
        tnum = (tnum / 10)
    rnum = int(rsx)
    #print(rnum)
    numsum = rnum + num
    return isLychrelish(counter+1, cap, numsum)

def main():
    #The Strategy: Brute-force; I don't know any significant optimizations I could make -- any test I could do
    #seems to be worse than just doing the next iteration. -- I don't know any long-range tests.

    #Despite sheer brute-force, executes in 0.589 seconds.
    t0 = time()
    count = 0
    maxnum = 10000
    for i in range(1,maxnum+1):
        if isLychrelish(0,50,i):
            count += 1
    print("Time Elapsed:", time()-t0)
    print(count)

main()