# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random
import string

WORDLIST_FILENAME = "words.txt"

def loadWords():
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

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    flag = True
    if lettersGuessed == []:
        return False
    else:
        for letter in secretWord :
            if letter not in lettersGuessed:
                flag = False
        return flag



def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    def find_index(str,c):
        for i, letter in enumerate(str):
            if letter == c:
                yield i
        
    result = ["_", " "]*len(secretWord)

    for letter in secretWord:
        if letter in lettersGuessed:
            #index = secretWord.index(letter)
            indexes = find_index(secretWord, letter)
            for index in indexes:
                result[index*2] = letter
    result = "".join(result)
    return result


def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    ava_list = list(string.ascii_lowercase)
    for letter in lettersGuessed:
        if letter in ava_list:
            ava_list.remove(letter)
    ava_list = "".join(ava_list)
    return ava_list

def alreadyGuessedWord(letter,lettersGuessed):
    if letter in lettersGuessed:
        return True
    else:
        return False
    

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    print("Welcome to the game Hangman!")
    print("I am thinking of a word that is {} letters long.".format(len(secretWord)))
    guess_left = 8 
    lettersGuessed = []
    
    
    while True:
        print("---------------------")
        print("You have {} guesses left".format(guess_left))
        available_letters = getAvailableLetters(lettersGuessed)
        print("Available Letters: {}".format(available_letters))
        guessed_letter = input("Please guess a letter: ")
        guessed_letter.lower()
        
        #string, comprised of letters and underscores that represents
        #what letters in secretWord have been guessed so far
        result = getGuessedWord(secretWord,lettersGuessed)
        
        #check if word had been guessed
        alreadyGuessed = alreadyGuessedWord(guessed_letter,lettersGuessed)
        if alreadyGuessed == True:
            print("Oops! You've already guessed that letter {}".format(result))
        else:
            lettersGuessed.append(guessed_letter) 
            result = getGuessedWord(secretWord,lettersGuessed)
            #if guessed letter is in secret word
            if guessed_letter in secretWord:    
                print("Good guess: {}".format(result))    
            else:
                print("Oops! That letter is not in my word: {}".format(result))
                guess_left -= 1

            #True if all the letters of secretWord are in lettersGuessed
        iswordguessed = isWordGuessed(secretWord,lettersGuessed)
        if iswordguessed == True:
            print("Congratulations, you won!")
            break
        if guess_left==0:
            print("Sorry, you ran out of guesses.")
            break
    print("The secret word is '{}'".format(secretWord))
secretWord = chooseWord(wordlist).lower()
hangman(secretWord)
