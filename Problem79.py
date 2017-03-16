

from time import time


def getLoginAttempts():
    #reads a file and provides a list of ASCII values
    f = open("TextFiles\KeyLogsProblem79.txt", 'r')
    lines = [line[:3] for line in f]
    print lines
    return lines

def removeDuplicates(dlist):
    clist = [dlist[0]]
    for i in range(1,len(dlist)):
        good = True
        for j in range(0,i):
            if dlist[j] == dlist[i]:
                good = False
                break
        if good:
            clist.append(dlist[i])
    return clist

def generateSmallestStrings(bstr, sstr, psl):
    if bstr == "":
        return [sstr]
    tcounter = 0
    for i in bstr:
        if tcounter < 3:
            if sstr[tcounter] == i:
                tcounter += 1
        else:
            break
    if tcounter == 3:
        return [bstr]

    psc = psl[len(bstr)]
    nsl = []
    for i in psc:
        tstr = ""
        tc = 0

        for j in range(0,len(bstr)+3):
            
            if tc < 3:
                #print(j,tc,i[tc])
                if j-tc == i[tc]:
                    tstr+= sstr[tc]
                    tc += 1
                else:
                    tstr += bstr[j-tc]
            else: 
                tstr += bstr[j-tc]
                
        nsl.append(tstr)
    for i in range(0,len(nsl)):
        cstr = nsl[i]
        apsc = list(psc[i])
        apsc[1] += 1
        apsc[2] += 2
        toRemove = []
        pspot = -1
        for j in apsc:
            indcheck = [j-1, j+1]
            remove = False
            for k in indcheck:
                if k > 0 and k < len(cstr) and k != pspot and remove == False:
                    bad = False
                    for l in apsc:
                        if l == k:
                            bad = True
                    if not(bad) and cstr[k] == cstr[j]:

                        remove = True
                        pspot = k
                        break
            if remove:
                toRemove.append(j)
        tctr = 0
        for j in toRemove:
            cstr = cstr[:j-tctr] + cstr[j-tctr+1:]
            tctr += 1
        nsl[i] = cstr

    minLen = 35
    for i in nsl:
        tli = len(i)
        if tli < minLen:
            minLen = tli
    smallStrList = []
    for i in nsl:
        if len(i) == minLen:
            smallStrList.append(i)
    return removeDuplicates(smallStrList)
    

def getSmallestPassword(guessList, psl):
    possibleLists = [guessList[0]]
    for i in guessList:
        npl = []
        for j in possibleLists:
            tl = generateSmallestStrings(j, i, psl)
            for k in tl:
                npl.append(k)
        print(npl)
        minLen = 35
        for i in npl:
            tli = len(i)
            if tli < minLen:
                minLen = tli
        mpl = []
        for i in npl:
            if len(i) == minLen:
                mpl.append(i)
        possibleLists = mpl
    return possibleLists
                

def main():
    t0 = time()
    possibleSpots = []
    for i in range(0,31):
        tps = []
        for a in range(0,i+1):
            for b in range(a,i+1):
                for c in range(b,i+1):
                    tps.append([a,b,c])
        possibleSpots.append(tps)
    logins = getLoginAttempts()
    newStrs = getSmallestPassword(logins,possibleSpots)
    print("Time Elapsed:", time()-t0)
    print(newStrs)

main()