#!/usr/bin/python3
for c in range(0, -26, -1):
    print(f"{chr(122 + c) if (-c % 2) == 0 else chr(c - 32 + 122)}", end="")
