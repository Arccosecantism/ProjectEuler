#Problem: 	What is the first fibbonacci number [f(x) = f(x-1)+f(x-2); f(0) = 0  f(1) = 1] that has 1000 digits?

import math
from time import time


	
def main():
	#Pretty easy, just use the explicit formula (Binet's formula) which is more or less exponential: f(n) = (((1+sqrt5)/2)^n-((1-sqrt5)/2)^n)/(sqrt5)
	#Also, log10(x) = y means x has floor(y) digits. So, 999 <= log10((((1+sqrt5)/2)^n-((1-sqrt5)/2)^n)/(sqrt5)). Since n is likely large, ((1-sqrt5)/2)^n) is 0.
	#also, let phi = (1+sqrt5)/2 
	#then 999 <= log10(phi^n/(sqrt5)) and 999 <= n*log(phi) - log10(sqrt5) and n >= (999+log10(sqrt5))/log(phi) so the smallest n is n = ceil((999+log10(sqrt5))/log(phi))
	dignum = 1000
	rdignum = dignum-1
	phi = (1+math.sqrt(5))/2
	sq5 = math.sqrt(5)
	ans = math.ceil((rdignum + math.log10(sq5))/math.log10(phi))
	print("Time Elapsed: ", time() - tic)
	print(ans)
	
	
main()


