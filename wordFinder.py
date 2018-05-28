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


def charPermutations(usrInput):
    # Takes the user input and creates a list of every possible arrangement.
    # Returns a list.
    # assert any(char.isdigit() == False for char in chars), 'No numbers allowed'

    if any(char.isdigit() for char in usrInput):
        raise Exception('no numbers allowed')

    words = []
    words = [''.join(p) for p in itertools.permutations(usrInput)]
    return words

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
        print 'found these words for ya:'
        for word in wordsFound:
            print '....' + word
    else:
        print 'No words where found!'
    print '----------------------------------------------------------'

def findWordinLibraryBinarySearch(usrInput):
    library = libraryBuilder()
    words = charPermutations(usrInput)
    foundWords = []
    u_lim = int(len(library))
    l_lim = int(0)
    print 'Doing binary search...'
    for word in words:
        while l_lim <= u_lim:
            i = (l_lim + u_lim) // 2
            '''
            print i
            print library[i], word
            '''
            if library[i] == word:
                foundWords.append(word)
                break
            elif library[i] > word:
                u_lim = i - 1
            elif library[i] < word:
                l_lim = i + 1
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
            print findWordinLibraryBinarySearch(chars)

            