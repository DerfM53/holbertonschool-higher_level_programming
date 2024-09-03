#!/usr/bin/python3
for i in range(100):
    if i <= 9:
        print(f"0{i}", end=", ")
    else:
        print(f"{i}", end=", " if i < 99 else "\n")
