def encodeString(stringVal):
    encodedList = []
    prevChar = stringVal[0]
    count = 0
    for char in stringVal:
        if prevChar != char:
            # if there is a change, add the previous character and its count to the list and reset the count
            encodedList.append((prevChar, count))
            count = 0
        prevChar = char
        count = count + 1
    
    # outside of the loop, we've reached the end of the string, so we need to make sure to record the last few characters
    encodedList.append((prevChar, count))
    return encodedList

def decodeString(encodedList):
    decodedStr = ''
    # go through each item in the list
    for item in encodedList:
        # take that item (item[0]) and multiply it by the count (item[1])
        # and then add it to the string
        decodedStr = decodedStr + item[0] * item[1]
    return decodedStr