#!/usr/bin/python3

def is_same_class(obj, a_class):
    """
    Return True if the type of obj is
    idently with a_class
    else return False
    """
    if type(obj) is a_class:
        return True
    else:
        return False
