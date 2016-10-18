#######################################################################
#
#   -- Stack Class --
#
#   Implements a Stack data structure.
#
#   Alan Rosenthal
#   October 2016
#
#######################################################################

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
        return self.items[self.size() - 1]

    def clear(self):
        self.__init__()

    def dump(self):
        if self.size() == 0:
            print('dump stack - ', 'Stack is empty')
        else:
            n = 0
            for i in self.items:
                print('dump stack - ', '[' + str(n) + ']', i)
                n += 1


#######################################################################
#   PYTEST Class
#######################################################################

class TestStack(object):

    def test_basic(self):
        s = Stack()
        assert s.isEmpty() == True
        assert s.size() == 0

    def test_1_item(self):
        s = Stack()
        s.push('hello there, world')
        assert s.isEmpty() == False
        assert s.size() == 1

        s.clear()
        assert s.isEmpty() == True
        assert s.size() == 0

    def test_3(self):
        s = Stack()
        s.push('hello')
        s.push('there')
        s.push('world')
        assert s.size() == 3
        assert s.isEmpty() == False

        assert s.peek() == 'world'
        item = s.pop()
        assert item == 'world'

        assert s.peek() == 'there'
        item = s.pop()
        assert item == 'there'

        assert s.peek() == 'hello'
        item = s.pop()
        assert item == 'hello'

        assert s.size() == 0
        assert s.isEmpty() == True

    def test_load(self):
        s = Stack()
        for i in range(0, 101):
            s.push(i)

        for i in range(100, -1, -1):
            assert s.peek() == i
            assert s.pop() == i

