# first solution
def factorial(num):
    if type(num) != int:
        return None
    if num < 0:
        return None
    
    fact = 1
    counter = 1
    while counter <= num:
        fact = fact * counter
        counter = counter + 1
    return fact
    # how it works for factorial of 0, which must be equal to 1
    # fact = 1, and it will never enter the while loop because counter is not less than 0, so it will return 1.

# recursion - a function calls itself
# recursive solution
def factorial(num):
    if type(num) != int:
        return None
    if num < 0:
        return None
    if num == 0:
        return 1
    
    return num * (factorial(num - 1))
    # how this works:
    # example: factorial(3)
    # factorial(3) => 3 * (factorial(2))
    # factorial(3) => 3 * (2 * factorial(1))
    # factorial(3) => 3 * (2 * 1 * factorial(0))
    # factorial(3) => 3 * (2 * 1 * 1)

number = 5
result = factorial(number)
print(result)