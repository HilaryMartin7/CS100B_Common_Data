import random
def selectionsort(list):
    for i in range(0, len(list)):
        min = i
        #look for an item smaller than list[min]
        for j in range(i, len(list)):
            if list[j] < list[min]:
                min = j     #just remember where this was
        #we've found it. Swap it into this location
        tmp = list[i]
        list[i]=list[min]
        list[min] = tmp

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
    selectionsort(list) 
    print(list[0:10])  #display first 10 of sorted list

if __name__ == '__main__':
    main()