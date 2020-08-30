from PIL import Image, ImageDraw
from functools import reduce
import operator as op
import random as rand
import math
import sys


pic_width = 500
pic_height = 500
white = (255, 255, 255)
green = (41,172,32)
brown = (210,105,30)


def nchoosek(n,k):
	k = min(k,n-k)
	numerator = reduce(op.mul,range(n,n-k,-1),1)
	denominator = reduce(op.mul, range(1,k+1),1)
	return numerator // denominator


# return bezier point corresponding to given control points and t
def bezier(t,points):
	b_point = [0,0]
	n = len(points)-1  # to get correct binaomial coeffs
	for i in range(0,n+1):
		#print("i, points[i], com(n,i):", i,points[i],nchoosek(n,i))
		b_point[0] = b_point[0] + nchoosek(n,i)*((1-t)**(n-i))*(t**i)*points[i][0]
		b_point[1] = b_point[1] + nchoosek(n,i)*((1-t)**(n-i))*(t**i)*points[i][1]
	return b_point


def draw_curve(image1,draw,points):
	for i in range(0,len(points)-1):
		if i != len(points)-1:
			draw.line([points[i][0],points[i][1],points[i+1][0],points[i+1][1]],fill=brown,width=4)

	for t in range(0,1000):
		t = t/1000.0
		curr_point = bezier(t,points)
		print(curr_point,t)
		draw.point([curr_point[0],curr_point[1]], fill=green)

	return image1,draw


def create_curve_img(filename): 
	# PIL create an empty image and draw object to draw on
	# memory only, not visible
	image1 = Image.new("RGB", (pic_width, pic_height), white)
	draw = ImageDraw.Draw(image1)

	# example points, modify this
	points = [[1,1],[312,90],[422,61],[499,301]]

	# actually draw the points
	image1, draw = draw_curve(image1, draw, points)
	
	# PIL image can be saved as .png .jpg .gif or .bmp file (among others)
	image1.save(filename+".png")


create_curve_img("test")