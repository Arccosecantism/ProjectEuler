#Problem: If the denominations of money (below 2 pounds) in England are 200p, 100p, 50p, 20p, 10p, 5p, 2p, and 1p (p is for pence), 
#           how many unique combinations of any amount of coins are there that add up to exactly 200p (2 pounds)?

import math
from time import time


def countCoinCombos(amt,coinvals,progress):
    #Recursively adds up the number of ways to make <amt> pence with the denominations in coinvals,
    #provided that the smallest denomination evenly divides amt. Essentially, what happens
    #is I pick 0 or 1 200p coins, and then for each case,[0 (for 1 200p case) ]or[ 0 or 1 or 2 100p coins], etc.
    #at the end (base case), 1 is the return value, as there is only one option left; filling the remaining amount
    #with 1 pence pieces.
    ret = 0
    lc = len(coinvals) - 1
    maxCoinNum = int(amt/coinvals[progress])
    if progress < lc:
        for i in range(0,maxCoinNum+1):
            ret += countCoinCombos(amt-i*coinvals[progress],coinvals,progress+1)
    elif progress == lc:
        ret = 1
    return ret

def main():
    #simple recursive function easily solves this as described above: execution time is -0.102 (wtf?)
    t0 = time()
    coinValues = [200,100,50,20,10,5,2,1]
    
    num = countCoinCombos(200, coinValues, 0)
    print("Time Elapsed:", t0-time())
    print(num)
main()