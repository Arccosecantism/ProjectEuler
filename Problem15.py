#Problem: 	How many paths are there (travelling only down and right) through a 20x20 grid?

import math


def fac(x):
	#factorial
	if x == 0:
		return 1
	else:
		return x*fac(x-1)
		
	
def nCr(n, r):
	#combinations: n choose r
	return int(fac(n)/(fac(n-r)*fac(r)))


def main():
	#this problem is equivalent to the number of ways you can arrange 20 1's and 20 0's in a binary array: that is 40 choose 20
	num = 20
	paths = nCr(2*num,num)
	print(paths)



main()


