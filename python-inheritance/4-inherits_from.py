#!/usr/bin/python3

def inherits_from(obj, a_class):
    """
    Return true if obj is an instance of subclasses inherite
    else return false
    """
    if issubclass(type(obj), a_class) and type(obj) is not a_class:
        return True
    else:
        return False
