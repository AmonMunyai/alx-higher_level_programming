#!/usr/bin/python3
def print_last_digit(number):
    digit = (number % 10) if (number > 0) else (-number % 10)
    print(digit, end="")  # print last digit
    return (digit)
