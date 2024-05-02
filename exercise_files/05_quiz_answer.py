def allPrimesUpTo(num):
    primes = [2]
    for number in range (3,num):
        sqrtNum = number**0.5
        # value of number**0.5 is stored in sqrtNum because we'd be recalculating it everytime it goes through the loop below,
        # so it saves a bit of computing power if we just store the value in the variable
        for factor in primes:
            if number % factor == 0:
                # Not prime
                break
            if factor > sqrtNum:
                # It's prime!
                # if we've gone past the square root of the number and we haven't found any factors yet, then it's prime
                primes.append(number)
                break
    return primes

# ALWAYS be careful NOT to OVER-optimize your programs
# You can write a pile of unreadable garbage while chasing some slight efficiency that doesn't even matter
# Remember: That happy middle ground, that sweet spot is the most Pythonic way.