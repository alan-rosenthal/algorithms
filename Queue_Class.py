#######################################################################
#
#   -- Queue Class --
#
#   Implements a Stack data structure.
#
#   Alan Rosenthal
#   October 2016
#
#######################################################################

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
        return self.items[0]

    def clear(self):
        self.__init__()

    def dump(self):
        if self.size() == 0:
            print('dump queue - ', 'Queue is empty')
        else:
            n = 0
            for i in self.items:
                print('dump queue - ', '[' + str(n) + ']', i)
                n += 1




#######################################################################
#   PYTEST Class
#######################################################################

class TestQueue(object):

    def test_basic(self):
        q = Queue()
        assert q.isEmpty() == True
        assert q.size() == 0

    def test_1_item(self):
        q = Queue()
        q.enqueue('hello there, world')
        assert q.isEmpty() == False
        assert q.size() == 1

        q.clear()
        assert q.isEmpty() == True
        assert q.size() == 0

    def test_3(self):
        q = Queue()
        q.enqueue('hello')
        q.enqueue('there')
        q.enqueue('world')
        assert q.size() == 3
        assert q.isEmpty() == False

        assert q.peek() == 'hello'
        assert q.dequeue() == 'hello'

        assert q.peek() == 'there'
        assert q.dequeue() == 'there'

        assert q.peek() == 'world'
        assert q.dequeue() == 'world'

        assert q.size() == 0
        assert q.isEmpty() == True

    def test_load(self):
        q = Queue()
        for i in range(0, 101):
            q.enqueue(i)

        for i in range(0, 101):
            assert q.peek() == i
            assert q.dequeue() == i

    
