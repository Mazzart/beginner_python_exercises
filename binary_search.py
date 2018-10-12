import random

while True:
    try:
        n = int(input('Enter the length of the list (positive integer): '))
        rand_list = random.sample(range(n*10), n)
        break
    except ValueError:
        print('Please, try again...')

def binary_search(list: list, value: int) -> int:
    '''Search algorithm that finds the positions of a target value'''
    list.sort() # binary search works for sorted list
    low = 0
    high = list.index(list[-1])
    while low <= high:
        mid = (low + high) // 2
        if list[mid] > value:
            high = mid -1
        else:
            if list[mid] < value:
                low = mid + 1
            else:
                return mid
    return -1
