#Problem: 40755 is the 285th triangle number, the 165th pentagonal number, and the 143rd hexagonal number
#           What is the next number that is triangular, pentagonal, and hexagonal? 

import math
from time import time

def isPentagonal(x):
    #checks if a number is pentagonal
    if math.sqrt(24*x+1)%6 == 5:
        return 1
    return 0

def main():
    #the strategy: first thing to notice: all hexagonal numbers are triangular -- I didn't know this in my first
    #solution, but it is quite obvious once you look for it (aren't most things?).  So we simply generate larger and
    #larger hexagonal number until we hit a number larger than 40755 that is pentagonal. I also saw a cooler, more
    #efficient solution where you try to "balance" a pentagonal and hexagonal number: if the 
    #pentagonal nubmer is smaller, take the next pentagonal, if the hexagonal number is smaller, take the next
    #hexagonal, until they are equal. 

    #My way executes in about .039 seconds  
    t0 = time()
    numCtr = 1
    hexCtr = 1
    fd = 1
    sd = 4
    done = 0
    while not(done):

        if hexCtr > 40755 and isPentagonal(hexCtr):
            done = 1
        else:
            numCtr+=1
            fd += sd
            hexCtr += fd
    print("Elapsed Time:", time()-t0)
    print(hexCtr)

main()