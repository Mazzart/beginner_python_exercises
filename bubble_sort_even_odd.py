import random

while True:
    try:
        n = int(input('Enter the length of the list (positive integer): '))
        items_list = random.sample(range(n*10), n)
        break
    except ValueError:
        print('Please, try again...')

even, odd = [], []

for item in items_list:
    if item % 2 == 0:
        even.append(item)
    else:
        odd.append(item)

def bubble_sort(items_list: list) -> list:
    for i in range(len(items_list)):
        swapped = False
        for j in range(len(items_list)-1):
            if items_list[j] > items_list[j+1]:
                items_list[j], items_list[j+1] = items_list[j+1], items_list[j]
                swapped = True
        if not swapped:
            break
    return items_list

bubble_sort(even)
bubble_sort(odd)
print(even + odd)
