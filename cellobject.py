class Cell:
	'''A Class that Represents a Cell'''

	def __init__(self, xcord, ycord, minestatus):
		self.xcord = xcord
		self.ycord = ycord
		self.minestatus = minestatus

	def getx(self):
		'''Returns xcord'''
		return self.xcord

	def gety(self):
		'''Returns ycord'''
		return self.ycord

	def getminestatus(self):
		'''Return minestatus'''
		return self.minestatus

	def setx(self, newx):
		self.xcord = newx

	def sety(self, newy):
		self.ycord = newy

	def setminestatus(self, minestatus):
		self.minestatus = minestatus

	def __repr__(self):
		return 'Cell('+str(self.xcord)+','+str(self.ycord)+','+str(self.minestatus)+')'