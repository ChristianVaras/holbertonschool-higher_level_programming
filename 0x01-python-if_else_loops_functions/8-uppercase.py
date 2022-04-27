#!/usr/bin/python3
def uppercase(str):
    for c in str:
        num = ord(c)
        print(f"{chr(num - 32) if 97 <= num <= 122 else c}", end="")
    print("")
