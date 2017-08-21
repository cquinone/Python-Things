
import sys

#create picture
def clp(pict):
	for i in range(len(pict)):
		for j in range(len(pict[0])):
			pict[i][j] = " "
	return pict

def new(m,n):
	print ""
	pic = []
	for x in range(m):
		pic.append([])
		for y in range(n):
			pic[x].append(" ")
	print "set picture to: "
	return pic

def display(pic):
	print ""
	#for i in range(len(pic)+1):
	#	sys.stdout.write("-")
	#sys.stdout.flush()
	#print "-"
	for row in pic:
		line = "|"
		for cell in row: 
			line = line + cell
		line = line + "|"
		print line
	
	#for i in range(len(pic)+2):
	#	sys.stdout.write("-")
	#sys.stdout.flush()
	print ""
	return None

def line(x1,y1,x2,y2):
	points = []
	dx = abs(x2 - x1)
	dy = abs(y2 - y1)
	x, y = x1, y1
	sx = -1 if x1 > x2 else 1
	sy = -1 if y1 > y2 else 1
	if dx > dy:
		err = dx / 2.0
		while x != x2:
			point = [x,y]
			points.append(point)
			x = x + sx
			err = err - dy
			if err < 0:
				y = y + sy
				err = err + dx

	else:
		err = dy / 2.0
		while y != y2:
			point = [x,y]
			points.append(point)
			y = y + sy
			err = err - dx
			if err < 0:
				x = x + sx
				err = err + dy
	point = [x2,y2]
	points.append(point)
	return points

while True:
	print "..............................................................................."
	cmd = raw_input("What will you do? (Enter hlp to see commands) ")
	if cmd == "hlp":
		print ""
		print "Commands:"
		print "newpic, point, line, fill, disp, clpic, clear, save, quit"
		continue
	if cmd == "newpic":
		print ""
		m,n = raw_input("Give size as m n: ").split()
		pict = new(int(m),int(n))
		display(pict)
		continue

	if cmd == "disp":
		 if ('pict' in locals() or 'pict' in globals() ):
		 	display(pict)
		 	continue
		 else:
			print ""
			print "No current picture"
			continue
	if cmd == "save":
		if ('pict' in locals() or 'pict' in globals() ):
			print ""
			filename = raw_input('Filename to save to (Use ".txt" extension) ')
			file = open(filename, 'w')
			for row in pict:
				line = ""
				for cell in row:
					line = line + cell
				file.write(line + "\n")
			file.close()
			continue
		else:
			print ""
			print "No current picture"
			continue
	if cmd == "clpic":
		if ('pict' in locals() or 'pict' in globals() ):
			pict = clp(pict)
			display(pict)
			continue
		else:
			print ""
			print "No current picture"
			continue

	if cmd == "point":
		if ('pict' in locals() or 'pict' in globals() ):
			print ""
			color = raw_input("What color? ")[0]
			x,y = raw_input("What point? ").split()
			x,y = int(x), int(y)
			if (x > len(pict[0])-1 or x < 0) or (y > len(pict)-1 or y < 0):
				print "That point is out of bounds"
				continue
			pict[y][x] = color
			display(pict)
			continue

	if cmd == "line":
		if ('pict' in locals() or 'pict' in globals() ):
			print ""
			color = raw_input("what color? ")[0]
			x1,y1 = raw_input("What initial point? ").split()
			x1,y1 = int(x1), int(y1)
			if (x1 > len(pict[0])-1 or x1 < 0) or (y1 > len(pict)-1 or y1 < 0):
				print "The inital point is out of bounds"
				continue
			x2,y2= raw_input("What end point? ").split()
			x2,y2 = int(x2), int(y2)
			if (x2 > len(pict[0])-1 or x2 < 0) or (y2 > len(pict)-1 or y2 < 0):
				print "The end point is out of bounds"
				continue
			else:
				points = line(x1,y1,x2,y2)
				for point in points:
					x = point[0] 
					y = point[1]
					pict[x][y] = color
				display(pict)
				continue
		else:
			print ""
			print "No current picture"
			continue
	
	if cmd == "fill":
		if ('pict' in locals() or 'pict' in globals() ):
			print ""
			color = raw_input("what color? ")[0]
			x1,y1 = raw_input("What initial point? ").split()
			x1,y1 = int(x1), int(y1)
			if (x1 > len(pict[0])-1 or x1 < 0) or (y1 > len(pict)-1 or y1 < 0):
				print "The inital point is out of bounds"
				continue
			x2,y2= raw_input("What end point? ").split()
			x2,y2 = int(x2), int(y2)
			if (x2 > len(pict[0])-1 or x2 < 0) or (y2 > len(pict)-1 or y2 < 0):
				print "The end point is out of bounds"
				continue
			
			else:
				for x in range(x1,x2+1):
					for y in range(y1,y2):
						pict[x][y] = color
						print "x,y filled: ", x,y

				display(pict)
				continue
		else:
			print ""
			print "No current picture"
			continue	
			#else:

	if cmd == "clear":
		for i in range(100):
			print ""
		continue

	if cmd == "quit":
		quit()

	else:
		print "Not a valid command"
		continue




#pict = new(50,50) #if pict != none, and new called--> nah tho (one pic at time)
#display(pict)
#fill(pict)
#commands: newpic(m,n) ---> picmn, point(x,y, color)-->xyred, line(x1,y1,x2,y2, color)---> x1y1x2y2red
# clear--->fill(color (here, white), all points)--> fillwhite{corner top, corner bottom}, save(filename)-->savefilename
#quit--> quit