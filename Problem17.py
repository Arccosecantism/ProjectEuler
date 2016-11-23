#Problem: 	How many letters total are there in the numbers: "one", "two", ... "one hundred and fifty-seven", ... "nine hundred and niety-nine", "one thousand"?
#			(ignore spaces and hyphens)
import math


#needless test -- thought I had wrong answer, but I just typed it in wrong
'''def countActualLetters(str):
	sum = 0
	for i in str:
		if ord(i) >= ord('a') and ord(i) <= ord('z'):
			sum += 1
	return sum'''

def findLettersInNumber(x):
	#finds the number of letters in a number
	digitLengthsUnit = [0,3,3,5,4,4,3,5,5,4]
	digitLengthsTens = [0,3,6,6,5,5,5,7,6,6]
	digitLengthsTeens = [3,6,6,8,8,7,7,9,8,8]
	hundredLength = 7
	andLength = 3
	
	if x == 1000:
		return 11
	lastTwo = x%100
	sum = 0
	if lastTwo == 0:
		sum += 0
	elif lastTwo < 10:
		sum += digitLengthsUnit[lastTwo%10]
	elif lastTwo < 20 and lastTwo >= 10:
		sum += digitLengthsTeens[lastTwo%10]
	else:
		sum += digitLengthsTens[int(lastTwo/10)] + digitLengthsUnit[lastTwo%10]
		
	if x >= 100:
		sum += hundredLength + digitLengthsUnit[int(x/100)]
		if lastTwo > 0:
			sum += andLength 
	return sum

	
#needless test -- thought I had wrong answer, but I just typed it in wrong
'''def constructNumName(x):
	digitNamesUnit = ["","one","two","three","four","five","six","seven","eight","nine"]
	digitNamesTens = ["","ten","twenty","thirty","forty","fifty","sixty","seventy","eighty","ninety"]
	digitNamesTeens = ["ten","eleven","twelve","thirteen","fourteen","fifteen","sixteen","seventeen","eighteen","nineteen"]
	hundredName = "hundred"
	andStr = "and"
	
	resultStr = ""
	
	if x == 1000:
		return "one thousand"
	firstDigit = int(x/100)
	lastTwo = x%100
	if firstDigit > 0:
		resultStr += digitNamesUnit[firstDigit] + " " + hundredName + " "
		
	if lastTwo > 0 and firstDigit > 0:
		resultStr += andStr + " "
	if lastTwo >= 20:
		resultStr += digitNamesTens[int(lastTwo/10)] + "-" + digitNamesUnit[lastTwo%10]
	elif lastTwo < 20 and lastTwo >= 10:
		resultStr += digitNamesTeens[lastTwo%10]
	else:
		resultStr += digitNamesUnit[lastTwo%10]
		
	return resultStr
	
def test(x):
	print(x, constructNumName(x), countActualLetters(constructNumName(x)), findLettersInNumber(x))
	if findLettersInNumber(x) !=  countActualLetters(constructNumName(x)):
		print("FOUND IT!!!", x)
'''

def main():
	#this problem is simple - but it took me a while because I thought I had the wrong answer
	#this solution is brute force -- just count up, finding the amount of letters and adding them  
	#to a running sum
	
	sum = 0
	for i in range(1,1001):
		sum += findLettersInNumber(i)
		print(i, findLettersInNumber(i))
		#test(i)
	print(sum)

			
			



main()


