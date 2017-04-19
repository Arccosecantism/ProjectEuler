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
                val = set([int(i[j*9+k])])
                if val == set([0]):
                    val = set([])
                grid[j].append(val)
        puzzles.append(grid)
    return puzzles
    
def getNumberConstraints(square, sudokuSquare):
    #basic numbers
    if len(sudokuSquare[square[0]][square[1]]) >= 1:
        return set([])
    inds = getAllConstraintIndeces(square)
    constraints = set([])
    for i in inds:
        if len(sudokuSquare[i[0]][i[1]]) == 1:
            constraints|=sudokuSquare[i[0]][i[1]]
    return constraints
def getAllConstraintIndeces(square):
    return getRowIndeces(square)|getColumnIndeces(square)|getBoxIndeces(square)
def getRowIndeces(square):
    return set([(square[0],i) for i in range(9)])

def getColumnIndeces(square):
     return set([(i,square[1]) for i in range(9)])

def getBoxIndeces(square):
    retset = set([])
    tr = (3*(square[0]//3),3*(square[1]//3))
    for i in range(tr[0],tr[0]+3):
        for j in range(tr[1],tr[1]+3):
            retset.add((i,j))
    return retset
def getSmallNumbers(sudokuSquare):
    print("k")
    #for i in range(len(sudokuSquare)):
       # for j in range(len(sudokuSquare)):
def main():
    puzzles = getPuzzles()
    for i in puzzles:
        for j in i:
            print(j)
        print("---")
    print(getAllConstraintIndeces((0,0)))

main()