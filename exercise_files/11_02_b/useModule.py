# import the whole primes module
# import primes

# print(primes.isPrime(5))

### COMMAND-LINE COMMAND (EITHER CMD OR GITBASH):
# python useModule.py
### RESULT:
# True

# import an individual function, instead of the whole module
from primes import listPrimes
# imports primes module at the top
# when primes gets imported, python will actually run through and execute all of the code in this module

print(listPrimes(100))
# you can now call the functon directly, other than saying primes.ListPrimes

### COMMAND-LINE COMMAND (EITHER CMD OR GITBASH):
# python useModule.py
### RESULT:
# [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]

### COMMAND-LINE COMMAND (EITHER CMD OR GITBASH): [AFTER ADDING print(f'primes.py module name is {__name__}') IN primes.py]
# python useModule.py
### RESULT:
# primes.py module name is primes
# [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
# - when we run useModule.py, the name of that module will print out
# - the module name is now primes, not main