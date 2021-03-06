import itertools
import time


# Builds a library from txt file.
def libraryBuilder():
    # Loads in the words and builds a library (List) of words.
    # Returns a list.
    text = open('wordlookup/sorted_lib.txt', 'r').read()
    library = text.split('\n')

    return library


# Finds words in the library.
def findWordinLibraryStandard(usrInput):
    # Finds if any of the Char Permutations found exists in the library
    # Returns a list of found (if any) words.
    library = libraryBuilder()
    possibleWords = charPermutations(usrInput)
    wordsFound = {}
    xtime = time.time()
    for word in possibleWords:
        if word in library:
            wordsFound[library.index(word)] = word
    wordsFound['time'] = time.time() - xtime
    if wordsFound:
        return wordsFound
    else:
        return None


# Mostly just a test case, but searches through the library linearly.
def linearSearch(usrInput):
    library = libraryBuilder()
    words = charPermutations(usrInput)
    wordDict = {}
    xtime = time.time()
    for word in words:
        for x in range(0, len(library)):
            if library[x] == word:
                wordDict[x] = library[x]
    wordDict['time'] = time.time() - xtime
    return wordDict


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


# Finds words in the library by doing
# a Binary Search.
def findWordinLibraryBinarySearch(usrInput):
    usrInput = usrInput.lower()
    if any(char.isdigit() for char in usrInput):
        raise Exception('no numbers allowed')

    library = libraryBuilder()
    words = charPermutations(usrInput)

    foundWords = {}
    xtime = time.time()
    for word in words:
        first = int(0)  # Making sure its integers.
        last = int(len(library))  # Making sure its integers.
        found = False
        while first <= last and not found:
            midpoint = (first + last) / 2
            if library[midpoint] == word:
                found = True
            else:
                if word < library[midpoint]:
                    last = midpoint - 1
                else:
                    first = midpoint + 1
        if found:
            foundWords[midpoint] = library[midpoint]
    xtime = time.time() - xtime
    foundWords['time'] = xtime
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

