import random
from collections import Counter


def sort_freq_desc_order(list: list) -> list:
    '''Sorts the list by the frequency of entry in a descending order'''
    c = Counter(list)
    result = []

    sorted_by_value = sorted(c.items(), key=lambda kv:kv[1], reverse=True)
    for item in sorted_by_value:
        result.extend([item[0] for i in range(item[1])])
    return result


if __name__ == '__main__':
    print(sort_freq_desc_order([4,3,7,4,3,4,2,7,5,4,5,7]))
    print(sort_freq_desc_order([random.randint(1,10) for i in range(20)]))
