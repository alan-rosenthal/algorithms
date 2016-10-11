class Deque(object):

    def __init__(self):
        self.deque = []

    def size(self):
        return len(self.deque)

    def isEmpty(self):
        return self.size() == 0

    def pushFront(self, item):
        self.deque.insert(0, item)

    def pushRear(self, item):
        self.deque.insert(self.size(), item)

    def popFront(self):
        return self.deque.pop(0)

    def popRear(self):
        return self.deque.pop()


class Stack(Deque):

    def __init__(self):
        self.s = Deque()

    def size(self):
        return self.s.size()

    def isEmpty(self):
        return self.s.isEmpty()

    def push(self, item):
        self.s.pushFront(item)

    def pop(self):
        return self.s.popFront()


class Queue(Deque):

    def __init__(self):
        self.q = Deque()

    def size(self):
        return self.q.size()

    def isEmpty(self):
        return self.q.isEmpty()

    def enqueue(self, item):
        self.q.pushRear(item)

    def dequeue(self):
        return self.q.popFront()




###
### Main Routine
###

print('Stack Test')

s = Stack()

s.push('world')
s.push('there')
s.push('hello')

while not s.isEmpty():
    print(s.pop())

print('')
print('Queue Test')

q = Queue()

q.enqueue('hello')
q.enqueue('there')
q.enqueue('world')

while not q.isEmpty():
    print(q.dequeue())

