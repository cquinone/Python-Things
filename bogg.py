from Tkinter import *
import numpy as np
import random
import enchant

#function to make new baord when new games tarts after first game
def newBoard(data):
	N = data.len
	if N == 5:
		dice = ["AAAFRS","AAEEEE","AAFIRS","ADENNN","AEEEEM","AEEGMU","AEGMNN","AFIRSY","BJKQXZ","CCENST","CEIILT","CEILPT","CEIPST","DDHNOT","DHHLOR","DHLNOR","DHLNOR","EIIITT","EMOTTT","ENSSSU","FIPRSY","GORRWV","IPRRRY","NOOTUW","OOOTTU"]
	if N == 4:
		dice = ["AAEEGN","ABBJOO","ACHOPS","AFFKPS","AOOTTW","CIMOTU","DEILRX","DELRVY","DISTTY","EEGHNW","EEINSU","EHRTVW","EIOSST","ELRTTY","HIMNUQu","HLNNRZ"]

	init_b = np.chararray((N,N))
	for i in range(0,N):
		for j in range(0,N):
			die = random.choice(dice)
			dice.remove(die)
			letter = random.choice(die) #0:26 to cut off capital letters, these could clash later with checking words
			init_b[i,j] = letter

	print(init_b)
	return init_b

def match(data, x, y):
	x = int((x-12)/40) #sub xinit jump and divide by spacing
	y = int((y-12)/40)
	#print "realx, realy: ", realx, realy
	#print x,y, " letter: ", data.grid[x,y]
	#print ""
	if x < 0 or x >= data.len:
		#write to board that you cant pick there, redraw -> going to drawboard brings you where? back?
		return None
	if y < 0 or y >= data.len:
		return None
	else:
		return data.grid[x,y]


def keyPressed(event, data, canvas):
	if event.char == "l":
		print("words found: ")
		print(data.found)
		print("")

	if data.clicks != 1:
		#dont do any directional stuff
		pass
	else:
		#do dir stuff here
		#check data current place, draw a line to new spot, update data curr place, add letter on new spot
		# --- canvas create line to new place depending on key press, update crr place
		if event.char == "a":
			canvas.create_line(data.curr_pos[0],data.curr_pos[1], data.curr_pos[0]-40, data.curr_pos[1])
			data.curr_pos[0] = data.curr_pos[0]-40
			letter = match(data, int(data.curr_pos[0]),int(data.curr_pos[1]))
			if letter != None:
				data.curr_word = data.curr_word + letter
		if event.char == "w":
			canvas.create_line(data.curr_pos[0],data.curr_pos[1], data.curr_pos[0], data.curr_pos[1]-40)
			data.curr_pos[1] = data.curr_pos[1]-40
			letter = match(data, int(data.curr_pos[0]),int(data.curr_pos[1]))
			if letter != None:
				data.curr_word = data.curr_word + letter
		if event.char == "d":
			canvas.create_line(data.curr_pos[0],data.curr_pos[1], data.curr_pos[0]+40, data.curr_pos[1])
			data.curr_pos[0] = data.curr_pos[0]+40
			letter = match(data, int(data.curr_pos[0]),int(data.curr_pos[1]))
			if letter != None:
				data.curr_word = data.curr_word + letter
		if event.char == "s":
			canvas.create_line(data.curr_pos[0],data.curr_pos[1], data.curr_pos[0], data.curr_pos[1]+40)
			data.curr_pos[1] = data.curr_pos[1]+40
			letter = match(data, int(data.curr_pos[0]),int(data.curr_pos[1]))
			if letter != None:
				data.curr_word = data.curr_word + letter
		if event.char == "q":
			canvas.create_line(data.curr_pos[0],data.curr_pos[1], data.curr_pos[0]-40, data.curr_pos[1]-40)
			data.curr_pos[0] = data.curr_pos[0]-40
			data.curr_pos[1] = data.curr_pos[1]-40
			letter = match(data, int(data.curr_pos[0]),int(data.curr_pos[1]))
			if letter != None:
				data.curr_word = data.curr_word + letter
		if event.char == "e":
			canvas.create_line(data.curr_pos[0],data.curr_pos[1], data.curr_pos[0]+40, data.curr_pos[1]-40)
			data.curr_pos[0] = data.curr_pos[0]+40
			data.curr_pos[1] = data.curr_pos[1]-40
			letter = match(data, int(data.curr_pos[0]),int(data.curr_pos[1]))
			if letter != None:
				data.curr_word = data.curr_word + letter
		if event.char == "z":
			canvas.create_line(data.curr_pos[0],data.curr_pos[1], data.curr_pos[0]-40, data.curr_pos[1]+40)
			data.curr_pos[0] = data.curr_pos[0]-40
			data.curr_pos[1] = data.curr_pos[1]+40
			letter = match(data, int(data.curr_pos[0]),int(data.curr_pos[1]))
			if letter != None:
				data.curr_word = data.curr_word + letter
		if event.char == "c":
			canvas.create_line(data.curr_pos[0],data.curr_pos[1], data.curr_pos[0]+40, data.curr_pos[1]+40)
			data.curr_pos[0] = data.curr_pos[0]+40
			data.curr_pos[1] = data.curr_pos[1]+40
			letter = match(data, int(data.curr_pos[0]),int(data.curr_pos[1]))
			if letter != None:
				data.curr_word = data.curr_word + letter

	return event.char

