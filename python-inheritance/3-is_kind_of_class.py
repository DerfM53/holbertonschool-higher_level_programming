#!/usr/bin/python3

def is_kind_of_class(obj, a_class):
    """
    Return True if obj is an object of instance or instance
    of a class
    Else return False
    """
    if isinstance(obj, a_class):
        return True
    else:
        return False
