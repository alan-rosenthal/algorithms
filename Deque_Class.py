#######################################################################
#
#   -- Deque Class
#
#   Implements a Deque data structure.
#
#   Alan Rosenthal
#   October 2016
#
#######################################################################

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

    def peekFront(self):
        return self.items[0]

    def peekRear(self):
        return self.items[self.size() - 1]

    def dump(self):
        n = 0
        while n < self.size():
            print(n, self.items[n])
            n += 1


####################################
#   Test code
####################################

class TestDeque(object):

    def test(self):
        d = Deque()

        d.isEmpty() == True
        assert d.size() == 0

        d.pushFront('hello')
        d.pushRear('there')
        d.pushRear('world')
        assert d.isEmpty() == False
        assert d.size() == 3

        assert d.peekFront() == 'hello'
        assert d.peekRear() == 'world'

        assert d.popFront() == 'hello'
        assert d.popFront() == 'there'
        assert d.popFront() == 'world'

        return True


###################################
#   Main Program
###################################

t = TestDeque()
if t.test():
    print('all tests have succeeded :)')