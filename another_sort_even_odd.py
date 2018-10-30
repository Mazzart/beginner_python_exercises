import random

checker = True

while checker:
    try:
        n = int(input('Enter the length of the list (positive integer): '))
        rand_list = random.sample(range(n*10), n)
        checker = False
    except ValueError:
        print('Please, try again...')

print(rand_list)


def even_odd_sort(array: list, array_len: int) -> list:
    left, right = 0, array_len - 1
    k = 0
    while left < right:
        while array[left] % 2 == 0:
            left += 1
            k += 1
        while array[right] % 2 != 0 and left < right:
            right -= 1
        if left < right:
            array[left], array[right] = array[right], array[left]

    even, odd = array[:k], array[k:]
    even.sort(), odd.sort()
    return even + odd


print(even_odd_sort(rand_list, len(rand_list)))
