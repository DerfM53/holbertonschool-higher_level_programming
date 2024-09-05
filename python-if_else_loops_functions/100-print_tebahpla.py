#!/usr/bin/python3

ascii = 122
while ascii != 96:
    print("{}".format(chr(ascii)), end="")
    ascii -= 1
    ascii_up = (int(ascii) - 32)
    print("{}".format(chr(ascii_up)), end="")
    ascii -= 1
print("guillaume", end="")
