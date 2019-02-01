"""Generators"""

import math


# Task 1
def counting(end, increment):
    current = 0
    print("We are starting now ...")

    while current < end:
        yield current
        current += increment

    print("The end")


# Task 2
def prime_number(n):
    if n == 1:
        return False

    divisor = math.floor(math.sqrt(n))
    for d in range(2, divisor+1):
        if n % d == 0:
            return False
    return True


user_input = int(input('Enter integer number: '))
res = (i for i in range(1, user_input) if prime_number(i))
