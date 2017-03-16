#The problem: consider an integer n. Let s(n) = 0 if n is square, and = the sum of the first 100 digits of sqrt(n) (including the digits left of the 
#               decimal point). What is the sum from 1 to 100 of s(n)?

import math
from time import time

def isSquare(num):
    #tests if a number is square
    return math.sqrt(num) == int(math.sqrt(num))

def getNextDigit(lt, bt):
    #finds the next top digit in the manual squareroot
    #solves (lt+x)*x<bt for greatest integer x wth lt and bt known
    #can't just do a squareroot expression -- the precicsion errors don't fit this problem well
    goodNum = 0
    for i in range(1,11):
        if (lt+i)*i > bt:
            goodNum = i-1
            break
    return goodNum

def manualSquarerootInt(num):
    #finds the first 100 digits of an irrational squareroot of a natural by manual by-hand long-division
    #squarerooting, an ancient technique taught many years ago in middle school in the 1970's or so -- 
    #only old fogeys like my dad and Mr. Rabchuk remember it. See the method here: http://www.homeschoolmath.net/teaching/square-root-algorithm.php
    leftTerm = 0
    bottomTerm = 0
    leftover = num
    digitList = []
    while len(digitList)<100:
        if digitList == []:
            leftTerm = 0
            bottomTerm = num
        else:
            leftTerm = int("".join(map(str,digitList)))*20
            bottomTerm = leftover*100
        nextDigit = getNextDigit(leftTerm, bottomTerm)
        digitList.append(nextDigit)
        if nextDigit == 0 and leftTerm < bottomTerm:
            print("What?", leftTerm+1, bottomTerm)
        leftover = bottomTerm - (leftTerm+nextDigit)*nextDigit

    return digitList

def main():
    #The Strategy: for integers 1-100, for the non-square ones, find the first 100 digits, sum them togehter, sum up all the sums, that is the answer.

    t0 = time()
    ssum = 0
    for i in range(1,101):
        if not(isSquare(i)):
            msi = manualSquarerootInt(i)
            ssum += sum(msi)
            #print(len(msi), i, sum(msi), msi)
    print("Time Elapsed:", time()-t0)
    print(ssum)

main()
