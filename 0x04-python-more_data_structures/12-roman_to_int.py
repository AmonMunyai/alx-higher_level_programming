#!/usr/bin/python3

def roman_to_int(roman_string):
    if (not isinstance(roman_string, str) or roman_string is None):
        return (0)

    r_dictionary = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }

    num = 0

    for r_numeral in roman_string:
        if r_numeral not in r_dictionary.keys():
            return (0)

    for i, j in zip(roman_string, roman_string[1:]):
        if r_dictionary[i] >= r_dictionary[j]:
            num += r_dictionary[i]
        else:
            num -= r_dictionary[i]
    
    num += r_dictionary[roman_string[-1]]

    return (num)
