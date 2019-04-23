# Problem Set 2, hangman.py
# Name: Quadri Adekunle
# Collaborators:
# Time spent:

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string

WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist


def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code

# -----------------------------------


# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    for letter in secret_word:
        if letter not in letters_guessed:
            return False
    return True


def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    guess_words = ""

    for letter in secret_word:
        if letter not in letters_guessed:
            guess_words = guess_words + '_ '
        else:
            guess_words = guess_words + letter
    return guess_words


def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    remaining_letter = ""
    for letter in string.ascii_lowercase:
        if letter not in letters_guessed:
            remaining_letter = remaining_letter + letter
    return remaining_letter


def get_unique_words(secret_word):
    '''
    secret_words: string, the word the user is guessing
    returns: number, the length of the each unqiue letter in secret word, the letter the occur at least once
    '''

    unique_word = []
    for letter in secret_word:
        if letter not in unique_word:
            unique_word.append(letter)
    return len(unique_word)


def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.

    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.

    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.

    Follows the other limitations detailed in the problem write-up.
    '''
    number_of_guesses = 6
    number_of_warning = 3
    letters_guessed = []
    print("Welcome to the game Hangman!")
    print("I am thinking of a word that is", len(secret_word), "letters long.")

    while number_of_guesses > 0 and not is_word_guessed(secret_word, letters_guessed):
        print("-" * 13)
        print("You have", number_of_warning, "warnings left.")
        print("You have", number_of_guesses, "guesses left.")
        print("Available letters:", get_available_letters(letters_guessed))
        guess = input("Please guess a letter: ")

        if not str.isalpha(guess):
            if number_of_warning < 1:
                number_of_guesses -= 1
            else:
                number_of_warning -= 1
            message = "Oops! That is not a valid letter. You have " + \
                str(number_of_warning) + " left: "
        else:
            guess = str.lower(guess)

            if guess in letters_guessed:
                if number_of_warning < 1:
                    number_of_guesses -= 1
                else:
                    number_of_warning -= 1
                message = "Oops! You've guessed that letter. You have " + \
                    str(number_of_warning) + " left: "
            else:
                letters_guessed.append(guess)

                if guess in secret_word:
                    message = "Good guess "
                else:
                    if guess in ['a', 'e', 'i', 'o', 'u']:
                        number_of_guesses -= 2
                    else:
                        number_of_guesses -= 1

                    message = "Oops! That letter is not in my word: "
        print(message, get_guessed_word(secret_word, letters_guessed))
    print('_'*13)
    if is_word_guessed(secret_word, letters_guessed):
        print("Congratulations, you won! \n Your total score for this game is: ", str(
            number_of_guesses * get_unique_words(secret_word)))
    else:
        print("Sorry, you ran out of guesses. The word was", secret_word)

# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
# (hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------


def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the 
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise: 
    '''
    my_word = my_word.strip().replace(" ", "")
    other_word = other_word.strip().replace(" ", "")
    if len(my_word) != len(other_word):
        return False

    my_word = list(my_word)
    other_word = list(other_word)

    idx = 0

    for letter in my_word:
        if letter != '_':
            if my_word.count(letter) != other_word.count(letter):
                return False

            if letter != other_word[idx]:
                return False
        idx += 1
    return True


def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    matched_words = []

    for word in wordlist:
        if match_with_gaps(my_word, word):
            matched_words.append(word)

    if len(matched_words) > 0:
        print(' '.join(matched_words))
    else:
        print('No matches found')


def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.

    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.

    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.

    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word. 

    Follows the other limitations detailed in the problem write-up.
    '''
    number_of_guesses = 6
    number_of_warning = 3
    letters_guessed = []
    print("Welcome to the game Hangman!")
    print("I am thinking of a word that is", len(secret_word), "letters long.")

    while number_of_guesses > 0 and not is_word_guessed(secret_word, letters_guessed):
        print("-" * 13)
        print("You have", number_of_warning, "warnings left.")
        print("You have", number_of_guesses, "guesses left.")
        print("Available letters:", get_available_letters(letters_guessed))
        guess = input("Please guess a letter: ")

        if guess == '*':
            show_possible_matches(get_guessed_word(
                secret_word, letters_guessed))
        else:
            if not str.isalpha(guess):
                if number_of_warning < 1:
                    number_of_guesses -= 1
                else:
                    number_of_warning -= 1
                message = "Oops! That is not a valid letter. You have " + \
                    str(number_of_warning) + " left: "
            else:
                guess = str.lower(guess)

                if guess in letters_guessed:
                    if number_of_warning < 1:
                        number_of_guesses -= 1
                    else:
                        number_of_warning -= 1
                    message = "Oops! You've guessed that letter. You have " + \
                        str(number_of_warning) + " left: "
                else:
                    letters_guessed.append(guess)

                    if guess in secret_word:
                        message = "Good guess "
                    else:
                        if guess in ['a', 'e', 'i', 'o', 'u']:
                            number_of_guesses -= 2
                        else:
                            number_of_guesses -= 1

                        message = "Oops! That letter is not in my word: "
            print(message, get_guessed_word(secret_word, letters_guessed))
    print('_'*13)
    if is_word_guessed(secret_word, letters_guessed):
        print("Congratulations, you won! \n Your total score for this game is: ", str(
            number_of_guesses * get_unique_words(secret_word)))
    else:
        print("Sorry, you ran out of guesses. The word was", secret_word)


# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.

if __name__ == "__main__":

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.

    #secret_word = choose_word(wordlist)
    # hangman(secret_word)

    ###############

    # To test part 3 re-comment out the above lines and
    # uncomment the following two lines.

    secret_word = choose_word(wordlist)
    hangman_with_hints(secret_word)
