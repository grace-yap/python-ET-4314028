def encodeString(stringVal):
    encodedList = []
    index = 0
    charCount = 1 # start count at 1 to include the first char
    stringLen = len(stringVal)
    # print('stringLen = ', stringLen)
    while index < stringLen:
        # print('index = ', index)
        tupleChar = stringVal[index]
        # print('tupleChar = ', tupleChar)
        if (index != stringLen - 1) and (stringVal[index] == stringVal[index+1]): # first if condition is to avoid "string index out of range" error
            charCount = charCount + 1
            # print('charCount = ', charCount)
        else:
            tupleAppend = (tupleChar,charCount)
            # print('tupleAppend = ', tupleAppend)
            encodedList.append(tupleAppend)
            # print('encodeList = ', encodeList)
            charCount = 1
        index = index + 1
    return encodedList

def decodeString(encodedList):
    listLen = len(encodedList)
    # print('listLen = ', listLen)
    index = 0
    fullString = ''
    while index < listLen:
        letter, number = encodedList[index]
        # print('encodeList = ', encodedList[index])
        # print('letter = ', letter)
        # print('number = ', number)
        while number > 0:
            fullString = fullString + letter
            # print('fullString = ', fullString)
            number = number - 1
        index = index + 1
        # print('index = ', index)
    return fullString


print(encodeString('AAAAABBBBAAA'))
# [('A',5), ('B',4), ('A',3)]

print(encodeString('Bookkeeping'))
# [('B', 1), ('o', 2), ('k', 2), ('e', 2), ('p', 1), ('i', 1), ('n', 1), ('g', 1)]

testList = [('W',5),('1',2),('G',3)]
print(decodeString(testList))
# WWWWWW11GGG

### encodeString flow
# create empty list
# slice 1 char
# compare to next char
# count
# append to list

### test how to create a list of tuples (append tuple to empty list)
# testList = []
# testTuple = ('A',5)
# testList.append(testTuple)
# testTuple2 = ('B',4)
# testList.append(testTuple2)
# testChar = 'C'
# testNum = 3
# testTuple3 = (testChar,testNum)
# testList.append(testTuple3)
# print('testList = ',testList)
# print('first tuple = ',testList[0])
# letter, number = testList[0]
# print('letter = ', letter, 'number = ', number)

art = '''

                                                                                
                                                                                
                               %%%%%%%%%%%%%%%%%%%                              
                        %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%                       
                    %%%%%%%%                         %%%%%%%%                   
                %%%%%%%                                   %%%%%%                
              %%%%%%                                         %%%%%%             
           %%%%%%                                               %%%%%           
          %%%%%                                                   %%%%%         
        %%%%%                                                       %%%%%       
       %%%%                 %%%%%              %%%%%                  %%%%      
      %%%%                 %%%%%%%            %%%%%%%                  %%%%     
     %%%%                  %%%%%%%            %%%%%%%                   %%%%    
    %%%%                   %%%%%%%            %%%%%%%                    %%%%   
    %%%%                    %%%%%              %%%%%                     %%%%   
   %%%%                                                                   %%%%  
   %%%%                                                                   %%%%  
   %%%%                                                                   %%%%  
   %%%%                                                      %%%%        %%%%   
    %%%%       %%%%%%                                        %%%%%       %%%%   
    %%%%         %%%%                                       %%%%        %%%%    
     %%%%         %%%%                                     %%%%         %%%%    
      %%%%         %%%%%                                  %%%%         %%%%     
       %%%%%         %%%%%                             %%%%%         %%%%%      
        %%%%%          %%%%%%                        %%%%%          %%%%        
          %%%%%           %%%%%%%               %%%%%%%           %%%%%         
            %%%%%             %%%%%%%%%%%%%%%%%%%%%             %%%%%           
              %%%%%%%                                        %%%%%              
                 %%%%%%%                                 %%%%%%%                
                     %%%%%%%%%                     %%%%%%%%%                    
                          %%%%%%%%%%%%%%%%%%%%%%%%%%%%%                         
                                   %%%%%%%%%%%%                                 
                                                                                
                                                                                 

'''

print(encodeString(art))
smiley = encodeString(art)
print(decodeString(smiley))