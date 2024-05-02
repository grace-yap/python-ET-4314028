# TASK:
# Write a function called allPrimesUpTo which returns a list of all prime numbers up to the given input number

def allPrimesUpTo(num):
    primeList = [2]
    for number in range(3,num):
        for factor in primeList[0:(int(number**0.5) + 1)]:
            if number % factor == 0:
                break
        else:
            primeList.append(number)
    return primeList

print(allPrimesUpTo(200))
# [2,3,5,7]

# loop through number
#     loop through prime list (up to sqrt(number) + 1 )
#         if divisible
#             break
#     append to list

# list with [2]
# next number 3
# divide by prime numbers so far [2]
# add to list
# next number 4
# divide by prime numbers so far [2,3]
# do not add to list
# next number 5
# divide by prime numbers so far [2,3]
# add to list
# ...
# next number 53
# divide by prime numbers so far [2,3,5,7,...] but only up to 7
# sqrt(53) = 7.28 ==> no need to go beyond 7 to know it's a prime
# add to list

