#!/usr/bin/python3

def weight_average(my_list=[]):
    w, res = 0, 0

    for i, j in my_list:
        w += j
        res += i * j

    return (res / w)
