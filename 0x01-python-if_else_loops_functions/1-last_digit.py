#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

# Get the last digit of the number
last_digit = abs(number) % 10

# Determine the appropriate message based on the last digit
message = "and is greater than 5" if last_digit > 5 \
          else "and is 0" if last_digit == 0 \
          else "and is less than 6 and not 0"

# Print the complete message
print("Last digit of", number, "is", last_digit, message)
