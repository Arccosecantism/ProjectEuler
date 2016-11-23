#Problem: 	How many Sundays were on the first of the month from January 1, 1901 to December 31, 2000?

import math


def isLeapYear(year):
	#finds is year is a leap year
	if not(year%400):
		return 1
	if not(year%100):
		return 0
	if not(year%4):
		return 1
	return 0

def findDaysInMonth(mnum, year):
	#finds days in a month in a year
	monthLengths = [31,28,31,30,31,30,31,31,30,31,30,31]
	if isLeapYear(year):
		monthLengths[1] = 29
	if mnum < 0 or mnum > 11:
		return 0
	return monthLengths[mnum]
	

	
def main():
	#really easy: just jump the days month by month, mod by 7 to get the weekday, go until the year is 2001
	weekdayCounter = 2
	monthCounter = 0
	yearCounter = 1901
	
	sundayCount = 0
	while yearCounter < 2001:
		if weekdayCounter == 0:
			sundayCount += 1
		weekdayCounter = (weekdayCounter + findDaysInMonth(monthCounter, yearCounter))%7
		monthCounter += 1
		if monthCounter > 11:
			monthCounter = 0
			yearCounter += 1
		
	print(sundayCount)



main()


