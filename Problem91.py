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
    boardSize = 50
    psum = 0 
    for i in range(1,boardSize+1):
        for k in range(1,boardSize+1):
            gf = gcf(i,k)
            psum += int(math.floor(min(gf*k/i,gf*(boardSize-i)/k)))
    ssum = 2*psum + 3*boardSize*boardSize
    print(ssum)

main()