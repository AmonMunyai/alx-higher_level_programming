#!/usr/bin/python3

def best_score(a_dictionary):
    if a_dictionary:
        keys = list(a_dictionary.keys())
        v = a_dictionary[keys[0]]
        for key in keys:
            if a_dictionary[key] > v:
                k, v = key, a_dictionary[key]
        return k
    return None
