
#The problem: what are the last ten digits of 28433×2^7830457+1?
from time import time
def lastTenSuperExponentTwo(doubleExp):
    #raises a number to the 2^doubleExp power mod 10^10
    val = 2
    for i in range(doubleExp):
        val = (val*val)%(10**10)
    return val
def main():
    #Strategy: we try to speed up the exponentiation process and segment it at the smae time by squaring.
    #we figure out how many times to square and multiply by using a binary representation of the exponent

    #Executes in "0.0" seconds
    t0 = time()
    coef = 28433
    exp = 7830457
    const = 1

    te = exp
    prod = 1
    ctr = 0
    while te:
        if te&1:
            prod = (prod*lastTenSuperExponentTwo(ctr)) % (10**10)
        te >>= 1
        ctr += 1

        
    fval = (coef*prod+const) % (10**10)
    print("Time Elapsed:  " + str(time()-t0))
    print(fval)

main()