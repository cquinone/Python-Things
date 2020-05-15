from tkinter import *
import numpy as np
import random
import enchant
import re
import os
from os import system
from platform import system as platform


four_dice = ["AAEEGN","ABBJOO","ACHOPS","AFFKPS","AOOTTW","CIMOTU","DEILRX","DELRVY","DISTTY","EEGHNW","EEINSU","EHRTVW","EIOSST","ELRTTY","HIMNUQu","HLNNRZ"]
five_dice = ["AAAFRS","AAEEEE","AAFIRS","ADENNN","AEEEEM","AEEGMU","AEGMNN","AFIRSY","BJKQXZ","CCENST","CEIILT","CEILPT","CEIPST","DDHNOT","DHHLOR","DHLNOR","DHLNOR","EIIITT","EMOTTT","ENSSSU","FIPRSY","GORRWV","IPRRRY","NOOTUW","OOOTTU"]


def sort_scores(data):
	order = dict()
	fixed = []
	lines = open("scores.txt").read().split("\n")
	curr_score = str(data.score)
	if len(curr_score) == 1:
		curr_score = "0"+curr_score
	lines.append(curr_score+"	"+data.name)
	for score in lines:
		fixed.append(re.sub(r"\t", "", score))	
	for entry in fixed:
		if entry == "":
			continue
		score = entry[:2]
		name = entry[2:]
		if score in order.keys():
			if name == order[score]:
				continue
			name = name + "," + order[score]
		order[score] = name
	high = sorted(order) #sort them
	high = high[::-1] #reverse
	open('scores.txt', 'w').close() #clear file
	file = open("scores.txt","w+")
	for score in high:
		file.write(score+"	"+order[score])
		file.write("\n")
	file.close()


def wordbank(canvas, data):
	font = "Arial 12 bold"
	compiled = ""
	counter = 0
	for word in data.found:
		if counter%7 != 0:
			compiled = compiled + word + ", "
		else:
			compiled = compiled + "\n"
			compiled = compiled + word + ", "
			counter = 0
		counter = counter + 1
	
	#add score
	canvas.create_text(325,280, text="SCORE: "+str(data.score), font=font)
	canvas.create_text(325,300, text="# words found: "+str(len(data.found)), font=font)
	canvas.create_text(80,330, text="UNIQUE FOUND WORDS: ", font=font)
	canvas.create_text(92,340, text="---------------------------------------------", font=font)
	#add words found
	canvas.create_text(12,330, text=compiled, font=font, anchor=NW) #include anchor to make top left corner exactly there


#score of given word
def score(data,canvas):
	font = "Arial 10 bold"
	word = data.found[len(data.found)-1] #last word added (2 clicks)
	if len(word) == 4 or len(word) == 3:
		add = 1
	if len(word) == 5:
		add = 3
	if len(word) == 6:
		add = 5
	if len(word) == 7:
		add = 9
	if len(word) >= 8:
		add = 13
	data.score = data.score + add #update total score
	canvas.create_text(350,80, text="Plus "+ str(add)+"!", font=font)
	return add


#new board pick, not draw
def newBoard(data):
	N = data.len
	if N == 5:
		dice = five_dice
	if N == 4:
		dice = four_dice

	init_b = np.chararray((N,N))
	for i in range(0,N):
		for j in range(0,N):
			die = random.choice(dice)
			dice.remove(die)
			letter = random.choice(die) #0:26 to cut off capital letters, these could clash later with checking words
			init_b[i,j] = letter
	return init_b


def match(data, x, y):
	x = int((x-12)/40) #sub xinit jump and divide by spacing
	y = int((y-12)/40)
	if x < 0 or x >= data.len:
		#write to board that you cant pick there, redraw -> going to drawboard brings you where? back?
		data.outside = True
		return None
	if y < 0 or y >= data.len:
		data.outside = True
		return None
	else:
		return data.grid[x,y]


