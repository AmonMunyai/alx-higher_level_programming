#!/usr/bin/python3

def roman_to_int(roman_string):
    if roman_string:
        num = 0
        roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        # IX
        for c in roman_string:
            for r in list(roman.keys()):
                if c == r:
                    num += roman[r]
        return num
    else:
        return 0
