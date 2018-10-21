import random

while True:
    try:
        n = int(input('Enter the length of the list (positive integer): '))
        rand_list = random.sample(range(n*10), n)
        break
    except ValueError:
        print('Please, try again...')

# Solution 1
def binary_search(list: list, value: int) -> int:
    '''Search algorithm that finds the positions of a target value'''
    list.sort() # binary search works for sorted list
    low = 0
    high = len(list) - 1
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

# Solution 2 (is number in list)
def bisect_search(L: list, e: int) -> bool:
    L.sort() # binary search works for sorted list
    def bisect_search_helper(L: list, e: int, low: int, high: int) -> bool:
        if high == low:
            return L[low] == e
        mid = (low + high) // 2
        if L[mid] == e:
            return True
        elif L[mid] > e:
            if low == mid: # nothing left to search
                return False
            else:
                return bisect_search_helper(L, e, low, mid-1)
        else:
            return bisect_search_helper(L, e, mid+1, high)
    if len(L) == 0:
        return False
    else:
        return bisect_search_helper(L, e, 0, len(L)-1)
