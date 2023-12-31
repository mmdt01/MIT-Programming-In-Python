# Problem Set 2, hangman.py
# Name: Matthys

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
    # initialise index of letter in secret_word
    i = 0
    # loop through letters in secret_word
    for letter in secret_word:
        # check if letter is in letters_guessed
        if letter in letters_guessed:
            # increase index
            i += 1
            # return true if letter is contained and index is equal to length of secret_word
            if i == len(secret_word):
                return True
        else:
            # return false if letter is not contained
            return False

def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '_ ' = unknown letters

    '''
    # initialize index of letter in secret_word
    n = 0 
    # convert string to a list to enable easy operations on secret_word
    word = list(secret_word)
    # loop through letters in secret_word
    for letter in secret_word:
        # check if letter is not within in letters_guessed
        if letter not in letters_guessed:
            # if true, change that letter to represent an unknown letter
            word[n] = "_ "
        n += 1   
    # convert list back to a sting
    guessed_word = ''.join(word)
    return guessed_word

def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    # list of all letters in the alphabet
    all_letters = list(string.ascii_lowercase)
    # remove letters guessed from all_letters
    for letter in letters_guessed:
        all_letters.remove(letter)
    # convert list of remaining letters to a string
    available_letters = ''.join(all_letters)
    return available_letters


# find number of unique letters in secret word
def unique_letters(secret_word):
    '''
    secret_word: string, the secret word to guess.
    returns: integer, number of unique letters in secret word
    '''
    # convert secret word to a list
    word = list(secret_word)
    # create empty list to store unique letters
    unique = []
    # loop through letters in secret word
    for letter in word:
        # check if letter is not in unique list
        if letter not in unique:
            # add letter to unique list
            unique.append(letter)
    # return number of unique letters
    return len(unique)


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
    g = 6   # initialise number of guesses
    w = 3   # initialise number of warnings
    ltrs_guessed = []    # initialise number of guesses

    # starts up game
    print("Welcome to the game Hangman!")
    # let the user know how many letters the secret word contains
    print("I am thinking of a word that is", len(secret_word), "letters long.\n------------------------")

    # enter guess loop 
    while g > 0 and is_word_guessed(secret_word, ltrs_guessed) == False :
        # display number of guesses left
        print("You have", g, "guesses left.")
        # display number of warnings left
        print("You have", w, "warnings left.")
        # display available letters
        print("Available letters:", get_available_letters(ltrs_guessed))
        
        # take a guess
        guess = input("Please guess a letter: ")

        # accept capital letters as a valid input
        guess = guess.lower()
        
        # check whether guess is valid
        if guess not in list(string.ascii_lowercase):
            print("\nOops! Your entry is not a valid input. Only singular alphabetical letters are accepted.")
            w -= 1    # decrement number of warnings
            if w == 0:
                print("Unfortunately, as this was you're final warning, you also lose a guess.")
                g -= 1    # user loses one guess
                w += 1    # add one warning back
        # check whether guess has already been made
        elif guess in ltrs_guessed:
            # if user has one or more warnings left, they lose one warning
            if w > 1:
                w -= 1
                print("\nOops! You've already guessed that letter. You now have", w,"warnings left.")
            # if user has no warnings left, they should lose a guess
            else:
                print("\nOops! You've already guessed that letter.\nUnfortunately, as this was you're final warning, you also lose a guess.")
                g -= 1    # user loses one guess
                w += 1    # add one warning back
        # user guess is correct
        elif guess in secret_word: # remember to convert secret word to a list
            print("\nWell done! Your guess is correct!")
            ltrs_guessed.append(guess)   # add guess to letters_guessed
        # user guess is incorrect
        else:
            print("\nYour guess is unfortunately wrong. Try again!")
            ltrs_guessed.append(guess)   # add guess to letters_guessed
            # if user guess is incorrent and vowel
            if guess in ['a','e','i','o','u']:
                print("(2 guesses are lost for an incorrect vowel)")
                g -= 2
            else:
                g -= 1   

        # display secret word with only guessed letters shown
        print(get_guessed_word(secret_word, ltrs_guessed))
        print("\n------------------------")

    if g == 0:
        # display message that guesses have run out
        print("You are out of guesses :( \nBetter luck next time!\n")
    else:
        # display message that secret word has been guessed
        print("Congratulations!!! You won! :) \nYour total score for this game is:", g*(unique_letters(secret_word)), "\n")

# find number of unique letters in secret word
def unique_letters(secret_word):
    # convert secret word to a list
    word = list(secret_word)
    # create empty list to store unique letters
    unique = []
    # loop through letters in secret word
    for letter in word:
        # check if letter is not in unique list
        if letter not in unique:
            # add letter to unique list
            unique.append(letter)
    # return number of unique letters
    return len(unique)


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
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    pass



def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    pass



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
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    pass



# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
    # pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.
    
    secret_word = choose_word(wordlist)
    hangman(secret_word)

###############
    
    # To test part 3 re-comment out the above lines and 
    # uncomment the following two lines. 
    
    #secret_word = choose_word(wordlist)
    #hangman_with_hints(secret_word)
