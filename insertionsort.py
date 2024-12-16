import random

def insertionsort(list):
    for i in range(1, len(list)):
        number = list[i]
        pos = i
        while pos > 0 and list[pos-1] > number:
            list[pos] = list[pos-1]
            pos = pos - 1
        list[pos] = number

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
   
    list = randomstrings()
    print(list[0:10])  #display first 10 of random list
    insertionsort(list) 
    print(list[0:10])  #display first 10 of sorted list

if __name__ == '__main__':
    main()