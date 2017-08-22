#The Problem: What is the sum of the perimeters of all almost equilateral triangels with integral side lengths and integral areas with 
#               perimeter less than or equal to a billion? An almost equilateral triangle is one where the longest and shortest side
#               differ by exactly one
from time import time

def main():
    #The strategy: This is magic. Using some geometry and math, we get to a quadratic expression of an integer n, that, when the expression is square,
    # corresponds with one integral almost-equilateral triangle. BY completeing the square, we rewrite this expression as a Pell's equation with D=3
    #Then, using standard Pell techniques to find all solutions, we generate the perimeter of all integral equilateral triangles under perimieter 1 billion.

    #Executes in "0.0" seconds
    t0 = time()
    xi = 2
    yi = 1
    xo = 2
    yo = 1
    perimSum = 0
    done = False
    while not(done):
        xn = xi*xo+3*yi*yo
        yn = xi*yo+xo*yi
        #print(xn,yn)
        sx = 0
        tperim = 0
        if xn%3 == 2:
            sx = (xn-2)//3
            #print(sx, 3*sx*sx+4*sx+1)
            tperim = 6*sx + 2
        elif xn%3 == 1:
            sx = (xn+2)//3
            #print(sx, 3*sx*sx-4*sx+1)
            tperim = 6*sx - 2
        if tperim > 0 and tperim <= 1000000000:
            perimSum+= tperim
        elif tperim > 1000000000:
            done = True
        xo = xn
        yo = yn
    print("Time Elapsed:  " + str(time()-t0))
    print(perimSum)

main()
    
