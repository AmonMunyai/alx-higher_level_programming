#!/usr/bin/python3

def weight_average(my_list=[]):
    if not isinstance(my_list, list) or len(my_list) == 0:
        return (0)

    w, res = 0, 0

    for i, j in my_list:
        w += j
        res += i * j

    return (res / w)
