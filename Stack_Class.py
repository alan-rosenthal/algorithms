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
        self.items = []

    def dump(self):
        if self.size() == 0:
            print('dump stack - ', 'Stack is empty')
        else:
            n = 0
            for i in self.items:
                print('dump stack - ', '[' + str(n) + ']', i)
                n += 1


#######################################################################
#   Test Class
#######################################################################

class TestStack(object):

    def test(self):

        s = Stack()

        assert s.isEmpty() == True
        assert s.size() == 0

        for i in range(100):
            s.push(i)
        assert s.peek() == 99
        assert s.size() == 100

        for i in range(99):
            s.pop()
        assert s.pop() == 0

        assert s.isEmpty() == True
        assert s.size() == 0

        print('All tests have succeeeded :)')
        return True

#######################################################################
#   Main
#######################################################################

t = TestStack()
t.test()