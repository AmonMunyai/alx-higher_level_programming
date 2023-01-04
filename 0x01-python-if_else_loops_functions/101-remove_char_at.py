#!/usr/bin/python3
def remove_char_at(str, n):
    i = 0
    string = ""

    while (i < len(str)):
        if (i != n):
            string += str[i]
        i = i + 1

    return (string)
