#Problem: What is the greatest product of four numbers in a line (up, down, left, right, diagonal) 
# in the table shown in yellow at line 29? 
import math 

def numberOfFactorsCapped(x, cap):

	#finds number of factors of x, given that x has no prime factors greater than or equal to cap
	#this function has this weird cap because compute time gets wayyy too long if you have to check 
	#large-ish numbers (10s of millions) that have a small (10 and under) number of factors -- 
	#these factors are big, and it takes a while to count up to, say, 100,000; putting a cap on greatly
	#reduces compute time
 	pfacArray = []
	pfaCtr = -1
	lastFactor = 1
	exit = 0
	
	while x > 1 and not(exit):
		for i in range(2,cap+1):
			if i == cap:
				exit = 1
				break
			elif x % i == 0:
				if i > lastFactor:
					lastFactor = i
					pfacArray.append(0)
					pfaCtr += 1
				x /= i
				pfacArray[pfaCtr] += 1 
				break
				
	if exit:
		return 0
		
		
	product = 1 
	for i in pfacArray:
		product *= (i+1)
	#print (pfacArray)
	return product 
	
	
def main(): 
	#just check all triangle numbers, find the amount of divisors and 
	
	
	
	done = 0
	ctr = 0
	tnum = 0
	while not(done):
		ctr += 1
		tnum += ctr
		
		#NOTE: 53 was chosen as a cap because it's assumed that a highly divisible triangle number will not have 
		#53 as a prime factor. However, this is not always the case, and the squareroot of tnum is a safer, albeit more
		#time-consuming cap -- both answers are the same, though
		
		
		#if numberOfFactorsCapped(tnum, int(math.ceil(math.sqrt(tnum))+1)) > 500:
		if numberOfFactorsCapped(tnum, 53) > 500:
			done = 1
		#print(ctr, tnum, numberOfFactorsCapped(tnum, 101))
			
	print(tnum)



	
main()