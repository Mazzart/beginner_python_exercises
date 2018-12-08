"""Practice of regular expressions"""

import re

# --------------------------------------------------------------------
# Task 1 - Say hello to a user using the typed name
# --------------------------------------------------------------------
# Format for answer_1: my name is ... or ... is my name
#answer_1 = input('What is your name? ')
# name =
#print(f'Hello {name}.')
# --------------------------------------------------------------------
# Task 2 - Check email
# --------------------------------------------------------------------
#answer_2 = input('Enter your email address: ')
# --------------------------------------------------------------------
# Task 3 - Check phone number
# --------------------------------------------------------------------
# Format for the phone number: (xxx) xxx - xxxx
answer_3 = input('Enter your phone number: ')
phone_number_regex = re.compile(r'\(\d\d\d\)\s\d\d\d\s-\s\d\d\d\d')
try:
    phone_number = phone_number_regex.search(answer_3)
    print(f'The phone number {phone_number.group()} '
          f'is in the correct format.')
except AttributeError:
    print('Please, enter your phone number in the correct format.')
# --------------------------------------------------------------------
# Task 4 - Find tag <title> in the file and print text inside
# --------------------------------------------------------------------
