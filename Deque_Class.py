class Deque(object):

    def __init__(self):
        self.items = []

    def size(self):
        return len(self.items)

    def isEmpty(self):
        return self.size() == 0

    def pushFront(self, item):
        self.items.insert(0, item)

    def pushRear(self, item):
        self.items.append(item)

    def popFront(self):
        return self.items.pop(0)

    def popRear(self):
        return self.items.pop(self.size() - 1)


####################################
#   Test code
####################################

d = Deque()

print(d.size())

d.pushRear('world')
d.pushFront('there')
d.pushFront('hello')

while not d.isEmpty():
    print(d.popRear())
