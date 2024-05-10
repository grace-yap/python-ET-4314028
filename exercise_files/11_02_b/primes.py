
def isPrime(n, foundPrimes=None):
    foundPrimes = range(2, int(n**0.5)) if foundPrimes is None else foundPrimes
    for factor in foundPrimes:
        if n % factor == 0:
            return False
    return True

def listPrimes(max):
    foundPrimes = []
    for n in range(2, max):
        if isPrime(n, foundPrimes):
            foundPrimes.append(n)
    return foundPrimes

# name - built-in python variable
print(f'primes.py module name is {__name__}')

# run primes.py directly from the command line
### COMMAND-LINE COMMAND (EITHER CMD OR GITBASH):
# python primes.py
### RESULT:
# primes.py module name is __main__
# - main is the default module name for the main piece of code that you're running directly

# one common pattern in python when writing modules and packages is to take advantage of this __name__ variable
#    by creating a code that will only be run if the module is run directly versus being imported

# we can add some helper text if your users get confused by doing this:
if __name__ == '__main__':
    print('This is a module! Please import using:\nimport primes')

### COMMAND-LINE COMMAND (EITHER CMD OR GITBASH): [AFTER ADDING ABOVE HELPER TEXT]
# python primes.py
### RESULT:
# primes.py module name is __main__
# This is a module! Please import using:
# import primes

# BUT if you run "python useModule.py", the helper text won't get printed out:
# primes.py module name is primes
# [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
