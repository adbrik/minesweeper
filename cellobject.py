class Cell:
	'''A Class that Represents a Cell'''

	def __init__(self, xcord, ycord, minestatus, triggered, minecount):
		self.xcord = xcord
		self.ycord = ycord
		self.minestatus = minestatus
		self.triggered = triggered
		self.minecount = minecount

	def getx(self):
		'''Returns xcord'''
		return self.xcord

	def gety(self):
		'''Returns ycord'''
		return self.ycord

	def getminestatus(self):
		'''Return minestatus'''
		return self.minestatus

	def gettriggered(self):
		return self.triggered

	def getminecount(self):
		return self.minecount

	def setx(self, newx):
		self.xcord = newx

	def sety(self, newy):
		self.ycord = newy

	def setminestatus(self, minestatus):
		self.minestatus = minestatus

	def settriggered(self, triggered):
		self.triggered = triggered

	def setminecount(self, new):
		self.minecount = new

	def __repr__(self):
		return 'Cell('+str(self.xcord)+','+str(self.ycord)+','+str(self.minestatus)+','+ str(self.triggered)+')'


class Board:

	def __init__(self, width=0, height=0, Cells=[]):
		self.width = width
		self.height = height
		self.Cells = Cells

	def getwidth(self):
		return self.width

	def getheight(self):
		return self.height

	def getCells(self):
		return self.Cells

	def printBoard(self):
		s = 'x'
		for i in range (self.getheight()):
			print ()
			for j in range (self.getwidth()):
				if self.getCells()[i][j].getminestatus():
					s = 'o'
				print ('['+self.getCells()[i][j].getminecount(), end = ']')
				s = 'x'

	def setwidth(self, new):
		self.width = new

	def setheight(self, new):
		self.height = new

	def setCells(self, new):
		self.Cells = new

