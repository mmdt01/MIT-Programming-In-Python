


def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    i = 0
    for letter in secret_word:
        # check if letter is in letters_guessed
        if letter in letters_guessed:
            i += 1
            if i == len(secret_word):
                return True
        else:
            return False

secret_word = input("Enter secret word: ")
letters_guessed = input("Enter a list of letters guessed: ")

print(is_word_guessed(secret_word, letters_guessed))
                    

