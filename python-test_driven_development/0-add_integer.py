#!/usr/bin/python3
def add_integer(a, b=98):
    sum = 0
    try:
        sum = int(a) + int(b)
    except (TypeError, ValueError):
        if isinstance(a, int):
            raise TypeError("b must be an integer")
        elif isinstance(b, int):
            raise TypeError("a must be an integer")
    else:
        return sum
