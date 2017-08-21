from Tkinter import *
import math 


def lines(canvas, cord, connect):
	for item in connect:
		for name in connect[item]:
				canvas.create_line(cord[item][0], cord[item][1], cord[name][0], cord[name][1])



def draw(canvas, connect, width, height):
	num = len(connect)
	deg = 360/num
	x = width/2
	y = height/2
 	i = 0
	cord = {}
	canvas.create_oval(width/2-300, height/2-300, width/2 + 300, height/2 + 300)
	for item in connect:
		canvas.create_oval((x+300*math.cos(math.radians(deg*i)))-20, (y-300*math.sin(math.radians(deg*i)))-20, (x+300*math.cos(math.radians(deg*i))+20), (y-300*math.sin(math.radians(deg*i)))+20, fill="red")
		canvas.create_text((x+300*math.cos(math.radians(deg*i))), (y-300*math.sin(math.radians(deg*i))), text=item, fill="black", font="Helvetica")
		cord[item] = [(x+300*math.cos(math.radians(deg*i))), (y-300*math.sin(math.radians(deg*i)))]
		i = i+1
		print item, connect[item]
 	lines(canvas, cord, connect)
	
 

def runDrawing(width,height):
    root = Tk()
    connect = {"georg":["chris","bob","tom"], "tom":["chris"], "bob":["tom","chris","georg"], "chris":["tom","georg"], "dylan":["georg", "bob"]}
    canvas = Canvas(root, width=width, height=height)
    canvas.pack()
    draw(canvas, connect, width, height)
    root.mainloop()
    

runDrawing(900, 800)