def grab_letter(data, end_x, end_y, canvas):
	old_x = data.curr_pos[0]
	old_y = data.curr_pos[1]
	data.curr_pos[0] = data.curr_pos[0]+end_x
	data.curr_pos[1] = data.curr_pos[1]+end_y
	letter = match(data, int(data.curr_pos[0]),int(data.curr_pos[1]))
	if letter != None:
		data.curr_word = data.curr_word + letter
		canvas.create_line(old_x,old_y, data.curr_pos[0], data.curr_pos[1])
	return data


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
			data = grab_letter(data, -40, 0, canvas)
		if event.char == "w":
			data = grab_letter(data, 0, -40, canvas)
		if event.char == "d":
			data = grab_letter(data, 40, 0, canvas)
		if event.char == "s":
			data = grab_letter(data, 0, 40, canvas)
		if event.char == "q":
			data = grab_letter(data, -40, -40, canvas)
		if event.char == "e":
			data = grab_letter(data, 40, -40, canvas)
		if event.char == "z":
			data = grab_letter(data, -40, 40, canvas)
		if event.char == "c":
			data = grab_letter(data, 40, 40, canvas)
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
	font = "Arial 12 bold"
	x = event.x
	y = event.y
	canvas.create_oval(x-7,y-7,x+7,y+7)
	data.clicks = data.clicks + 1
	if data.timer == 0:
		return None, 0,0, None
	if data.clicks == 2:
		#now the word has ended, reset and check, print if good
		data.clicks = 0
		if data.d.check(data.curr_word) or (data.d.check(data.curr_word[0:1]+"U"+data.curr_word[1:]) and data.curr_word[0:1] == "Q"):
			#add to list if long enough
			if len(data.curr_word) <= 2:
				add = -2 #use this val for too short
				data.curr_word = ""
				return None, 0,0, add
			if data.curr_word not in data.found:
				data.found.append(data.curr_word)
				add = score(data,canvas)
			else:
				add = -3 #use for repeat word
			data.curr_word = ""
		else:
			add = -1
			data.curr_word = ""
		return None,0,0, add
	letter = match(data, int(x),int(y))
	if letter != None:
		data.curr_word = data.curr_word + letter
	data.curr_pos[0] = x
	data.curr_pos[1] = y
	add = None #not making word here, use None to ignore printing "Plus" stuff
	return letter, event.x,event.y, add


def timerFired(data,canvas,root):
	font = "Arial 12 bold"
	if data.timer == 0:
		#print game over, end game, record score
		font = "Arial 34 bold"
		canvas.create_text(120, 242, text="GAME OVER!", font=font)
		wordbank(canvas, data)
		sort_scores(data)
		#reset everything
		data.curr_word = ""
		data.timer = 81
		data.pause = True
		data.grid = newBoard(data)
		data.found = []
	else:
		data.timer = data.timer - 1
		if data.timer != 81:
			canvas.delete("curr")
		canvas.create_text(350,50, text=str(data.timer), font=font, tag="curr")
		#canvas.create_text(350,50, text="||||||||||", font=font, fill="white")
		#canvas.create_text(340,50, text="||||||||||", font=font, fill="white")
		#canvas.create_text(360,50, text="||||||||||", font=font, fill="white")
		#save above, way to create white space over existing text without redrawing		


def run():
	def timerFiredWrapper(canvas, data):
		timerFired(data,canvas, root)
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
		font = "Arial 12 bold" 
		if data.pause == False:		
			letter,x,y, add = word_start(canvas, event, data)
			if event.y < 0: #if you go off the top? (not sure)
				data.clicks = data.clicks - 1
			if data.curr_word == "" and event.y >= 0: #successfully double clicked now? so redraw all without added lines?
				drawboardWrapper(canvas, data)
				if add == -1: #use -1 for not a word, but still assign add
					canvas.create_text(300, 80, text="Not a word", font=font)
				if add == -2: #use for too short of word
					canvas.create_text(300, 80, text="Too short", font=font)
				if add == -3: #using for repeated word
					canvas.create_text(320, 80, text="Already found", font=font)
				if add >= 0 and add != None:
					canvas.create_text(300, 80, text="Plus "+str(add)+" !", font=font)

	def keyPressedWrapper(event, canvas, data):
		key = keyPressed(event, data, canvas)
		if key == "n":
			data.pause = False
			data.clicks = 0 # reset to fix extra clicks?
			data.score = 0
			drawboardWrapper(canvas, data)
			timerFiredWrapper(canvas, data)
	
	np.set_printoptions(precision=3,linewidth=200, suppress=True)
	print("NOTE: TREAT Q AS BOTH Q AND QU")
	name = input("NAME: ")
	size = input("what size: ")
	if size == "big" or size == "5":
		N = 5	
		dice = list(five_dice)  # use list command to copy the global
	if size == "small" or size == "4":
		N = 4
		dice = list(four_dice)
	init_b = np.chararray((N,N))
	for i in range(0,N):
		for j in range(0,N):
			die = random.choice(dice)
			dice.remove(die)
			letter = random.choice(die) #0:26 to cut off capital letters, these could clash later with checking words
			init_b[i,j] = letter
	
	print("")
	# Set up data and call init
	class Struct(object): pass
	data = Struct()
	#data.outside = False #weird try to catch words made in and out of grid in one chain
	data.grid = init_b #copy grid
	data.len = N
	data.clicks = 0
	data.curr_pos = [0,0]
	data.curr_word = ""
	data.found = [] #list of found words
	data.d = enchant.Dict("en_US") #dictionary to check words in
	data.timer = 81 #game length
	data.timerDelay = 1000 #milliseconds
	data.pause = False #pause game
	data.score = 0
	data.name = name
	# create the root and the canvas
	root = Tk()
	root.lift()
	root.attributes("-topmost", True)
	# hack way of making winow focused on, works for non app version, just script run from terminal
	if platform() == 'Darwin':
		system('''/usr/bin/osascript -e 'tell app "Finder" to set frontmost of process "python" to true' ''')
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

run()


