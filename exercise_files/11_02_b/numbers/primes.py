from numbers.factors import getFactors

def isPrime(n, foundPrimes=None):
    # rewrite isPrime() function to use the getFactors() function by importing the factors module (see above)
    # foundPrimes = range(2, int(n**0.5)) if foundPrimes is None else foundPrimes
    # for factor in foundPrimes:
    #     if n % factor == 0:
    #         return False
    # return True
    return len(getFactors()) == 2
    # take advantage of the fact that prime numbers have exactly 2 factors

def listPrimes(max):
    foundPrimes = []
    for n in range(2, max):
        if isPrime(n, foundPrimes):
            foundPrimes.append(n)
    return foundPrimes
    
