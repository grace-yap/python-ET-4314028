### INCOMPLETE ANSWER!!!
### DIDN'T SOLVE decodeFile PART!!!

import json 
import os

def encodeString(stringVal):
    encodedList = []
    prevChar = None
    count = 0
    for char in stringVal:
        if prevChar != char and prevChar is not None:
            encodedList.append((prevChar, count))
            count = 0
        prevChar = char
        count = count + 1
    encodedList.append((prevChar, count))
    return encodedList

def decodeString(encodedList):
    # print('encodeList = ', encodedList)
    decodedStr = ''
    for item in encodedList:
        # print('item = ', item)
        decodedStr = decodedStr + item[0] * item[1]
        # print('decodeStr = ', decodedStr)
    return decodedStr

# The filename that will be passed to this function
# is 10_04_challenge_art.txt
def encodeFile(filename, newFilename):
    encodeList = []
    tempString = ''
    with open(filename, 'r') as f:
        for line in f.readlines():
            encodeList.append(encodeString(line))
    for item in encodeList:
        tempString = tempString + str(item)
        tempString = tempString.replace('), (', '),(').replace('][', ',')
    # print('tempString = ', tempString)
    with open(newFilename, 'w') as g:
        g.write(tempString)


def decodeFile(filename):
    decodeList = []
    tempString = ''
    with open(filename, 'r') as h:
        # print(h.readline())
        # tempString = str(h.readline())
        # print('tempString = ', tempString)
        # decodeList.append(h.readline())
            # decodeList = list(h.readline().replace('[','').replace(']','').split(','))
            # print('decodeList = ', decodeList)
            # decodeString(decodeList)
        return(h.readline())
    # return decodeList






# print(encodeFile('10_04_challenge_art.txt', '10_04_challenge_art_encoded.txt'))

print('PART 1')
original_filesize = os.path.getsize("10_04_challenge_art.txt")
print(f'Original file size: {original_filesize}')
encodeFile('10_04_challenge_art.txt', '10_04_challenge_art_encoded.txt')

print('PART 2')
# decodeFile('10_04_challenge_art_encoded.txt')

new_filesize = os.path.getsize("10_04_challenge_art_encoded.txt")
print(f'New file size: {new_filesize}')
decoded = decodeFile('10_04_challenge_art_encoded.txt')
print(decoded)