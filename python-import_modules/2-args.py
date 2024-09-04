#!/usr/bin/python3

from sys import argv

print("{} arguments.".format(len(argv)-1))

for i in range(1, len(argv)):
    print("{}: {}".format(i, argv[i]))
