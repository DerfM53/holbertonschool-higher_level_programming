#!/usr/bin/python3

from calculator_1 import add, sub, mul, div

a = 10
b = 5
sum = add(a, b)
print("{} + {} = {}".format(a, b, sum))
sum = sub(a, b)
print("{} + {} = {}".format(a, b, sum))
sum = mul(a, b)
print("{} + {} = {}".format(a, b, sum))
sum = div(a, b)
print("{} + {} = {}".format(a, b, sum))

if __name__ == "__main__":
    pass
