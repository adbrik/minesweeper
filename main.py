from cellobject import *
import random

def generate_cords(xmax,ymax,number):
	l = []
	switch = True
	for i in range(number):
		while (switch):
			a = (random.randint(0, xmax),random.randint(0, ymax))
			if a not in l:
				switch = False
		l.append(a)
		switch = True
	return l

def bombCount(bomb_cords,x,y):
	count = 0
	for i in bomb_cords:
		if (i[0] in range (x-1,x+2))and(i[1] in range (y-1,y+2)):
			count+=1
	### take this out later
	if count == 0:
		count = ' '

	return str(count)

def initialize(width, height, bombs):
	a = Board(width,height,[])
	b2 = []
	c = False
	d = generate_cords (width, height, bombs)

	for i in range (a.getheight()):
		b = []
		for j in range (a.getwidth()):
			f = bombCount(d,i,j)
			if (i,j) in d:
				c = True
				f= 'O'
			b.append(Cell(i,j,c,False,f))
			c =False
		b2.append(b)
	a.setCells(b2)
	return a
			

a = initialize(8,8,10)

a.printBoard()
a.test()