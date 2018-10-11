import random

while True:
    try:
        n = int(input('Enter the length of the list (positive integer): '))
        list_1 = random.sample(range(n*10), n)
        list_2 = random.sample(range(n*10), n)
        break
    except ValueError:
        print('Please, try again...')

# Solution 1
counter = 0
while counter < n:
    max_num = max(list_1[counter:])
    max_index = list_1.index(max_num)
    list_1[counter],list_1[max_index] = list_1[max_index],list_1[counter]
    counter += 1

print(list_1)

# Solution 2
for i in range(n):
    index = i
    for k in range(i+1, n):
        if list_2[index] < list_2[k]:
            index = k
    list_2[index], list_2[i] = (
        list_2[i], list_2[index]
    )

print(list_2)
