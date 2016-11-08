#Problem: find sum of all multiples of 3 or five under 1000 (sum of 0,3,5,6,9,10,12,15,18,.....,995,996,999)

def main():
	sum = 0;
	for i in range(0,1000):
		#go through all natural numbers from 0-999
		if not(i%3) or not(i%5):
			#if it's divisible by 3 or 5, add to the sum
			sum += i
	print(sum)


main()