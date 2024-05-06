class Shape:
	width = 5
	height = 5
	printChar = '#'

	def printRow(self, i):
		raise NotImplementedError("Will be implemented by children extending this class")

	# print() - iterates through the height, printing out one row at a time,
 	# 			calling out printRow() with the height index (i) where 0 is the top row and 4 is the bottom row (for default height = 5)
	def print(self):
		for i in range(self.height):
			self.printRow(i)

class Square(Shape):
	# doesn't even use the height index (i) that gets passed in
	def printRow(self, i):
		print(self.printChar * self.width)

class Triangle(Shape):
	# Right Triangle
	# def printRow(self, i):
	# 	print(self.printChar*(i + 1))

	#Equilateral Triangle
	height = 6
	# we need something that's wider than it is tall
	# this is because for each row, to stack on top of subsequent larger rows in a symmetrical way, the number of characters in each row needs to be odd
	width = 2 * height

	def printRow(self, i):
		# triangle width at each height
  		# this guarantees that the width of our triangle at height i will always be an odd number and we can stack these rows symmetrically
		triangleWidth = i * 2 + 1
		# there needs to be some initial padding space before we start printing the row
  		# and the padding space is going to get smaller as we go down
		# we can calculate the padding as the width of the entire figure, which is 2 * height, minus the triangle width
  		# divide (self.width - triangleWidth) by 2 because we want to have equal padding on both sides
		# convert (self.width - triangleWidth)/2 to int, so we can multiply it by our character to get the string
		padding = int((self.width - triangleWidth)/2)
		print(' ' * padding + self.printChar * triangleWidth)

triangle = Triangle()
triangle.print()