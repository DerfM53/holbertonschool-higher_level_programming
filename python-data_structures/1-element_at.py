#!/usr/bin/python3
def element_at(my_list, idx):
    i = 0
    if idx < 0:
        return None
    elif idx > len(my_list):
        return None
    else:
        while i < my_list[idx]:
            i += 1
        return i
