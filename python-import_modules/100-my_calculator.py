#!/usr/bin/python3

import calculator_1
import sys

if __name__ == "__main__":

    if len(sys.argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    else:
        a = int(sys.argv[1])
        b = int(sys.argv[3])
        if sys.argv[2] == "+":
            print("{} + {} = {}".format(a, b, calculator_1.add(a, b)))
        elif sys.argv[2] == "-":
            print("{} - {} = {}".format(a, b, calculator_1.sub(a, b)))
        elif sys.argv[2] == "*":
            print("{} * {} = {}".format(a, b, calculator_1.mul(a, b)))
        elif sys.argv[2] == "/":
            print("{} / {} = {}".format(a, b, calculator_1.div(a, b)))
        else:
            print("Unknown operator. Available operators: +, -, * and /")
            exit(1)
