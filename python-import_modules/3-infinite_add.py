#!/usr/bin/python3

from sys import argv

if len(argv) == 1:
    print("{}".format(len(argv)-1))
else:
    result = 0
    for i in range(1, len(argv)):
        result = result + int(argv[i])
    print("{}".format(result))
