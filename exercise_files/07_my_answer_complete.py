class Shape:
    printChar = '#'

    def __init__(self, height, sides, type):
        self.height = height
        self.sides = sides
        self.type = type

    def printShape(self, sides, type):
        if (sides == 4) and (type == 'square'):
            for i in range(self.height):
                print(self.printChar * self.height)
        elif (sides == 3) and (type == 'right'):
            for i in range(1, self.height + 1):
                print(self.printChar * i)
        elif (sides == 3) and (type == 'equilateral'):
            for i in reversed(range(0, int(self.height))):
                if self.height % 2 == 0:
                    print((' ' * i) + (self.printChar * (self.height - i) * 2))
                if self.height % 2 == 1:
                    print((' ' * i) + (self.printChar * ((self.height - i)*2 - 1)))

class Square(Shape):
	def printSquare(self):
          self.printShape(4, self.type)

class Triangle(Shape):
    def printTriangle(self):
        self.printShape(3, self.type)
		
print('SQUARE - 5')
square = Square(5, 4, 'square')
square.printSquare()
# flow:
# 1. call print()
# 2. child classs Square has not print()
# 3. call print() from parent class Shape
# 4. Shape-print() calls Square-printRow() [i=0]
# 5. Square-printRow() prints first row of chars
# 6. back to for loop in Shape-print()
# 7. Shape-print() calls Square-printRow() [i=1]
# 8. Square-printRow() prints second row of chars
# 9. back to for loop in Shape-print()
# 10 ...

print('RIGHT TRIANGLE - 5')
triangle = Triangle(5, 3,'right')
triangle.printTriangle()

print('EQUILATERAL TRIANGLE - 6')
triangle = Triangle(6, 3,'equilateral')
triangle.printTriangle()

print('EQUILATERAL TRIANGLE - 7')
triangle = Triangle(7, 3,'equilateral')
triangle.printTriangle()

# height = 5
    #               4 spaces, 1 #
   ###              3 spaces, 3 #
  #####             2 spaces, 5 #
 #######            1 space, 7 #
#########           0 space, 9 #

# height = 6
     ##              5 spaces, 2 #
    ####             4 spaces, 4 #
   ######            3 spaces, 6 #       
  ########           2 space, 8 #        
 ##########          1 space, 10 #       
############         0 space, 12 #

# height = 7
      #             6 spaces, 1 #
     ###            5 spaces, 3 #
    #####           4 spaces, 5 #
   #######          3 spaces, 7 #
  #########         2 spaces, 9 #
 ###########        1 space, 11 #
#############       0 space, 13 #

