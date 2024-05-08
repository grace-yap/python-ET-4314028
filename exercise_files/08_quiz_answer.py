class NonIntArgumentException(Exception):
    pass

def handleNonIntArguments(func):
    def wrapper(*args):
        # handles any number of arguments by iterating through the args tuple
        for item in args:
            if type(item) is not int:
                raise NonIntArgumentException()
        # if you don't return this, this means sum is not going to return anything,
        # and the caller is going to be confused when they don't get the result
        return func(*args)
    return wrapper

@handleNonIntArguments
def sum(a, b, c):
    return a + b + c

try:
    result = sum(1, 2, 3)
    print('result = ', result)
    print('This should not print out')
except NonIntArgumentException as e:
    print('Hooray!')

try:
    result = sum(1, 2, 'a')
    print('This should not print out')
except NonIntArgumentException as e:
    print('Hooray!')

try:
    result = sum(1.0, 2.0, 3.0)
    print('This should not print out')
except NonIntArgumentException as e:
    print('Hooray!')

try:
    result = sum(None, None, None)
    print('This should not print out')
except NonIntArgumentException as e:
    print('Hooray!')