#!/usr/bin/python3
for num1 in range(9):
    for num2 in range(num1 + 1, 10):
        print(f"{num1}{num2}", end=", " if num1 != 8 or num2 != 9 else "")
print()
