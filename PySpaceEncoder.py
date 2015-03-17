#!/usr/bin/python
"""
PySpaceEncoder
Takes a string and key from user and encodes the string
with the key by inserting semi-random letters into the spaces.
"""

import random
from itertools import cycle

# World Vars
code_string = list("Hello World")
space_array = (2,5,7,2,6) # default spaces (DONT USE!)
alphabet = list("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")

# Define Function to add letters to the head letter in a loop
def encode_string(string, key):
    extra_letters = list("")
    edited_string = list("")
    #for letter in string:
    for letter, number in zip(string, cycle(key)):
        for x in range(number):
            extra_letters += random.choice(alphabet)
        edited_string.extend(letter)
        #if letter is "!" or letter is "." or letter is ",":
            #extra_letters = ""
        edited_string.extend(extra_letters)
        extra_letters = ""
    return edited_string
    
# Define Function to Decode String
def decode_string(dstring, key):
    i = 0
    decoded_string = []
    for x in cycle(key):
        if i >= len(dstring):
            break
        else:
            decoded_string.extend(dstring[i])
            i += x + 1
    return decoded_string

# Define Function to save a file
def save_file(file_name, write_string):
    save_file = open(file_name, "w")
    save_file.write("".join(write_string))
        # ''.join(write_string))
    save_file.close()
    return

# Define Function to open a file
def open_file(file_name):
    read_file = open(file_name, "r")
    code_string = read_file.read()
    return code_string

def main():
    #Check Encode/Decode
    code_direction = input("Encode (e) or Decode (d)? ")

    #Use if to decide what we are doing
    if code_direction == 'e' or code_direction == 'E':
        print("You are Encoding a file.")
        file_name = input("What would you like to name your file? :")
        arr = input("What is your key? (2,7,3) :").split(',')
        space_array = [int(num) for num in arr]
        code_string = input("What is your message? :")
        print("".join(encode_string(code_string, space_array)))
        save_file(file_name, encode_string(code_string, space_array))

    elif code_direction == 'd' or code_direction == 'D':
        print("You are Decoding a file.")
        file_name = input("What file would you like to read? :")
        arr = input("What is your key? (2,7,3) :").split(',')
        space_array = [int(num) for num in arr]
        print("".join(decode_string(open_file(file_name), space_array)))

#Run this shit
if __name__ == "__main__": main()
