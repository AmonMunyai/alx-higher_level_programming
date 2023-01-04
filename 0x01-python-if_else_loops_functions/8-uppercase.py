#!/usr/bin/python3
def uppercase(str):
    string = ""  # initialize empty string
    for char in str:
        if (97 <= ord(char) <= 122):
            string += chr(ord(char) - 32)  # lower to upper
        else:
            string += char
    print(string)  # print capitalized string
