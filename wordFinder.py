import itertools
import re

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

    for pw in possibleWords:
        regex = re.compile('{}\b'.format(pw))
        print regex
        for word in library:
            if regex.search(word):
                print regex.search(word)

findWordinLibrary('aa')
            