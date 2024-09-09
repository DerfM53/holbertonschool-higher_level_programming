#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    i = 0
    new_list = []
    while i < len(my_list):
        new_list.append(my_list[i])
        i += 1
    if idx < 0:
        return None
    elif idx > len(new_list):
        return None
    else:
        new_list[idx] = element
        return new_list