def drawboard(canvas, data):
	#draw everything in here
	spacing = 40
	x_init = 12
	y_init = 12
	font = "Arial 12 bold"
	for i in range(0,len(data.grid[0])):  #this will get the row/column  length
		for j in range(0,len(data.grid[0])):
			canvas.create_text(30+i*spacing, 30+j*spacing, text=data.grid[i,j], font=font)
			canvas.create_line(x_init + i*(spacing),y_init,x_init+ i*(spacing),spacing*data.len + 12)
			canvas.create_line(x_init, y_init + j*(spacing), spacing*data.len + 12, y_init + j*(spacing))
			
	#manually add final lines on outside of board
	canvas.create_line(x_init + (data.len)*(spacing) ,y_init,x_init+ (data.len)*(spacing),spacing*data.len + 12)
	canvas.create_line(x_init, y_init + data.len*(spacing), spacing*data.len + 12, y_init + data.len*(spacing))
	canvas.create_text(300,50, text="Time left: ", font=font)





def word_start(canvas, event, data):
	x = event.x
	y = event.y
	canvas.create_oval(x-7,y-7,x+7,y+7)
	data.clicks = data.clicks + 1
	if data.clicks == 2:
		#now the word has ended, reset and check, print if good
		data.clicks = 0
		if data.d.check(data.curr_word) or (data.d.check(data.curr_word[0:1]+"U"+data.curr_word[1:]) and data.curr_word[0:1] == "Q"):
			#add to list if long enough
			if len(data.curr_word) <= 2:
				#print "word too short"
				data.curr_word = ""
				return None, 0,0

			data.found.append(data.curr_word)
			#print "adding this word: ", data.curr_word
			data.curr_word = ""
		else:
			#print that this word sux, not good.
			#print "word is invalid, nah"
			data.curr_word = ""
		return None,0,0

	letter = match(data, int(x),int(y))
	if letter != None:
		data.curr_word = data.curr_word + letter
	data.curr_pos[0] = x
	data.curr_pos[1] = y
	#print data.curr_word

	
	return letter, event.x,event.y
	#	#also get rid of everything, so call drawboard?
	#	drawboard(canvas,data)


def score(data,canvas):
	font = "Arial 10 bold"
	score = 0
	compiled = ""
	once = 1
	#check for doubles
	check = []
	#save them in here
	doubled = []
	for word in data.found:
		if word in check:
			print("doubled: ", word)
			print("in:", check) 
			doubled.append(word)
			continue
		#use big boggle scoring	
		if len(word) == 4 or len(word) == 3:
			score = score + 1
		if len(word) == 5:
			score = score + 2
		if len(word) == 6:
			score = score + 3
		if len(word) == 7:
			score = score + 5
		if len(word) >= 8:
			score = score + 11
		compiled = compiled + word + ", "
		check.append(word)

	#add newlines where the wordbank would get too long	
	for i in range(len(compiled)):
		if i%45 == 0 and i != 0:
			compiled = compiled[:i] + "\n" + compiled[i:]
	#remove doubles
	for word in doubled:
		data.found.remove(word)


	#add words found
	canvas.create_text(155,368, text=compiled, font=font)
	font = "Arial 12 bold"
	#add score
	canvas.create_text(295,80, text="Score: "+str(score), font=font)
	canvas.create_text(65,330, text="FOUND WORDS: ", font=font)

