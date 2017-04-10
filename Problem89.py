import math

from time import time

def readRomanNumerals():
    #gets the list of numbers from "TriangleProblem67.txt"
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
    li = ["M","D","C","L","X","V","I","CM","CD","XC","XL","IX","IV"]
    vi = [1000, 500, 100, 50, 10, 5, 1, 900, 400, 90, 40, 9, 4]
    for i in range(0,13):
        if nl == li[i]:
            return vi[i]
    return 0

def compareNumeralLetters(la, lb):
    va = numeralToValue(la)
    vb = numeralToValue(lb)
    
    if va == vb:
        return 2
    if va > vb:
        return 1
    if va < vb:
        return 0
    
def romanNumeralToNumber(numerstr):
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
    return (len(rnstr) - numberToRomanNumeralCount(romanNumeralToNumber(rnstr)))

def main():
    romanNumeralList = readRomanNumerals()
    #print(romanNumeralList)
    savesum = 0
    for i in romanNumeralList:
        savesum += compareMinimalRomanNumeral(i)
    print(savesum)
    #print(compareMinimalRomanNumeral("MMMMDCLXXII"))

main()