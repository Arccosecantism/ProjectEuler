from time import time

def main():
    t0 = time()

    xo = 1
    yo = 1
    discAmount = 0
    done = False
    while not(done):
        xn = 3*xo+4*yo
        yn = 2*xo+3*yo 
        #print(xn,yn)
        discs = 0
        tamt = 0
        
        if xn%2 and yn%2:
            discs = int((yn+1)//2)
            tamt = int((xn+1)//2) 
            print(discs, tamt) 
            if tamt > 10**12:
                discAmount = discs
                done = True
        xo = xn
        yo = yn
    print("Time Elapsed:  " + str(time()-t0))
    print(discAmount)

main()