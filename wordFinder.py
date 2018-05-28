import itertools
import re
import unittest


# Builds a library from txt file.
def libraryBuilder():
    # Loads in the words and builds a library (List) of words.
    # Returns a list.
    text = open('words_alpha.txt', 'r').read()
    text = text.replace('\r', '')
    library = text.split('\n')
    return library


# Permuates through the user input to create
# all possible character combinations.
def charPermutations(usrInput):
    # Takes the user input and creates a list of every possible arrangement.
    # Returns a list.

    if any(char.isdigit() for char in usrInput):
        raise Exception('no numbers allowed')

    words = []
    words = [''.join(p) for p in itertools.permutations(usrInput)]
    return words


# Finds words in the library.
def findWordinLibraryStandard(usrInput):
    # Finds if any of the Char Permutations found exists in the library
    # Returns a list of found (if any) words.
    library = libraryBuilder()
    possibleWords = charPermutations(usrInput)
    wordsFound = []

    for word in possibleWords:
        if word in library:
            wordsFound.append(word)

    if wordsFound:
        return wordsFound
    else:
        return None


# Finds words in the library by doing
# a Binary Search.
def findWordinLibraryBinarySearch(usrInput):
    library = libraryBuilder()
    words = charPermutations(usrInput)
    foundWords = []
    u_lim = int(len(library))-1
    l_lim = int(0)

    for word in words:

        while l_lim <= u_lim:
            i = (l_lim + u_lim) // 2

            if library[i] < word:
                print i, library[i] < word
                l_lim = i + 1
            elif library[i] > word:
                print i, library[i] > word
                u_lim = i - 1
            else:
                foundWords.append(library[i])

        '''
        while l_lim <= u_lim:
            i = (l_lim + u_lim) // 2
            if library[i] == word:
                foundWords.append(word)
                break
            elif library[i] > word:
                u_lim = i - 1
            elif library[i] < word:
                l_lim = i + 1
        '''
    return foundWords


# 11 char limit
if __name__ == '__main__':
    print 'Starting...'
    while True:
        print 'What characters do you want to search for?'
        chars = raw_input()
        if len(chars) > 11:
            print 'no inputs above 11 chars'
        else:
            print 'binary: ', findWordinLibraryBinarySearch(chars)
            # print 'standard: ', findWordinLibraryStandard(chars)
