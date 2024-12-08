import collections
import random
import json

class LifeSaver:
    def __init__(self,flavor):
        self.flavor= flavor
    def toJson(self):
        return self.__dict__


#put lifesavers in the tube

tube = collections.deque()
flavors = ["orange", "pineapple", "cherry", "raspberry", "watermelon"]

for l in range(1,10):
    flavor = random.choice(flavors)
    lifesaver = LifeSaver(flavor)
    tube.append(lifesaver)

lifesavers = []
for l in tube:
        #convert the LifeSaver object to dictionary so we can conver it to JSON
    lifesavers.append(l.toJson())
    
f = open('tube.json', 'w')
f.write(json.dumps(lifesavers))
f.close()

#eat from each end
while len(tube) > 0:
    side = random.randrange(0,2)
    if side == 0:
        l = tube.pop()
        print ("eating" + l.flavor + "from right side")
    else:
        l = tube.popleft()
        print ("eating" + l.flavor + "from the left side")

print ("Yum")

