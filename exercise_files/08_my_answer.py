### INCOMPLETE ANSWER!!!
### FAILED TEST CASE (1.0, 2.0, 3.0)

def handleNonIntArguments(func):
    def wrapper(*args):
        try:
            return func(*args)
        except TypeError:
            print('This is a type error from handleNonIntArguments!')
    return wrapper

class NonIntArgumentException(Exception):
    pass

@handleNonIntArguments
def sum(a, b, c):
    if (isinstance(a, int)) and isinstance(b, int) and isinstance(c, int):
        return a + b + c
    raise NonIntArgumentException

try:
    print('first try')
    result = sum(1, 2, 'a')
    print('This should not print out')
except NonIntArgumentException as e:
    print('Hooray!')

try:
    print('second try')
    result = sum(1, 2, 3)
    print('This should not print out')
except NonIntArgumentException as e:
    print('Hooray!')

try:
    print('third try')
    result = sum(1.0, 2.0, 3.0)
    print('This should not print out')
except NonIntArgumentException as e:
    print('Hooray!')
