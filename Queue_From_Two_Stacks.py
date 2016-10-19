#######################################################################
#
#   Queue_From_Two_Stacks
#
#   Create the functionality of a Queue from two stacks.
#   Uses the trick that when you pop things off a stack you reverse the order.
#   So reversing the order of a stack twice actually puts it in normal queue order.
#   Then you can just pop items off of the "stack" and you get them in FIFO order.
#
#   Alan Rosenthal
#   October 2016
#
#######################################################################

class Stack(object):

    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items)-1]

    def isEmpty(self):
        return self.items == []

    def size(self):
        return self.items.count()

    def clear(self):
        self.items = []

    def dump(self, message):
        print('')
        print(message)
        n = 0
        for i in self.items:
            print(n, i)
            n += 1


class Queue(Stack):

    def __init__(self):
        self.s1 = Stack()
        self.s2 = Stack()

    def enqueue(self, newItem):
        while not self.s1.isEmpty():
            self.s2.push(self.s1.pop())

        self.s1.push(newItem)

        while not self.s2.isEmpty():
            self.s1.push(self.s2.pop())

    def dequeue(self):
        return self.s1.pop()


#####################################
#   TestIt
#####################################

class TestIt():

    def test_1_item(self):
        q = Queue()

        q.enqueue('one')
        assert q.dequeue() == 'one'

    def test_2_items(self):
        q = Queue()

        q.enqueue('one')
        q.enqueue('two')
        assert q.dequeue() == 'one'
        assert q.dequeue() == 'two'

    def test_4_items_mixed(self):
        q = Queue()

        q.enqueue('one')
        q.enqueue('two')
        q.enqueue('three')
        assert q.dequeue() == 'one'
        assert q.dequeue() == 'two'
        q.enqueue('four')
        assert q.dequeue() == 'three'
        assert q.dequeue() == 'four'






