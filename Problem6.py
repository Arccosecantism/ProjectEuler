#Problem: 	what is the difference of the sum of the squares of the first 100 natural numbers 
#			and the square of the sums of the first 100 natural numbers?
#			or, find s where s = (1+2+3+4+...+99+100)^2 - (1^2+2^2+3^2+...+99^2+100^2)



	
def main():
	#this is actually really easy. The sum from 1^2 to n^2 = n*(n+1)*(2n+1)/6 (can prove this by induction)
	#and the square of the sum from 1 to n is ((n)(n+1)/2)^2
	num = 100
	ssd = num*num*(num+1)*(num+1)/4-num*(num+1)*(2*num+1)/6
	print(ssd)


main()