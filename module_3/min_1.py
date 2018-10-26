import datetime


# Task 1
name_1 = input("Please enter your name: ")
print(f"Hello {name_1}.")


# Task 2
name_2 = input("Please enter your name: ")
now = datetime.datetime.now()
current_year = now.year
checker_2 = True

while checker_2: 
    try:
        age = int(input("Please enter your age: "))
        checker_2 = False
    except ValueError:
        print("Please enter an integer")
        
if age > 100:
    print("You are already 100 years old.")
elif age < 0:
    print("It is impossible.")
else:
    print(f"{name_2} you will be 100 years old in {100 - age} years.\n"
      f"It will be {current_year + 100 - age} year.")


# Task 3
checker_3 = True

while checker_3: 
    try:
        number_3 = int(input("Please enter a number: "))
        checker_3 = False
    except ValueError:
        print("Please enter an integer")

if number_3 % 2 == 0:
    print(f"{number_3} is even")
else:
    print(f"{number_3} is odd")


# Task 4
word_4 = input("Please enter a word: ")

if word_4.lower() == word_4.lower()[::-1]:
    print(f"{word_4} is a palindrom")
else:
    print(f"{word_4} is not a palindrom")
