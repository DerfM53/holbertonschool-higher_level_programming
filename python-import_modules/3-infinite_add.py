#!/usr/bin/python3

from sys import argv
from calculator_1 import add

if len(argv) == 1:
    print("{}".format(len(argv)-1))
else:
    result = 0
    for i in range(1, len(argv)):
        result = add(result, int(argv[i]))
    print("{}".format(result))
