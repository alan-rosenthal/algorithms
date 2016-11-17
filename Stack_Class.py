#######################################################################
#
#   -- Stack Class --
#
#   Implements a Stack data structure.
#
#       .size()         Returns the number of items in the stack.
#       .isEmpty()      Returns True if the stack is empty.
#       .push(item)     Pushes the item onto the top of the stack.
#       .pop()          Pops the item off the top of the stack
#                           and returns it.
#       .peek()         Returns the item on the top of the stack
#                           and leaves it on the top of the stack.
#       .clear()        Removes all items on the stack and leaves it empty.
#       .dump()         For debugging, dumps the contents of the stack to 
#                           standard out.
#
#   Alan Rosenthal
#   October 2016
#
#######################################################################

import unittest

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

class TestIt(unittest.TestCase):

    def test_basic(self):
        s = Stack()
        self.assertTrue( s.isEmpty(), 'An empty stack should test as empty')
        self.assertEqual(s.size(), 0, 'An empty stack should have size of zero')

    def test_1_item(self):
        s = Stack()
        s.push('hello there, world')
        self.assertFalse(s.isEmpty(), 'A stack with 1 items is not empty')
        self.assertEqual(s.size(), 1, 'A stack with 1 item has a size of 1')

        s.clear()
        self.assertTrue(s.isEmpty(), 'A stack that was just cleared should be empty')
        self.assertEqual(s.size(), 0, 'A stack that was just cleared should have size 0')

    def test_3(self):
        s = Stack()
        s.push('hello')
        s.push('there')
        s.push('world')
        self.assertEqual(s.size(), 3, 'A stack with 3 items should have size of 3')
        self.assertFalse(s.isEmpty(), 'A stack with 3 items is not empty')

        item1 = s.peek()
        item2 = s.pop()
        self.assertEqual(item1, 'world', 'The top item on the stack should be "world"')
        self.assertEqual(item2, 'world', 'The top item on the stack should be "world"')

        item1 = s.peek()
        item2 = s.pop()
        self.assertEqual(item1, 'there', 'The top item on the stack should be "there"')
        self.assertEqual(item2, 'there', 'The top item on the stack should be "there"')

        item1 = s.peek()
        item2 = s.pop()
        self.assertEqual(item1, 'hello', 'The top item on the stack should be "hello"')
        self.assertEqual(item2, 'hello', 'The top item on the stack should be "hello"')


        self.assertEqual(s.size(), 0, 'All items should have been popped off the stack')
        self.assertTrue(s.isEmpty(), 'The stack should be empty')

    def test_load(self):
        s = Stack()
        for i in range(0, 101):
            s.push(i)

        for i in range(100, -1, -1):
            self.assertEqual(s.peek(), i, 'Push 100 values and peek them should be the same')
            self.assertEqual(s.pop(), i, 'Push 100 values and pop them should be the same')


if __name__ == '__main__':
    unittest.main()
