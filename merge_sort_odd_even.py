import random

n = 10
rand_list = random.sample(range(n*10), n)


def merge_sort(left: list, right: list) -> list:
    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    while i < len(left):
        result.append(left[i])
        i += 1
    while j < len(right):
        result.append(right[j])
        j += 1
    return result


def merge_sort_recur(L: list) -> list:
    if len(L) < 2:
        return L[:]
    else:
        middle = len(L) // 2
        L_odd = [i for i in L if i % 2 == 1]
        L_even = [i for i in L if i % 2 == 0]
        left_odd = merge_sort_recur(L_odd[:middle])
        right_odd = merge_sort_recur(L_odd[middle:])
        left_even = merge_sort_recur(L_even[:middle])
        right_even = merge_sort_recur(L_even[middle:])
        return merge_sort(left_odd, right_odd) + merge_sort(left_even, right_even)

print(merge_sort_recur(rand_list))
