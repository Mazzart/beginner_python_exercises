def quick_sort(list_num: list) -> list:
    '''Return a sorted list in ascending order'''
    if len(list_num) < 2:
        return list_num
    else:
        pivot = list_num[0]
        less_part = [i for i in list_num[1:] if i <= pivot]
        greater_part = [i for i in list_num[1:] if i > pivot]
        return quick_sort(less_part) + [pivot] + quick_sort(greater_part)
