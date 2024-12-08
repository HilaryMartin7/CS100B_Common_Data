import random

class Student:
    def __init__(self, id, name):
        self.id = id
        self.name = name

roster = {} #empty dictionary
names = ['alice', 'bob', 'carol', 'dave', 'edith', 'fred']
#add a student with random ID
for n in names:
    id = random.randrange (0,100000)
    roster [id] = Student(id,n)

print ('here are the studnts in your roster:')
for s in roster:
    print(s)


#ask user for an id to output
i = input ('which id would you like information on? Type -1 to quit:')
i = int(i)
while i != -1:
    print (str(i) + ":" + roster[i].name)
    i = input ('which id would you like information on? Type -1 to quit:')
    i = int(i)