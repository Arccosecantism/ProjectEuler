
from time import time

def main():
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
    
