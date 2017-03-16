
import math

def getSquareRootList(num):
    digList = []

    strn = str(num)
    if len(strn)%2:
        digList.append(int(strn[0]))
    else:
        digList.append(int(strn[0:2]))
    start = len(strn)-2*(int((len(strn)+1)/2)-1)
    for i in range(start, len(strn), 2):
        digList.append(int(strn[i:i+2]))
    return digList
def manualSquareRootInt(num):
    #sqlist = manualSquareRootInt(num)
    leftTerm = 0
    bottomTerm = 0
    leftover = num
    digitList = []
    while len(digitList)<=100:
        if digitList == []:
            leftTerm = 0
            bottomTerm = num
        else:
            leftTerm = int("".join(map(str,digitList)))*20
            bottomTerm = leftover*100
        print("leftTerm:", leftTerm)
        print("bottomTerm", bottomTerm)
        nextDigit = int((math.sqrt(4*bottomTerm + leftTerm*leftTerm)-leftTerm)/2)
        print("nextDigit:", nextDigit)
        digitList.append(nextDigit)
        print("digitList:", digitList)
        leftover = bottomTerm - (leftTerm+nextDigit)*nextDigit
        print("leftover:", leftover)
    return digList
def main():
    print(manualSquareRootInt(2))

main()
