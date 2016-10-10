class Queue(object):

    def __init__(self):
        self.items = []

    def size(self):
        return len(self.items)

    def isEmpty(self):
        return self.size() == 0

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        return self.items.pop(0)

    def peek(self):
        return self.items(self.size() - 1)



q = Queue()

q.enqueue('alan')
q.enqueue('bill')
q.enqueue('chuck')

while not q.isEmpty():
    print(q.dequeue())

    
