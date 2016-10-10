class Stack(object):

    def __init__(self):
        self.items = []

    def size(self):
        return len(self.items)

    def isEmpty(self):
        return self.size() == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items(self.size() - 1)



s = Stack()

s.push('alan')
s.push('bill')
s.push('chuck')

while not s.isEmpty():
    print(s.pop())
