hexNumbers = {
    '0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
    'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15
}

# Converts a string hexadecimal number into an integer decimal
# If hexNum is not a valid hexadecimal number, returns None
def hexToDec(hexNum):
    ############### FOR NON-VALID HEX INPUT!!!!!!!!!!!!!1
    # if isinstance(num, int) and (num >= 0):
    # for counter in range(0,num):
    #     output = output * (counter + 1)
    # return output
    if not isinstance(hexNum, str):
        return None

    hexLength = len(hexNum)
    powIndex = len(hexNum)

    for counter in range(0,hexLength):
        if hexNum[counter:counter+1] not in hexNumbers:
            return None

    # print('hexLength = ', hexLength)
    index = 0
    decNum = 0
    # print('hexNum = ', hexNum)
    while index < hexLength:
        # print('convert hex to dec: ', hexNumbers[hexNum[index:index+1]])
        decNum = decNum + (int(hexNumbers[hexNum[index:index+1]]) * (16**(powIndex-1)))
        # print('decNum = ', decNum)
        # print('index = ', index)
        # print('powIndex = ', powIndex)
        index = index + 1
        powIndex = powIndex - 1
    return decNum

print('hex value of E7A9 is', hexToDec('E7A9'))
print('hex value of spam spam spam is', hexToDec('spam spam spam'))
print('hex value of integer 12345 is', hexToDec(12345))

#         E 7 A 9
# index   0 1 2 3
# 16^x    3 2 1 0

# E * (16**3)
