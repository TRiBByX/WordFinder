import itertools
import re
import unittest

def libraryBuilder():
    # Loads in the words and builds a library (List) of words.
    # Returns a list.
    text = open('words_alpha.txt', 'r').read()
    text = text.replace('\r', '')
    library = text.split('\n')
    return library


def charPermutations(chars):
    # Takes the user input and creates a list of every possible arrangement.
    # Returns a list.
    # assert any(char.isdigit() == False for char in chars), 'No numbers allowed'

    if any(char.isdigit() for char in chars):
        raise Exception('no numbers allowed')

    chars = list(chars)
    words = []
    possiblewords = list(itertools.permutations(chars))
    for word in possiblewords:
        newWord = ''.join(word)
        words.append(newWord)
    return words

def findWordinLibrary(usrInput):
    # Finds if any of the Char Permutations found exists in the library
    # Returns a list of found (if any) words.
    library = libraryBuilder()
    possibleWords = charPermutations(usrInput)
    wordsFound = []

    for word in possibleWords:
        if word in library:
            wordsFound.append(word)

    if wordsFound:    
        print 'found these words for ya:'
        for word in wordsFound:
            print '....' + word
    else:
        print 'No words where found!'
    print '----------------------------------------------------------'


if __name__ == '__main__':
    while True:
        print 'What characters do you want to search for?'
        chars = raw_input()
        findWordinLibrary(chars)

            