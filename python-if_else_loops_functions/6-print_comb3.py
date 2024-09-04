#!/usr/bin/python3
for num1 in range(9):
    for num2 in range(num1 + 1, 10):
        end_char = ", " if num1 != 8 or num2 != 9 else ""
        print("{}{}".format(num1, num2), end=end_char)
print()
