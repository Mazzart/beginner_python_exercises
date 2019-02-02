"""Iterators"""

import math

# Task 1
class RandomNumber:
    """Generate sequence of numbers"""

    def __init__(self, increment=0, end=0):
        self.start = 0
        self.increment = increment
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        if self.start <= self.end:
            result = self.start
            self.start += self.increment
            return result
        else:
            raise StopIteration


result_1 = RandomNumber(20, 100)


# Task 2
class PrimeNumber:
    """Generate prime numbers"""

    def __init__(self, user_input):
        self.start = 2
        self.user_input = user_input

    def __iter__(self):
        return self

    def is_prime(self, number):       
        divisor = math.floor(math.sqrt(number))
        for d in range(2, divisor+1):
            if number % d == 0:
                return False
        return True

    def __next__(self):
        number = self.start
        while not self.is_prime(number):
            number += 1
        if number > self.user_input:
            raise StopIteration
            
        self.start = number + 1
        return number


result_2 = PrimeNumber(100)
        
