import random
from collections import Counter

# ---------------------------------------------------------------------
# Task 1 - Check recursively is the list sorted
# ---------------------------------------------------------------------
test_0 = [0]
test_1 = [1, 2, 3, 3, 4, 5]
test_2 = [2, 4, 6, 6, 8, 7]
test_3 = [5, 4, 3, 3, 2, 1]
test_4 = [8, 6, 4, 4, 2, 3]


def is_sorted_growing(lst: list) -> bool:
    """Return True or False depending on whether the list is sorted or not (growing order)"""

    if len(lst) < 2:  # if the length of the list is less than 2
        return True  # return True - list is sorted
    else:
        if lst[0] <= lst[1]:  # if 1st element of the list is less than 2nd then
            return is_sorted_growing(lst[1:])  # call is_sorted function on list which is reduced by one
        else:
            # if 1st element of the list is greater than 2nd, return False - list is not sorted in growing order
            return False


def is_sorted_descending(lst: list) -> bool:
    """Return True or False depending on whether the list is sorted or not (descending order)"""

    if len(lst) < 2:  # if the length of the list is less than 2
        return True  # return True - list is sorted
    else:
        if lst[0] >= lst[1]:  # if 1st element of the list is greater than 2nd then
            return is_sorted_descending(lst[1:])  # call is_sorted function on list which is reduced by one
        else:
            # if 1st element of the list is less than 2nd, return False - list is not sorted in descending order
            return False


print("Task 1 answers:")
print(is_sorted_growing(test_0), is_sorted_descending(test_0))
print(is_sorted_growing(test_1), is_sorted_growing(test_2))
print(is_sorted_descending(test_3), is_sorted_descending(test_4))
# ---------------------------------------------------------------------
# Task 2 - Calculate words in the string
# ---------------------------------------------------------------------
text = "Hello, my name is Taras. yes, yes, Taras. Taras has 5 letters!"
print("\nTask 2 answer:\nInitial text: ", text)

char_to_delete = ",.!?/:;"  # string with the characters we want to remove from the input text
for item in text:  # iteration through the characters of the text
    if item in char_to_delete:  # if the character is in the char_to_delete
        text = text.replace(item, "")  # replace the character with an empty string

text_items = text.split(" ")  # split items in the text and create the list with them
count_items = Counter(text_items)  # count items in text_items

# create a new list where each item is a tuple of two elements
# 1st element of the tuple is an item from text_items, 2nd - counts of each item in text_items
# tuples in the new list sorted by the first elements of each tuple
sorted_by_key = sorted(count_items.items(), key=lambda kv: kv[0])

result = []
for item in sorted_by_key:  # iteration through the items in sorted_by_key
    # add to the result list 1st element of each item + ':' + 2nd element converted to string
    result.append(item[0] + ':' + str(item[1]))

print("Output:", result)
# ---------------------------------------------------------------------
# Task 3 - Quick sort growing order
# ---------------------------------------------------------------------
L_3 = random.sample(range(1, 100), 10)  # create list with 10 items in the range from 1 to 100 using random module
print("\nTask 3 answer:\nInput list L_3:", L_3)


def quick_sort_growing(list_num: list) -> list:
    """Return the sorted list in growing order"""

    if len(list_num) < 2:  # if length of the list is less than 2
        return list_num  # return input list
    else:
        pivot = list_num[0]  # write the first element of the input list to the variable
        less_part = [i for i in list_num[1:] if i < pivot]  # create list where all numbers is less than pivot
        greater_part = [i for i in list_num[1:] if i > pivot]  # create list where all numbers is greater than pivot
        # recursive call of the function with less part (greater part) until base case
        return quick_sort_growing(less_part) + [pivot] + quick_sort_growing(greater_part)


print("Output list L_3:", quick_sort_growing(L_3))
# ---------------------------------------------------------------------
# Task 4 - Quick sort decrease order
# ---------------------------------------------------------------------
L_4 = random.sample(range(1, 100), 10)  # create list with 10 items in the range from 1 to 100 using random module
print("\nTask 4 answer:\nInput list L_4:", L_4)


def quick_sort_descending(list_num: list) -> list:
    """Return the sorted list in descending order"""

    if len(list_num) < 2:  # if the length of the list is less than 2
        return list_num  # return input list
    else:
        pivot = list_num[0]  # write the first element of the input list to the variable
        greater_part = [i for i in list_num[1:] if i > pivot]  # create list where all numbers is greater than pivot
        less_part = [i for i in list_num[1:] if i < pivot]  # create list where all numbers is less than pivot
        # recursive call of the function with greater part (less part) until base case
        return quick_sort_descending(greater_part) + [pivot] + quick_sort_descending(less_part)


print("Output list L_4:", quick_sort_descending(L_4))
