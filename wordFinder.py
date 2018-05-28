import itertools


# Builds a library from txt file.
def libraryBuilder():
    # Loads in the words and builds a library (List) of words.
    # Returns a list.
    text = open('words_alpha.txt', 'r').read()
    text = text.replace('\r', '')
    library = text.split('\n')
    sorted(library)
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

    for word in words:
        first = int(0)  # Making sure its integers.
        last = int(len(library))  # Making sure its integers.
        found = False
        while first <= last and not found:
            midpoint = int((first + last) // 2)
            w = library[midpoint]
            if library[midpoint] == word:
                found = True
            else:
                if word < library[midpoint]:
                    last = midpoint - 1
                else:
                    first = midpoint + 1
        if found:
            foundWords.append(library[midpoint])
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
