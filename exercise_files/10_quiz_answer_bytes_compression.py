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
    decodedStr = ''
    for item in encodedList:
        decodedStr = decodedStr + item[0] * item[1]
    return decodedStr


# you can store any integer up to 255 in a single byte of data
# so rather than storing the number '255' as a string with 3 characters, which takes up 3 bytes, you can use 1 single byte
# -- you store it as an integer, rather than a string
# each of these characters in the ASCII art also one byte or one character.
# so if we make sure that we write our file precisely (i.e., one character, one number, one character, one number, ...),
#     and then we read it in precisely (i.e., the first byte's the character, the next byte's the number, and so on),
#     we can encode and decode this image extremely efficiently.
# there are no deilmiters. we're just depending on the pattern being exactly correct every single


# The filename that will be passed to this function
# is 10_04_challenge_art.txt
def encodeFile(filename, newFilename):
    with open(filename) as f:
        data = encodeString(f.read())
    output = bytearray()
    for item in data:
        ### Character byte
        output.extend(bytes(item[0], 'utf-8'))
        ### Integer count byte
        output.extend(item[1].to_bytes(1, 'big'))
    with open(newFilename, 'wb') as binary_file:
        ### Write bytes to file
        binary_file.write(output)


def decodeFile(filename):
    with open(filename, 'rb') as f:
        data = f.read()
        ### Split data into pairs
        bytePairs = [data[i:i+2] for i in range(0, len(data), 2)]
        encodedList = []
        for bytePair in bytePairs:
            encodedList.append((bytePair[:1].decode('utf-8'), int.from_bytes(bytePair[1:], 'big')))
    return decodeString(encodedList)



original_filesize = os.path.getsize("10_04_challenge_art.txt")
print(f'Original file size: {original_filesize}')
encodeFile('10_04_challenge_art.txt', '10_04_challenge_art_encoded_bytes_compression.txt')


new_filesize = os.path.getsize("10_04_challenge_art_encoded_bytes_compression.txt")
print(f'New file size: {new_filesize}')
decoded = decodeFile('10_04_challenge_art_encoded_bytes_compression.txt')
print(decoded)