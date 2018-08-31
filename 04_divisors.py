"""
Create a program that asks the user for a number and then prints out
a list of all the divisors of that number.
"""

x = int(input("Please enter a number: "))
divisors_list = []

for item in range(x):
    if x % (item + 1) == 0:
        divisors_list.append(item + 1)
print(divisors_list)


# Second option to solve this exercise

y = int(input("Please enter a number: "))
dividend = range(1, y+1)

result = [i for i in dividend if y % i == 0]
print(result)
