#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    i = 0
    if idx < 0:
        return None
    elif idx > len(my_list):
        return None
    else:
        while i < my_list[idx - 1]:
            i += 1
        my_list[i] = element
        return my_list
