#problem: how many pairs of vertecies are there on a 50x50 grid such that the triangle formed by connetcing the points to each other and the
#            bottom left hand corner.
from time import time
import math

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


def main():
    #The strategy: we notice that by selecting one point, the rest of the points that could make right triangles with the
    #right angle around the first selected point will all lie on a line, so we can calulate the number that will work
    #using gcf. Also, the square is almost completely symmetric, so we only have to check half the trinagle, in essence 

    #Executes in .014 seconds
    t0 = time()
    boardSize = 50
    psum = 0 
    for i in range(1,boardSize+1):
        for k in range(1,boardSize+1):
            gf = gcf(i,k)
            psum += int(math.floor(min(gf*k/i,gf*(boardSize-i)/k))) #the amount of points that form right triangles with the first point
    ssum = 2*psum + 3*boardSize*boardSize                           #the 3 bs^2 term counte the number of triangles on the edges.
    print("Time Elapsed:  " + str(time()-t0))
    print(ssum)

main()