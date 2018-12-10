"""Practice of regular expressions

Write the program to check the password security.
1) should contain [a-z], [A-Z], [0-9] - one from each group
2) should contain [*#+@]
3) length from 4 to 6 symbols (without spaces)
"""

import re

passwords = []
verified_passwords = []

while True:
    password = input('To exit the program enter - stop\n'
                     'Enter your password: ')
    if password == 'stop':
        break
    else:
        passwords.append(password)

password_regex = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[*#+@])[a-zA-Z\d*#+@]{4,6}$'
prog = re.compile(password_regex)
for password in passwords:
    if prog.match(password):
        verified_passwords.append(password)

if not verified_passwords:
    print('You need to thinks about safer passwords.')
elif len(verified_passwords) == 1:
    print(f'The following password is secure: {verified_passwords[0]}')
else:
    print(f'The following passwords are secure:')
    for password in verified_passwords:
        print(password)
