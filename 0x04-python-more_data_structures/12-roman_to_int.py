#!/usr/bin/python3

def roman_to_int(roman_string):
    if (roman_string is None or
            type(roman_string) is not str or
            len(roman_string)) == 0:
        return 0

    num = 0
    dic = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    for i, j in zip(roman_string, roman_string[1:]):
        if i not in list(dic.keys()):
            return 0
        elif dic[i] >= dic[j]:
            num += dic[i]
        else:
            num -= dic[i]
    num += dic[roman_string[-1]]
    return num
