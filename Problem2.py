
def fib(x):
	if x == 0:
		return 0
	if x == 1:
		return 1
	else:
		return fib(x-1)+fib(x-2)

def main():
	num = 0
	sum = 0
	ctr = 0
	while num < 4000000:
		sum += num
		num = fib(ctr)
		ctr += 3
	print(sum)
		


main()