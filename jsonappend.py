import collections
import json

class LifeSaver:
    def __init__(self, flavor):
        if type(flavor) is dict:
            self.__dict__.update(flavor)
        else:
            self.flavor = flavor
    def toJson(self):
        return self.__dict__
    
tube = collections.deque()
f = open('tube.json')
lifesavers = json.loads(f.read())
f.close()
for l in lifesavers:
    tube.append(LifeSaver(l))
print (l.flavor)
