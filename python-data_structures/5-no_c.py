#!/usr/bin/python3
def no_c(my_string):
    i = 0
    new_string = []
    while i < len(my_string):
        if my_string[i] == "c" or my_string[i] == "C":
            i += 1
        else:
            new_string.append(my_string[i])
            i += 1
    my_string = "".join(new_string)
    return my_string
