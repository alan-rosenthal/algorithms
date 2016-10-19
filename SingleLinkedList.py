class Node(object):

    def __init__(self, data):
        self.data = data
        self.next = None


class SingleLinkedList(Node):

    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
        self.current = None

    def append(self, data):
        new_node = Node(data)

        if self.head == None:
            self.head = new_node
            self.tail = new_node

        self.tail.next = new_node
        self.tail = new_node

        self.size += 1
        self.current = new_node

    def get_first(self):
        self.current = self.head
        return self.current.data

    def get_next(self):
        self.current = self.current.next
        return self.current.data


class TestIt(object):

    def test_new(self):
        ll = SingleLinkedList()
        assert ll.size == 0

    def test_one(self):
        ll = SingleLinkedList()
        ll.append('hello')
        assert ll.size == 1

    def test_three(self):
        ll = SingleLinkedList()
        ll.append('hello')
        ll.append('there')
        ll.append('world')
        assert ll.size == 3

        assert ll.get_first() == 'hello'
        assert ll.get_next() == 'there'
        assert ll.get_next() == 'world'
