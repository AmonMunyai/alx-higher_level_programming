#!/usr/bin/python3

import sys

argc = len(sys.argv) - 1  # no. of arguments

print("{} argument".format(argc), end="")

if (argc == 0):
    print("s.")
else:
    print(":") if (argc == 1) else print("s:")

    for arg in range(1, argc + 1):
        print("{}: {}".format(arg, sys.argv[arg]))