def timerFired(data,canvas):
	font = "Arial 12 bold"
	if data.timer == 0:
		#end game somehow?
		#or print "OVER"?
		font = "Arial 34 bold"
		canvas.create_text(120, 242, text="GAME OVER!", font=font)
		data.curr_word = ""
		data.timer = 81
		data.pause = True
		data.grid = newBoard(data)
		score(data,canvas)
		data.found = []

	else:
		#print "one second, pause is: ", data.pause
		data.timer = data.timer - 1
		if data.timer != 81:
			canvas.delete("curr")
		canvas.create_text(350,50, text=str(data.timer), font=font, tag="curr")
		#canvas.create_text(350,50, text="|||||||||||", font=font, fill="white")
		
def run():
	def timerFiredWrapper(canvas, data):
		#print "firing timer"
		timerFired(data,canvas)
		# pause, then call timerFired again
		if data.pause == False:
			canvas.after(data.timerDelay, timerFiredWrapper, canvas, data)
		else: 
			print("paused...")

	def drawboardWrapper(canvas, data):
		canvas.delete(ALL)
		drawboard(canvas, data)
		canvas.update()    

	def mousePressedWrapper(event, canvas, data):
		#mousePressed(event, data)
		if data.pause == False:
			#print "data.pause is: ", data.pause		
			letter,x,y = word_start(canvas, event, data)
			if event.y < 0:
				data.clicks = data.clicks - 1
			if data.curr_word == "" and event.y >= 0:
				drawboardWrapper(canvas, data)


	def keyPressedWrapper(event, canvas, data):
		if data.timer == 2*60:
			timerFiredWrapper(canvas, data)
		key = keyPressed(event, data, canvas)
		if key == "n":
			data.pause = False
			drawboardWrapper(canvas, data)
			timerFiredWrapper(canvas, data)
	
	np.set_printoptions(precision=3,linewidth=200, suppress=True)
	size = raw_input("what size: ")
	if size == "big" or size == "5":
		N = 5	
		dice = ["AAAFRS","AAEEEE","AAFIRS","ADENNN","AEEEEM","AEEGMU","AEGMNN","AFIRSY","BJKQXZ","CCENST","CEIILT","CEILPT","CEIPST","DDHNOT","DHHLOR","DHLNOR","DHLNOR","EIIITT","EMOTTT","ENSSSU","FIPRSY","GORRWV","IPRRRY","NOOTUW","OOOTTU"]
	if size == "small" or size == "4":
		N = 4
		dice = ["AAEEGN","ABBJOO","ACHOPS","AFFKPS","AOOTTW","CIMOTU","DEILRX","DELRVY","DISTTY","EEGHNW","EEINSU","EHRTVW","EIOSST","ELRTTY","HIMNUQu","HLNNRZ"]
	init_b = np.chararray((N,N))
	for i in range(0,N):
		for j in range(0,N):
			die = random.choice(dice)
			dice.remove(die)
			letter = random.choice(die) #0:26 to cut off capital letters, these could clash later with checking words
			init_b[i,j] = letter

	print(init_b)
	print("")
	# Set up data and call init
	class Struct(object): pass
	data = Struct()
	data.grid = init_b #copy grid
	data.len = N
	data.clicks = 0
	data.curr_pos = [0,0]
	data.curr_word = ""
	data.found = [] #list of found words
	data.d = enchant.Dict("en_US") #dictionary to check words in
	data.timer = 81 #3 minutes in seconds
	data.timerDelay = 1000 #milliseconds
	data.pause = False #pause game
	# create the root and the canvas
	root = Tk()
	root.lift()
	root.attributes("-topmost", True)
	canvas = Canvas(root, width=500, height=500)
	canvas.pack()
	# set up events
	root.bind("<Button-1>", lambda event:
	                        mousePressedWrapper(event, canvas, data))
	root.bind("<Key>", lambda event:
	                        keyPressedWrapper(event, canvas, data))
	# and launch the app
	root.mainloop()  # blocks until window is closed
	root.after(1, lambda: root.focus_force())
	root.update()
	print("bye!")

run()


