import random

# Task 1 (2 versions)

rand_list_1 = [random.choice(range(5)) for i in range(10)]

# version_1
unique_values_1 = set(rand_list_1)
unique_values_list = list(unique_values_1)

# version_2
unique_values_2 = []
for item in rand_list_1:
    if item not in unique_values_2:
        unique_values_2.append(item)

# Task 2
searched_numbers = []
for i in range(1500, 3001):
    if i % 7 == 0 and i % 3 != 0:
        searched_numbers.append(i)

# Task 3
rand_list_N = random.sample(range(10), 5)
rand_list_M = random.sample(range(15), 10)
common_N_M = [i for i in rand_list_N if i in rand_list_M]

# Task 4 - Insertion sort
array_4 = random.sample(range(100), 10)
print(f"Input list: {array_4}")

for i in range(1, len(array_4)):
    k = array_4[i]
    j = i - 1
    while j >= 0 and array_4[j] > k:
        array_4[j+1] = array_4[j]
        j -= 1
    array_4[j+1] = k

print(f"Output list: {array_4}")

# Task 5 - Insertion sort reversed
array_5 = random.sample(range(100), 10)
print(f"Input list: {array_5}")

for i in range(1, len(array_5)):
    k = array_5[i]
    j = i - 1
    while j >= 0 and array_5[j] < k:
        array_5[j+1] = array_5[j]
        j -= 1
    array_5[j+1] = k

print(f"Output list: {array_5}")

# Task 6
# https://github.com/Mazzart/beginner_python_exercises/blob/master/another_sort_even_odd.py
