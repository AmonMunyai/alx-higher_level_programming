#!/usr/bin/python3
for i in range(0, 9):
    for j in range(1, 9):
        if not (i >= j):
            print("{0:d}{1:d}".format(i, j), end=", ")
print(89)
