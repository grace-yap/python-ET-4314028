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


### [("A", 1), ("B", 80), ("C", 10)]
### becomes A|1~B|80~C|10
# ), (" ==> 5 characters for what's just essentially a delimiter between a number and the next character
# use | and ~ as delimiters to shrink the JSON blob

# The filename that will be passed to this function
# is 10_04_challenge_art.txt
def encodeFile(filename, newFilename):
    with open(filename) as f:
        data = encodeString(f.read())

    data = [f'{char}|{count}' for char, count in data]

    with open(newFilename, 'w') as f:
        f.write('~'.join(data))


def decodeFile(filename):
    with open(filename) as f:
        data = f.read()
        
    pairs = data.split('~')
    pairs = [p.split('|') for p in pairs]
    pairs = [(p[0], int(p[1])) for p in pairs]
    return decodeString(pairs)



original_filesize = os.path.getsize("10_04_challenge_art.txt")
print(f'Original file size: {original_filesize}')
encodeFile('10_04_challenge_art.txt', '10_04_challenge_art_encoded_bigger_compression.txt')


new_filesize = os.path.getsize("10_04_challenge_art_encoded_bigger_compression.txt")
print(f'New file size: {new_filesize}')
decoded = decodeFile('10_04_challenge_art_encoded_bigger_compression.txt')
print(decoded)