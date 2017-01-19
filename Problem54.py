#Problem: In the file of pairs of poker hand given, how many hands does player 1 win?

import math
from time import time
import os

def getHands():
    #reads the files and provides the list of strings
    f = open("TextFiles\PokerHandsProblem54.txt", 'r')
    lines = f.readlines()
    for i in range(0, len(lines)):
        lines[i] = lines[i][:-1]
    dHands = [i.split(" ") for i in lines]
    hands = []
    for i in dHands:
        hands.append([i[:5],i[5:]])
    return hands


def getCardData(cardStr):
    #Translates a Rank and suit into numerical values: e.g., "AS" -> [14, 3] becase an ace is 14 and spades are the 
    #largest of the fours suits
    rank = -1
    cr = cardStr[0]
    if cr == 'T':
        rank = 10
    elif cr == 'J':
        rank = 11
    elif cr == 'Q':
        rank = 12
    elif cr == 'K':
        rank = 13
    elif cr == 'A':
        rank = 14
    else:
        rank = ord(cr)-ord('0')
    
    suit = -1
    cs = cardStr[1]
    if cs == "C":
        suit = 0
    elif cs == "D":
        suit = 1
    elif cs == "H":
        suit = 2
    elif cs == "S":
        suit = 3
    
    return [rank,suit]


def interpretHand(hand):
    #translates all cards in a five-card hand
    handData = []
    for i in hand:
        handData.append(getCardData(i))
    return handData

def interpretHandList(handlist):
    #translates all hands in a list of hand-pairs
    handData = []
    for i in handlist:
        handData.append([])
        for j in i:
            handData[-1].append(interpretHand(j))
    return handData

def rankHand(hand):
    #ranks a hand -- really annoying to make this; there is so much tedious testing and cases and logic

    winA = 0
    winB = 0
    
    straightTest = 1
    rankParts = []
    for i in hand:
        rankParts.append(i[0])
    rankParts.sort()
    for i in range(1,5):
        if rankParts[i] - rankParts[i-1] != 1:
            straightTest = 0
            break

    flushTest = 1
    flushSuit = hand[0][1]
    for i in hand[1:]:
        if i[1] != flushSuit:
            flushTest = 0
            break   
    if flushTest:
        if straightTest:
            if rankParts[4] == 14:
                winA = 10

            else:
                winA = 9

        else:
            winA = 6
            winC = rankParts[-1]
    elif straightTest:
        winA = 5
    
    rankAmounts = [] 
    for i in range(0,15):
        rankAmounts.append(0)
    for i in rankParts:
        rankAmounts[i] += 1
    pairs = 0
    pairsRank = 0
    trips = 0
    tripsRank = 0
    quads = 0
    quadsRank = 0
    for i in range(0, len(rankAmounts)):
        ti = rankAmounts[i]
        if ti == 2:
            pairs += 1
            if i > pairsRank:
                pairsRank = i
        elif ti == 3:
            trips += 1
            tripsRank = i
        elif ti == 4:
            quads += 1
            quadsRank = i
    
    if tripsRank > 0:
        pairsRank = 0

    if pairs >= 1:
        if trips == 1:
            winA = 7
            winB = tripsRank

        elif pairs == 2:
            winA = 3
            winB = pairsRank

        else:
            winA = 2
            winB = pairsRank


    elif trips == 1:
        winA = 4
        winB = tripsRank
 
    elif quads == 1:
        winA = 8
        winB = quadsRank
        for i in range(1,6):
            if rankParts[-i] != quadsRank:
                winC = rankParts[-i]
                break
    
    if winA == 0:
        winA = 1
    tmpC = []
    for i in range(1,6):
        tmpC.append(rankParts[-i])
    winC = []
    for i in tmpC:
        if i != pairsRank and i != tripsRank and i != quadsRank:
            winC.append(i)

    return [winA, winB, winC]

def compareHandPair(handa, handb):
    #Compares two hands to see who wins
    hra = rankHand(handa)
    hrb = rankHand(handb)

    bigger = 0
    arrayCheck = 0
    if hra[0] > hrb[0]:
        bigger = 1
    elif hra[0] == hrb[0]:
        if hra[1] > hrb[1]:
            bigger = 1
        elif hra[1] == hrb[1]:
            arrayCheck = 1
    
    if arrayCheck:
        ara = hra[2]
        arb = hrb[2]
        for i in range(0,len(ara)):
            if ara[i] > arb[i]:
                bigger = 1
                break
            elif ara[i] < arb[i]:
                break
        
   
    return bigger
                
def main():
    #The Stratetgy: No way except brute-force. Simply get all the hands, interpret them, and test and compare them.
    #
    #Executes in .063 seconds
    t0 = time()
    handPairList = interpretHandList(getHands())
    ssum = 0
    for i in handPairList:
        ssum += compareHandPair(i[0], i[1])
    
    print ("Time Elapsed:", time()-t0)
    print(ssum)

main()