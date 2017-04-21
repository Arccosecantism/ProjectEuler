

def lastTenSuperExponentTwo(doubleExp):
    val = 2
    for i in range(doubleExp):
        val = (val*val)%(10**10)
    return val
def main():
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
    print(fval)

main()