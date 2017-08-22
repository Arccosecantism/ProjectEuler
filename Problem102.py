import math
from time import time
import os

def readTriangles():
	f = open("TextFiles\\TrianglesProblem102.txt", 'r')
	lines = f.readlines()
	triangles = []
	for i in lines:
		tl = map(int, i[:-1].split(","))
		tmptri = ((tl[0],tl[1]),(tl[2],tl[3]),(tl[4],tl[5]))
		triangles.append(tmptri)
	return triangles



def absAreaTriangle(tri):
	return abs((tri[0][0]*tri[1][1]+tri[1][0]*tri[2][1]+tri[2][0]*tri[0][1]) - 
			   (tri[0][1]*tri[1][0]+tri[1][1]*tri[2][0]+tri[2][1]*tri[0][0]))*.5


def testOriginInside(tri):
	tpoint = (0,0)
	totalAreaA = absAreaTriangle(tri)
	totalAreaB = 0
	for i in range(3):
		
		tmpArea = absAreaTriangle((tpoint, tri[i], tri[(i+1)%3]))
		if tmpArea == 0:
			return 0
		else:
			totalAreaB += tmpArea

	if totalAreaB == totalAreaA:
		return 1
	return 0	

def main():
	t0 = time()
	triangles = readTriangles()
	ssum = 0
	for i in triangles:
		ssum += testOriginInside(i)
	
	print("Time Elapsed:", time()-t0)
	print(ssum)
	#print(testOriginInside(((0,0),(100,0),(0,100))))

main()