#Problem: for all rational numbers f = p/q where p and q are naturals <= 1000000, find f such that f < 3/7, and f is greater than all other possiblee f's
#           In other words, if you listed all of the unique rationals in order, what number is directly to the left of 3/7?
#           btw, we just need the numerator

from time import time
def gcf(x,y):
    #Euclid's method for finding greatest common factor
    a = max(x,y)
    b = x+y-a
    r = 2
    while r:
        r=a%b
        a=b
        b=r
    return a

def reduceFraction(fpair):
    #reduces a fraction
    fac = gcf(fpair[0],fpair[1])
    return [int(fpair[0]/fac), int(fpair[1]/fac)]

def main():
    #The strategy: check all numbers from 1 to 1000000 and find the closest numerator-denominator pair. Keep track of all of them, and find the largest
    #fraction.

    #Executes in 4.5 seconds 
    t0 = time()
    rng = 1000000
    fracs = []
    for i in range(1,rng+1):
        if i%7:
            num = int(3*i/7)
            fracs.append([num,i])
    largest = 0
    largestFrac = 0
    for i in fracs:
        val = i[0]*1.0/i[1]
        if val > largest:
            largest = val
            largestFrac = reduceFraction(i)
    print("Time Elapsed:", time()-t0)
    print(largestFrac)

main()