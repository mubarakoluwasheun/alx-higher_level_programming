#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

# Extract the last digit of the number
last_digit = abs(number) % 10


if last_digit > 5:
	comparison = "is greater than 5"
elif last_digit == 0:
	comparison = "is 0"
else:
	comparison = "is less than 6 and not 0"

# print the result
print(f"Last digit of {number} is {last_digit} and {comparison}")
