

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
    
    print(largestFrac)

main()