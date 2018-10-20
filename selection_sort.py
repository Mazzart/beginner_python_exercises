import random

while True:
    try:
        n = int(input('Enter the length of the list (positive integer): '))
        list_1 = random.sample(range(n*10), n)
        list_2 = random.sample(range(n*10), n)
        list_3 = random.sample(range(n*10), n)
        break
    except ValueError:
        print('Please, try again...')

# Solution 1
counter = 0
while counter < n:
    min_num = min(list_1[counter:])
    min_index = list_1.index(min_num)
    list_1[counter],list_1[min_index] = list_1[min_index],list_1[counter]
    counter += 1
    
print(list_1)

# Solution 2
for i in range(n):
    index = i
    for k in range(i+1, n):
        if list_2[index] > list_2[k]:
            index = k
    list_2[index], list_2[i] = (
        list_2[i], list_2[index]
    )

print(list_2)

# Solution 3
index = 0
while index != len(list_3):
    for i in range(index, len(list_3)):
        if list_3[i] < list_3[index]:
            list_3[index], list_3[i] = list_3[i], list_3[index]
    index += 1

print(list_3)
