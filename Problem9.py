#Problem: 	what is the 10001st prime number?

import math

def isPythagTriplet(a,b,c):
	return ((a*a+b*b) == (c*c))
	
def main():

	#checks all possible sums up to 1000 of three natural numbers, checks them all if they are 
	#pythagorean triplets -- I think thereis a more mathematical way, though
	
	
	
	#print(isPythagTriplet(3,4,5), isPythagTriplet(4,4,7))
	
	cap = 1000
	product = 0;
	az = 0
	bz = 0
	cz = 0
	for i in range(1,333):
		print(int(math.ceil(float(1000-i)/2))-1)
		for k in range(i+1,int(math.ceil(float(1000-i)/2))):
			if isPythagTriplet(i,k,1000-i-k):
				az = i
				bz = k
				cz = 1000-i-k
				product = i*k*(1000-i-k)
				break
		if product:
			break
	print(product, az, bz, cz)


main()