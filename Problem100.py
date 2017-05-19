#Problem: If a box contains 3 blue disc and 1 yellow disc, the probability of drawing two blue discs without replacement
#           is (3/4)*(2/3) = 1/2. The same is true for a box with 15 blue discs and 6 yellow discs: the probability is (15/21)*(14/20) = 1/2
#           for the first (integer) case where there are over 1 trillion discs in total and the probability of drawing two blue discs without
#           replacement is 1/2, how many blue discs are there? 


from time import time

def main():
    #The strategy: Let B be the number of blue disks and T be the number of total disks. Then\
    #    B/T * (B-1)/(T-1) = 1/2
    # => 2B^2 - 2B = T^2 - T
    # => 2B^2-2B+1/2 = T^2 - T + 1/4 + 1/4
    # => 2(B-1/2)^2 = (T-1/2)^2 + 1/4
    # => 8(B-1/2)^2 = 4(T-1/2)^2 + 1
    # => (2T-1)^2 - 2(2B-1)^2 = -1

    #This is a negative Pell's equation of the form x^2 - 2y^2 = -1
    #"figuring out" (looking up) the way to solve this Pell's equation reveals that 
    #the fundamental solution is x_1=1, y_1=1, and
    #x_n+1 = 3x_n + 4x_n,  y_n+1 = 2x_n + 3y_n
    #Using this recurrence, we can easily generzate all solutions. We take the first one with total number over 1 tril.

    #Executes in "0.0" seconds -- I love these Pell things
    
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