class LinkedList:

    def __init__(self, collection=None):
        self.head = None
        if collection:
            for item in reversed(collection): 
                self.insert(item)

    def __iter__(self):
        def value_generator():
            current = self.head
            while current:
                yield current.value
                current = current.next
        return value_generator()

    def insert(self, value):
            self.head = Node(value, self.head)

    def __eq__(self, other):
        return list(self) == list(other)


class Node:
    def __init__(self, value, next = None):
        self.value = value
        self.next = next

