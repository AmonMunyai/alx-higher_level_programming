#!/usr/bin/python3

def multiple_returns(sentence):
    strlen = len(sentence)
    return (strlen, sentence[0] if strlen > 0 else None)