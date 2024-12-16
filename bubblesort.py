import random

def bubblesort(list):
    swap = True
    while swap:
        swap = False
        for i in range(0, len(list)-1):
            if list[i] > list[i+1]:
                swap = True
                tmp = list[i]
                list[i] = list[i+1]
                list[i+1] = tmp

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
    bubblesort(list) 
    print(list[0:10])  #display first 10 of sorted list

if __name__ == '__main__':
    main()