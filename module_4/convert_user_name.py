"""Програми, які перетворюють ім'я користувача у:
- послідовність байтів
- unicode code points
- бінарне представлення
"""
# ---------------------------------------------------------------------
# Sequence of bytes
# The rules for translating a Unicode string into a sequence of bytes
# are called an encoding.
# ---------------------------------------------------------------------
USER_NAME = input("Please, enter your name: ")
# UTF-8 uses the following rules:
# 1) If the code point is < 128, it’s represented by the corresponding
# byte value.
# 2) If the code point is >= 128, it’s turned into a sequence of two,
# three, or four bytes, where each byte of the sequence is between 128
# and 255.
USER_NAME_BYTES = USER_NAME.encode('utf-8')

print(f"Hello, {USER_NAME}. "
      f"\nYour name as sequence of bytes will be: {USER_NAME_BYTES}\n"
      f"Type: {type(USER_NAME_BYTES)}")
# ---------------------------------------------------------------------
# Unicode code points (UCP)
# Literal strings are unicode by default in Python 3
# ---------------------------------------------------------------------
USER_NAME = input("Please, enter your name: ")
USER_NAME_UCP = ""

for letter in USER_NAME:
    USER_NAME_UCP += "{:04x}".format(ord(letter))[1:]

print(f"Your name in binary representation will be: {USER_NAME_UCP}")
# ---------------------------------------------------------------------
# Binary representation
# ---------------------------------------------------------------------
USER_NAME = input("Please, enter your name: ")
USER_NAME_BINARY = ''.join(format(ord(letter), 'b') for letter in USER_NAME)

print(f"Your name in binary representation: {USER_NAME_BINARY}")
