import random
import string

# sequential search
#  look for an item and return where that item is in the list.
#  if it's not there, return -1
def sequentialsearch(haystack, needle):
    for i in range(0, len(haystack)):
        if (needle in haystack[i] ):
            return i

    # if we went through the whole haystack, it must not be there
    return -1

def generate_random_string(length):
    """Generates a random string of letters."""
    characters = string.ascii_letters 
    return ''.join(random.choice(characters) for i in range(length))

def randomstrings():
    letters = 'abcdefghijklmopqrstuvwxyz'
    strings = []
    for i in range(0,1000):
        #how long should the string be?
        length = random.randrange(5,15)
        s = ''
        for c in range(0,length):
            #pick a random letter from letters
            i = random.randrange(0,len(letters))
            #append that letter to my string
            s = s + letters[i]
            #add the string to the list of strings
        strings.append(s)
    return strings

def main():
    string = []
    # let's make a list of strings
    for i in range(0, 1000):
        string.append(generate_random_string(10))
        

    target = generate_random_string(2)
    location = sequentialsearch(string, target)
    if location == -1:
        print("couldn't find " + str(target))
    else:
        print("found " + str(target) + " at location " + str(location))


main()