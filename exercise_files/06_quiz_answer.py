# recursive function
def triangle(num):
    if num == 1:
        return num
    return num + triangle(num - 1)
    # triangle() calls itself

# this is a similar recursive function to the factorial challenge by just changing + to * and (return num if num == 1) to (return 1 if num == 0):
def factorial(num):
    if num == 0:
        return 1
    return num * factorial(num - 1)

def square(num):
    return triangle(num) + triangle (num - 1)