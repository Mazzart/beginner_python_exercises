"""Practice of regular expressions"""

import re

# --------------------------------------------------------------------
# Task 1 - Say hello to a user using the typed name
# --------------------------------------------------------------------
# Format for answer_1: my name is ... or ... is my name
# Your name should begin with a capital letter.
answer_1 = input('What is your name? ')
name = re.search(r'[A-Z]\w*', answer_1)
try:
    print(f'Hello {name.group()}.')
except AttributeError:
    print(f'Please, reply in the correct format.')
# --------------------------------------------------------------------
# Task 2 - Check email
# --------------------------------------------------------------------
# Format for the email address: simple@example.com
answer_2 = input('Enter your email address: ')
# regex expression based on valid email examples from wiki
if not re.match(r'(^[a-z0-9.+-]+@[a-z0-9-]+\.[a-z]+$)', answer_2):
    print('Please, check entered email.')
# --------------------------------------------------------------------
# Task 3 - Check phone number
# --------------------------------------------------------------------
# Format for the phone number: (xxx) xxx - xxxx
answer_3 = input('Enter your phone number: ')
phone_number_regex = re.compile(r'\(\d\d\d\)\s\d\d\d\s-\s\d\d\d\d')
phone_number = phone_number_regex.search(answer_3)
try:
    print(f'The phone number {phone_number.group()} '
          f'is in the correct format.')
except AttributeError:
    print('Please, enter your phone number in the correct format.')
# --------------------------------------------------------------------
# Task 4 - Find tag <title> in the file and print text inside
# --------------------------------------------------------------------
with open('test.html', 'r') as test:
    test_into_string = test.read()
    title_regex = r'<title>(.*?)</title>'
    print(re.findall(title_regex, test_into_string)[0])
