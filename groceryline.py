import collections
import random

class GroceryLine:
    def __init__(self,people):
        self.people= people

#put lifesavers in the tube

queue = collections.deque()
peopleWaiting = ["Abigail", "Bob", "Charlie", "Diane", "Edward", "Greta", "Henry", "Isabella"]

for l in range(1,100):
    while len(queue) < 3:
        people = random.choice(peopleWaiting)
        line= GroceryLine(people)
        queue.append(line)
        print (people + " entered@ the queue")
        print (len(queue))
    
    while len(queue) > 6:
        l = queue.popleft()
        print (l.people + " left the queue--balked")
        print (len(queue))

    side = random.randrange(0,3)
    if side == 0:
        l = queue.pop()
        print (l.people + " is now being served")
        print(len(queue))
    else:
        people = random.choice(peopleWaiting)
        line= GroceryLine(people)
        queue.append(line)
        print (people + " entered the queue")
        print (len(queue))



