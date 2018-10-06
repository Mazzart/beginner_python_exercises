import math

while True:
    try:
        n = int(input("Please, enter positive integer number: "))
        break
    except ValueError:
        print("Please, try again...")


def prime_number(n):
    if n == 1:
        return False

    divisor = math.floor(math.sqrt(n))
    for d in range(2, divisor+1):
        if n % d == 0:
            return False
    return True

result = [i for i in range(1, n+1) if prime_number(i)]
print(result)

