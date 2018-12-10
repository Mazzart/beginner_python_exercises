"""Practice of regular expressions

Write the program to check the password security.
1) should contain [a-z], [A-Z], [0-9] - one from each group
2) should contain [*#+@]
3) length from 4 to 6 symbols (without spaces)
"""

import re

passwords = []
while True:
    password = input('To exit the program enter - stop\n'
                     'Enter your password: ')
    if password == 'stop':
        break
    else:
        passwords.append(password)

