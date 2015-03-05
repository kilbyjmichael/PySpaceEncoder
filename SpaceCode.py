#!/usr/bin/python
# Space Code Encoder/Decoder

import random
from itertools import cycle

# World Vars
codeString = list("Hello World")
spaceArray = (2,5,7,2,6) # default spaces (DONT USE!)
alphabet = list("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")

# Define Function to add letters to the head letter in a loop
def encodeString(string, key):
    extraLetters = list("")
    editedString = list("")
    #for letter in string:
    for letter, number in zip(string, cycle(key)):
        for x in range(number):
            extraLetters += random.choice(alphabet)
        editedString.extend(letter)
        #if letter is "!" or letter is "." or letter is ",":
            #extraLetters = ""
        editedString.extend(extraLetters)
        extraLetters = ""
    return editedString
    
# Define Function to Decode String
def decodeString(dstring, key):
    #decodedString.extend(string[0]) #take the first letter of the string
    dstring = list(dstring)
    chosenString = decodedString = ""
    for letter, number in zip(dstring, cycle(key)):
        for x in range(number + 1):
            chosenString += dstring.pop(0)
            list(chosenString)
        decodedString += chosenString[0]
        chosenString = ""
    return decodedString

# Define Function to save a file
def saveFile(fileName, writeString):
    saveFile = open(fileName, "w")
    saveFile.write("".join(writeString))
        # ''.join(writeString))
    saveFile.close()
    return

# Define Function to open a file
def openFile(fileName):
    readFile = open(fileName, "r")
    codeString = readFile.read()
    return codeString

def main():
    #Check Encode/Decode
    codeDirection = input("Encode (e) or Decode (d)? ")

    #Use if to decide what we are doing
    if codeDirection == 'e' or codeDirection == 'E':
        print("You are Encoding a file.")
        fileName = input("What would you like to name your file? :")
        #saveFile(fileName, "")
        #spaceArray = input("What is your key? (2,7,3) :")
        arr = input("What is your key? (2,7,3) :").split(',')
        spaceArray = [int(num) for num in arr]
        #print(spaceArray)
        codeString = input("What is your message? :")
        print("".join(encodeString(codeString, spaceArray)))
        saveFile(fileName, encodeString(codeString, spaceArray))

    elif codeDirection == 'd' or codeDirection == 'D':
        print("You are Decoding a file.")
        fileName = input("What file would you like to read? :")
        arr = input("What is your key? (2,7,3) :").split(',')
        spaceArray = [int(num) for num in arr]
        #print(openFile(fileName)) #reads the file into codeString
        print("".join(decodeString(openFile(fileName), spaceArray)))

#Run this shit
if __name__ == "__main__": main()
