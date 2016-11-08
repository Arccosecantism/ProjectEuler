#Problem: find sum of all even fibonacci numbers under 4,000,000 (sum of 0,2,8,34, etc 


#The key thing to realize is that even fibonacci numbers occur every three terms: (0),1,1,(2),3,5,(8),13,21,(34),
#this makes sense: even, odd, (even+odd)=odd, (odd+odd)=even, (odd+even)=odd, (even+odd)=odd, (odd+odd)=even, etc

def genFib(x):
	#generates a list of all fibonacci numbers under x, defined as f(0)=0, f(1)=1, f(x)=f(x-1)+f(x-2)
	fiblist=[]
	fiblist.append(0)
	fiblist.append(1)
	end = 1
	while (fiblist[end]+fiblist[end-1]) < x:
		fiblist.append(fiblist[end]+fiblist[end-1])
		end += 1
	return fiblist
	

def main():
	
	sum = 0
	ctr = 0
	fiblist = genFib(4000000)
	#gen the fibonacci list
	#print(fiblist[6])
	while ctr < len(fiblist):
		#go through every third term
		sum += fiblist[ctr]
		ctr += 3	#hit every third (even) term
		
		
	print(sum)
		


main()