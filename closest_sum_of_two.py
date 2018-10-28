import random

sum_of_two, closest_num = 0, 0
checker = True

while checker:
    try:
        list_length = int(input("Enter the length of the list: "))
        number = int(input("Enter your number: "))
        checker = False
    except ValueError:
        print("Enter positive integer.")

rand_list = random.sample(range(list_length * 10), list_length)
rand_list.sort()
i, j = 0, list_length-1

while i < j:
    sum_of_two = rand_list[i] + rand_list[j]
    if sum_of_two > number:
        j -= 1
    else:
        if sum_of_two > closest_num:
            closest_num = sum_of_two
            position_i = i
            position_j = j
        i += 1

# next 3 lines for cases when sum_of_two always greater then number
# then closest number will be sum of the first two elements of the list
if closest_num == 0:
    closest_num = rand_list[0] + rand_list[1]
    position_i, position_j = 0, 1

print(rand_list, closest_num, 'less:', position_i, 'greater:', position_j)
