from .node import DoubleLinkedNode as Node

class Queue:
    def __init__(self, m=None):
        self.head = self.tail = None
        self.max = m

    def shift(self, value):
        if self.max and self.count == self.max:
            return "Queue full"
        if not self.head:
            self.head = Node(value, prev=None, nxt=None)
            self.tail = self.head
        else:
            prev_tail, self.tail = self.tail, Node(value, prev=self.tail, nxt=None)
            prev_tail.next = self.tail

    def unshift(self):
        if not self.head and not self.tail:
            return None
        self.head = self.head.next
        try:
            self.head.prev = None
        except AttributeError:
            self.head = self.tail = None

    def dump(self):
        node = self.head
        output = '|--Front--| '
        while node:
            output += repr(node)
            node = node.next
        output += ' |--Back--|'
        return output

    @property
    def count(self):
        node = self.head
        i = 0
        while node:
            i += 1
            node = node.next
        return i

    @property
    def empty(self):
        return self.count > 0
