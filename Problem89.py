import math

from time import time

def readRomanNumerals():
    #gets the list of roman numerals from "RomanNumeralsProblem89.txt"
    f = open("TextFiles\\RomanNumeralsProblem89.txt", 'r')
    lines = f.readlines()
    flines = []
    for i in lines:
        if i[-1] == "\n":
            flines.append(i[:-1])
        else:
            flines.append(i)
    #for i in nlines:
    #	print(i)
    return flines

def numeralToValue(nl):
    #gets a numeral and returns its value
    li = ["M","D","C","L","X","V","I","CM","CD","XC","XL","IX","IV"]
    vi = [1000, 500, 100, 50, 10, 5, 1, 900, 400, 90, 40, 9, 4]
    for i in range(0,13):
        if nl == li[i]:
            return vi[i]
    return 0

def compareNumeralLetters(la, lb):
    #compares two numerals in size
    va = numeralToValue(la)
    vb = numeralToValue(lb)
    
    if va == vb:
        return 2
    if va > vb:
        return 1
    if va < vb:
        return 0
    
def romanNumeralToNumber(numerstr):
    #converts a roman numeral to a number
    ssum = 0
    skip = False
    for i in range(0,len(numerstr)-1):
        if not(skip):
            if not(compareNumeralLetters(numerstr[i],numerstr[i+1])):
                conc = str(numerstr[i])+str(numerstr[i+1])
                ssum += numeralToValue(conc)
                
                skip = True
            else:
                ssum += numeralToValue(numerstr[i])
        elif i != len(numerstr) - 1:
            skip = False
    
    if skip == False:
        ssum += numeralToValue(numerstr[-1])

    return ssum

def numberToRomanNumeralCount(x):
    #returns the minimal amount of numerals required to represent a number
    sx = str(x)
    count = 0
    
    for i in sx:
        ti = int(i)
        if ti == 9 or ti == 4:
            count += 2
        elif ti >= 5:
            count += ti-4
        else:
            count += ti
    if x >= 4000:
        count += 2
    return count

def compareMinimalRomanNumeral(rnstr):
    #returns the number of numerals saved if a roman numeral is represented in its smallest form
    return (len(rnstr) - numberToRomanNumeralCount(romanNumeralToNumber(rnstr)))

def main():
    t0 = time()
    #the strategy: once we have the function for transforming a rmoan numeral to a number and the function for rewriting
    # a number as a minimally-sized roman numeral, the rest is easy; we simply go through the list and see how many chars could be saved on each row.
    #executes in 0.125 seconds
    romanNumeralList = readRomanNumerals()
    #print(romanNumeralList)
    savesum = 0
    for i in romanNumeralList:
        savesum += compareMinimalRomanNumeral(i)
    print("Time Elapsed:  " + str(time()-t0))
    print(savesum)

main()