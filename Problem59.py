#Problem: XOR encryption/decryption -- see site: https://projecteuler.net/problem=59
import math
from time import time
import os


def getCode():
    #reads a file and provides a list of ASCII values
    f = open("TextFiles\CipherProblem59.txt", 'r')
    lines = f.read()
    codeChars = lines.split(',')
    codeVals = map(int,codeChars)
    return codeVals

def XOR(a,b):
    #does XOR
    return a^b

def incPassword(password):
    #Increments the password
    av = ord('a')
    zv = ord('z')
    done = 0
    if password[2] == zv:
        password[2] = av
        if password[1] == zv:
            password[1] = av
            if password[0] == zv:
                password[0] = av
                done = 1
            else: password[0] += 1
        else:
            password[1] += 1
    else:
        password[2] += 1
    return [password, done]



def main():
    #The Strategy: We test all passwords and the message they produce. Then we determine if the message is 
    #the actual plaintext by searching for the words "the", "and", "this", and "in"

    #Executes in 4.606 seconds
    t0 = time()
    codeVals = getCode()
    av = ord('a')
    
    password = [av, av, av]
    done = 0
    wordTests = ["the", "and", "this", "in"]
    goodWord = ""
    while not(done):
        decryptAttempt = ""
        pctr = 0
    
        for i in codeVals:
            nc = chr(XOR(i,password[pctr]))
            decryptAttempt += nc

            pctr = (pctr+1)%3

            
        gwt = 1
        for i in wordTests:
            if i not in decryptAttempt:
                gwt = 0
                break
        if gwt:
            print(decryptAttempt)
            goodWord = decryptAttempt
            done = 1

  
        ip = incPassword(password)
        done = done or ip[1]
        password = list(ip[0])
    
    ssum = 0
    for i in goodWord:
        ssum += ord(i)
    
    print("Time Elapsed:", time()-t0)
    print(ssum)
        
        
        

main()