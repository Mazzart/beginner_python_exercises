import random
import time
from collections import deque

# Task 1
checker_1 = True


def fibonacci(num: int):
    i = 1
    if num == 0:
        fibonacci_numbers = []
    elif num == 1:
        fibonacci_numbers = [1]
    elif num == 2:
        fibonacci_numbers = [1, 1]
    elif num > 2:
        fibonacci_numbers = [1, 1]
        while fibonacci_numbers[-1] <= num:
            fibonacci_numbers.append(fibonacci_numbers[i] + fibonacci_numbers[i-1])
            i += 1
    return fibonacci_numbers[:-1]


while checker_1:
    try:
        num = int(input('Enter the length of the list (positive integer): '))
        tmp = fibonacci(num*5)
        rand_list = [random.choice(tmp) for _ in range(num)]
        checker_1 = False
    except ValueError:
        print('Please, try again...')

for i in range(1, len(rand_list)):
    k = rand_list[i]
    j = i - 1
    while j >= 0 and rand_list[j] > k:
        rand_list[j+1] = rand_list[j]
        j -= 1
    rand_list[j+1] = k

print("Task 1:", rand_list)

# Task 2 - Binary search
# https://github.com/Mazzart/beginner_python_exercises/blob/master/binary_search.py

# Task 3
# https://github.com/Mazzart/beginner_python_exercises/blob/master/greater_common_divisor.py

# Task 4
# https://github.com/Mazzart/beginner_python_exercises/blob/master/sort_freq_desc_order.py

# Task 5 - Inversion, a[i] > a[j] and i < j
checker_5 = True

while checker_5:
    try:
        n = int(input('Enter the length of the list (positive integer): '))
        rand_list_5 = random.sample(range(n * 10), n)
        checker_5 = False
    except ValueError:
        print('Please, try again...')

start_time = time.time()
count = 0

for i in range(len(rand_list_5)):
    for j in range(len(rand_list_5)):
        if rand_list_5[i] > rand_list_5[j] and i < j:
            count += 1

print(f"{time.time() - start_time} seconds")


def count_insertions(array: list) -> int:
    start_time_1 = time.time()
    new_count = 0

    if len(array) < 2:
        new_count = 0
    else:
        for i in range(len(array)):
            for j in range(i + 1, len(array)):
                if array[i] > array[j] and i < j:
                    new_count += 1

    print(f"{time.time() - start_time_1} seconds")
    return new_count


print(count, count_insertions(rand_list_5))

# Task 6 - BFS (breadth-first search) from book Грокаем Алгоритмы
graph = dict()
graph["you"] = ["alice", "bob", "claire"]
graph["bob"] = ["anna", "peggy"]
graph["alice"] = ["peggy"]
graph["claire"] = ["thom", "johny"]
graph["anna"] = []
graph["peggy"] = []
graph["thom"] = []
graph["johny"] = []


def search(name: str):
    search_queue = deque()
    search_queue += graph[name]
    searched = []

    while search_queue:  # while queue not empty
        print("What we already searched:", searched)
        person = search_queue.popleft()  # take first person
        if person not in searched:
            if person_is_seller(person):
                print(person + " is a mango seller!")
                return True
            else:
                search_queue += graph[person]  # add all friends of the person to the queue
                searched.append(person)
    return False


def person_is_seller(name):
    answer = input(f"{name}, are you a mango seller? (yes or no) ")
    return answer == 'yes'


search("you")
