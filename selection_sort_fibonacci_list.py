import random

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

while True:
    try:
        n = int(input('Enter the length of the list (positive integer): '))
        tmp = fibonacci(n*5)
        rand_list = [random.choice(tmp) for _ in range(n)]
        break
    except ValueError:
        print('Please, try again...')

for i in range(n):
    index = i
    for k in range(i+1, n):
        if rand_list[index] > rand_list[k]:
            index = k
    rand_list[index], rand_list[i] = (
        rand_list[i], rand_list[index]
    )

print(rand_list)
