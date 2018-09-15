"""
Ask the user for a string and print out whether this string is a palindrome or not. 
(A palindrome is a string that reads the same forwards and backwards.)
"""

word = input("Please enter a word: ")

if word == word[::-1]:
    print("{} is a palindrome".format(word))
else:
    print("{} is not a palindrome".format(word))


# Solution with recursion
def is_palindrome(s):

    def to_chars(s):
        s = s.lower()
        ans = ''
        for char in s:
            if char in "abcdefghijklmnopqrstuvwxyz":
                ans = ans + char
        return ans

    def is_pal(s):
        if len(s) <= 1:
            return True
        else:
            return s[0] == s[-1] and is_pal(s[1:-1])

    return is_pal(to_chars(s))


print(is_palindrome("Hello, olleh"))
print(is_palindrome("Elba non able"))
print(is_palindrome("Hello world!"))
