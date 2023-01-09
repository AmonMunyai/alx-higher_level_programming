#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    list_cpy = []
    for num in my_list:  # copy list
        list_cpy.append(num)
    if 0 <= idx < len(list_cpy):
        list_cpy[idx] = element  # replace element
    return list_cpy
