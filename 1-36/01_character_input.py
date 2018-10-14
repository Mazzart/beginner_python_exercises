"""
Create a program that asks the user to enter their name and their age.
Print out a message addressed to them that tells them the year that
they will turn 100 years old.
"""

import datetime

name = input("Please enter your name: ")
age = int(input("Please enter your age: "))
birthday_yes_no = input("Did you have your birthday this year (yes/no)? ")
now = datetime.datetime.now()

if age >= 100:
    print(f"{name}, you are already 100 years old.")
else:
    if birthday_yes_no == "yes":
        year = (100 - age) + now.year
    else:
        year = (99 - age) + now.year
    print(f"{name}, you will be 100 years old in {year}")