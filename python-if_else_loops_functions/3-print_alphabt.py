#!/usr/bin/python3
ascii = 97
while ascii != 123:
    if ascii == 101 or ascii == 113:
        pass
    else:
        print("{}".format(chr(ascii)), end="")
    ascii += 1
