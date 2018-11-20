"""
Hangman game

This game is to guess the word.
User has 6 attempts.
"""
import random

WORD_LIST_FILENAME = "words.txt"


def load_words() -> list:
    """
    Returns a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # file: file
    file = open(WORD_LIST_FILENAME, 'r')
    # line: string
    line = file.readline()
    # word_list: list of strings
    words_list = line.split()
    print("  ", len(words_list), "words loaded.")
    return words_list


def choose_word(words_list: list) -> str:
    """
    word_list (list): list of words (strings)

    Returns a word from words_list at random
    """
    return random.choice(words_list)

# Load the list of words into the variable word_list
# so that it can be accessed from anywhere in the program


WORD_LIST = load_words()


def is_word_guessed(secret_word_to_guess: str, letters_guessed: list) -> bool:
    """
    secret_word: string, the word the user is guessing
    letters_guessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
    False otherwise
    """
    secret_word = list(secret_word_to_guess)
    for letter in secret_word:
        if letter in letters_guessed:
            continue
        else:
            return False
    return True


def get_guessed_word(secret_word_to_guess: str, letters_guessed: list) -> str:
    """"
    secret_word: string, the word the user is guessing
    letters_guessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
    what letters in secret_word have been guessed so far.
    """
    secret_word = list(secret_word_to_guess)
    for count, elem in enumerate(secret_word_to_guess):
        if elem not in letters_guessed:
            secret_word[count] = '_ '
    guessed_word = ''.join(secret_word)
    return guessed_word


def get_available_letters(letters_guessed: list) -> str:
    """"
    letters_guessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    """
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    available_letters = ""
    for letter in alphabet:
        if letter not in letters_guessed:
            available_letters += letter
    return available_letters


def hangman(secret_word: str):
    """"
    secret_word: string, the secret word to guess.

    Starts up an interactive game of Hangman.
    """
    print("Welcome to the game Hangman!")
    print("I am thinking of a word that is", len(secret_word), "letters long")
    print("_ _ _ _ _ _ _ _")

    letters_guessed = []
    guesses = 6
    # Guessing the word in 6 tries
    while not is_word_guessed(secret_word, letters_guessed) and guesses > 0:
        print("You have " + str(guesses) + " guesses left")
        print("Available letters: " + get_available_letters(letters_guessed))

        # If letter already used
        while True:
            guess_letter = str(input("Please guess a letter: ").lower())
            if guess_letter in letters_guessed:
                print("Oops! You've already guessed that letter: " +
                      get_guessed_word(secret_word, letters_guessed))
                print("_ _ _ _ _ _ _ _")
                print("You have " + str(guesses) + " guesses left")
                print("Available letters: " + get_available_letters(letters_guessed))
            else:
                break
        letters_guessed += guess_letter

        # If word is found
        if is_word_guessed(secret_word, letters_guessed):
            print("Good guess: " + get_guessed_word(secret_word, letters_guessed))
            print("_ _ _ _ _ _ _ _")
            print("Congratulations, you won!")
        # If guessed_letter in secret_word
        elif guess_letter in secret_word:
            print("Good guess: " + get_guessed_word(secret_word, letters_guessed))
            print("_ _ _ _ _ _ _ _")
            # If guessed_letter not in secret_word
        else:
            print("Oops! That letter is not in my word: " +
                  get_guessed_word(secret_word, letters_guessed))
            print("_ _ _ _ _ _ _ _")
            guesses -= 1

        # If all guesses are used
        if guesses == 0:
            print("Sorry, you ran out of guesses. The word was " + secret_word + ".")


# Code testing
SECRET_WORD_TEST = choose_word(WORD_LIST).lower()
hangman(SECRET_WORD_TEST)
