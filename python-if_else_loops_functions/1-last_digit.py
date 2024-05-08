#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

def get_last_digit (num):
    return abs(num)%10

last_digit = get_last_digit(number)

if last_digit >5:
    print(f"the last digit {number} is {last_digit} and is greater than 5")

elif last_digit == 0:
    print(f"the last digit of {number} is {last_digit} and is 0")

else:
    print(f"the last digit of{number} is {last_digit} and is less than 6 and not 0")
