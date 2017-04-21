import math
from time import time

def getPuzzles():
 
    f = open("TextFiles\\SudokuProblem96.txt", 'r')
    lines = f.read()
    pregridsa = lines.split("Grid ")
    pregridsb = [i[2:len(i)] for i in pregridsa]
    pregridsc = []
    for i in pregridsb:
        if i != "":
            pregridsc.append(i.replace("\n", ""))
        
    puzzles = []
    for i in pregridsc:
        grid = []
        for j in range(0,9):
            grid.append([])
            for k in range(0,9):
                val = {int(i[j*9+k])}
                if val == set([0]):
                    val = set([1,2,3,4,5,6,7,8,9])
                grid[j].append(val)
        puzzles.append(grid)
    return puzzles
    

def getIncompleteConstraintIndeces(square, sudoku):
    return (getIncompleteRowIndeces(square, sudoku)|
            getIncompleteColumnIndeces(square, sudoku)|
            getIncompleteBoxIndeces(square, sudoku))

def getIncompleteRowIndeces(square, sudoku):
    rset = set([])
    for i in range(9):
        if len(sudoku[square[0]][i]) > 1:
            rset.add((square[0],i))
    return rset

def getIncompleteColumnIndeces(square, sudoku):
    rset = set([])
    for i in range(9):
        if len(sudoku[i][square[1]]) > 1:
            rset.add((i,square[1]))
    return rset

def getIncompleteBoxIndeces(square, sudoku):
    rset = set([])
    tr = (3*(square[0]//3),3*(square[1]//3))
    for i in range(tr[0],tr[0]+3):
        for j in range(tr[1],tr[1]+3):
            if len(sudoku[i][j]) > 1:
                rset.add((i,j))
    return rset

def RCBSimplification(sudoku):
    changed = False
    cset = getCompleteIndeces(sudoku)
    while cset != set([]):
        ind = cset.pop()
        checkers = getIncompleteConstraintIndeces((ind[0],ind[1]), sudoku)
        for i in checkers:
            if (sudoku[i[0]][i[1]] & sudoku[ind[0]][ind[1]]) != set([]):
                changed = True
                sudoku[i[0]][i[1]] -= sudoku[ind[0]][ind[1]] 
                if len(sudoku[i[0]][i[1]]) == 1:
                    cset.add((i[0],i[1]))
    return changed

def getCompleteIndeces(sudoku):
    rset = set([])
    for i in range(9):
        for j in range(9):
            if len(sudoku[i][j]) == 1:
                rset.add((i,j))
    return rset

def tupleSimplificationB(tset, sudoku):
    changed = False
    sl = int(len(tset))
    tlist = list(tset)
    for i in range(1,2**sl-1):
        tx = i
        subset = set([])
        ctr = 0
        while tx:
            if tx&1:
                subset.add(tlist[ctr])
            ctr += 1
            tx >>= 1



        union = set([])
        for j in subset:
            union |= sudoku[j[0]][j[1]]

        if len(union) == len(subset):
            comp = tset - subset
            for j in comp:
                if (sudoku[j[0]][j[1]] & union) != set([]):
                    #print("here")
                    changed = True
                    sudoku[j[0]][j[1]] -= union
    return changed

def tupleSimplificationA(sudoku):
    changed = False
    for i in range(9):
        rs = getIncompleteRowIndeces((i,0),sudoku)
        changed = (changed or tupleSimplificationB(rs,sudoku))
    for i in range(9):
        cs = getIncompleteColumnIndeces((0,i),sudoku)
        changed = (changed or tupleSimplificationB(cs,sudoku))
    for i in range(9):
        bs = getIncompleteBoxIndeces((3*(i//3),3*(i%3)),sudoku)
        #if (3*(i//3),3*(i%3)) == (6,3):
        #    print(bs)
        changed = (changed or tupleSimplificationB(bs,sudoku))
    return changed

def printSudoku(sudoku):
    for i in range(9):
        print(sudoku[i])
        print("-")
    print("*****")
    print("*****")

def testSudokuFinish(sudoku):
    for i in range(9):
        for j in range(9):
            if len(sudoku[i][j]) > 1:
                return 0
    if badcheck(sudoku):
        return 1
    else:
        return 2

def setSudoku(sa, sb):
    for i in range(9):
        for j in range(9):
            sa[i][j] = set(sb[i][j])
def copySudoku(sa):
    rs = []
    for i in range(9):
        rs.append([])
        for j in range(9):
            rs[i].append(set(sa[i][j]))
    return rs

def solveSudoku(sudoku, backtracks, resets):
    done = False
    fail = False
    split = False
    changed = False
    while not(done):
        RCBSimplification(sudoku)
        changed = tupleSimplificationA(sudoku)

        doneCheck = testSudokuFinish(sudoku)
        if doneCheck == 1:
            done = True
        elif doneCheck == 2:
            #print("fail?!")
            #printSudoku(sudoku)
            done = True
            fail = True
        elif not(changed):
            #print("split--")
            done = True
            split = True

    if fail:
        setSudoku(sudoku, resets[-1])
        del resets[-1] 
        sudoku[backtracks[-1][0][0]][backtracks[-1][0][1]] = set([backtracks[-1][1]])
        del backtracks[-1]
        solveSudoku(sudoku,backtracks,resets)
    if split:
        ns = copySudoku(sudoku)
        resets.append(ns)
        nbt = ((-1,-1),-1)
        for i in range(9):
            for j in range(9):
                if len(sudoku[i][j]) == 2 and nbt == ((-1,-1),-1):
                    val = sudoku[i][j].pop()
                    nbt = ((i,j),val)
        backtracks.append(nbt)
        solveSudoku(sudoku,backtracks,resets)
        
def badcheck(sudoku):
    for i in range(9):
        ta = [0,0,0,0,0,0,0,0,0]
        for j in range(9):
            val = sudoku[i][j].pop()
            sudoku[i][j].add(val)
            ta[val-1]+=1
        for f in ta:
            if f != 1:
                return False
    
    
    for j in range(9):
        ta = [0,0,0,0,0,0,0,0,0]
        for i in range(9):
            val = sudoku[i][j].pop()
            sudoku[i][j].add(val)
            ta[val-1]+=1
        for f in ta:
            if f != 1:
                return False

    for i in range(9):
        ta = [0,0,0,0,0,0,0,0,0]
        tlin = (3*(i//3), 3*(i%3))
        for j in range(3):
            for k in range(3):
                ti = tlin[0]+j
                tj = tlin[1]+k
                val = sudoku[ti][tj].pop()
                sudoku[ti][tj].add(val)
                ta[val-1]+=1
       
        for f in ta:
            if f != 1:
                return False

    return True
        
def main():
    puzzles = getPuzzles()
    for i in puzzles:
        solveSudoku(i,[],[])
        '''for j in i:
            print(j)
            print("---")
        print("***")
        print("***")
        print("***")'''
    ssum = 0
    for i in puzzles:
        tval = 0
        if not(badcheck(i)):
            for j in i:
                print(j)
                print("-")
            tval = int(str(i[0][0].pop())+str(i[0][1].pop())+str(i[0][2].pop()))
            print(tval)
            print("*****")
            print("*****")
        else:
            tval = int(str(i[0][0].pop())+str(i[0][1].pop())+str(i[0][2].pop()))
        
        ssum += tval
    print(ssum)
main()