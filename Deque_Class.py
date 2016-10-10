class Deque(object):

    def __init(self):
        items = []

    def size(self):
        return len(self.items)

    def isEmpty(self):
        return self.items.size() == 0

    def pushFront(self, item):
        self.items.append(0, item)

    def pushRear(self, item):
        self.items.append(item)

    def popFront(self):
        return self.items.pop(0)

    def popRear(self):
        return self.items.pop(self.size() - 1)
