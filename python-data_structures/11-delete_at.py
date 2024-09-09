#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    i = 0
    if idx < 0 or idx > len(my_list) - 1:
        return my_list
    while i < len(my_list):
        if i == idx:
            del my_list[i]
            i += 1
        else:
            i += 1
    return my_list
