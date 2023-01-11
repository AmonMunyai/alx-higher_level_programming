#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    outer = []

    for nums in matrix:
        inner = []
        for num in nums:
            inner.append(num * num)
        outer.append(inner)

    return (outer)
