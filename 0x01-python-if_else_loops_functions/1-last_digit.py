#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    remainder = number % (-10)
else:
    remainder = number % 10
msg = f"Last digit of {number} is {remainder}"

if remainder > 5:
    print(f"{msg} and is greater than 5")
elif remainder == 0:
    print(f"{msg} and is 0")
else:
    print(f"{msg} and is less than 6 and not 0")
