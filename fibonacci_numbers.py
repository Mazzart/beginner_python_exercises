import time

while True:
    try:
        n = int(input("Please, enter positive integer number: "))
        break
    except ValueError:
        print("Please, try again...")


# Solution #1
def fibonacci(n):
    i = 1
    if n == 0:
        fibonacci_list = []
    elif n == 1:
        fibonacci_list = [1]
    elif n == 2:
        fibonacci_list = [1,1]
    elif n > 2:
        fibonacci_list = [1,1]
        while fibonacci_list[-1] <= n:
            fibonacci_list.append(fibonacci_list[i] + fibonacci_list[i-1])
            i += 1
    return fibonacci_list[:-1]


print("First solution:", fibonacci(n))


# Solution #2
def fib(n, d):
    if n in d:
        return d[n]
    else:
        ans = fib(n-1, d) + fib(n-2, d)
        d[n] = ans
        return ans


d = {1:1, 2:2}
fib_list = [1]
for item in range(1, n):
    if fib_list[-1] <= n:
        fib_list.append(fib(item, d))

print("Second solution:", fib_list[:-1])
