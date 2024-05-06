class Shape:
	width = 5
	height = 5
	printChar = '#'

	def printRow(self, i):
		raise NotImplementedError("Will be implemented by children extending this class")

	def print(self):
		for i in range(self.height):
			# print('SHAPE - printRow')
			# print('i = ', i)
			# print('height = ',self.height)
			self.printRow(i)

class Square(Shape):
	def printRow(self, i):
		# print('SQUARE - printRow')
		# print('width = ', self.width)
		print(self.printChar * self.width)

class Triangle(Shape):
	def print(self, i):
		for i in range(1, self.width + 1):
			print(self.printChar * i)

square = Square()
square.print()
# flow:
# 1. call print()
# 2. child classs Square does not have print()
# 3. call print() from parent class Shape
# 4. Shape-print() calls Square-printRow() [i=0]
# 5. Square-printRow() prints first row of chars
# 6. back to for loop in Shape-print()
# 7. Shape-print() calls Square-printRow() [i=1]
# 8. Square-printRow() prints second row of chars
# 9. back to for loop in Shape-print()
# 10 ...

triangle = Triangle()
triangle.print(5)
