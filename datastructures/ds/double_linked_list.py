from .node import DoubleLinkedNode as Node

class DoubleLinkedList:
    def __init__(self):
        self.head = self.tail = None
        self._count = 0

    def push(self, obj):
        '''Place a node at the tail of the list'''
        if not self.head:
            self.head = self.tail = Node(obj, prev=None, nxt=None)
        else:
            prev_tail, self.tail = self.tail, Node(obj, prev=self.tail, nxt=None)
            # previous tail still points to None, so we make it point to the new tail
            prev_tail.next = self.tail
        self._count += 1

    def shift(self, obj):
        '''Place a node at the head of the list'''
        if not self.head:
            self.head = self.tail = Node(obj, None, None)
        else:
            prev_head, self.head = self.head, Node(obj, prev=None, nxt=self.head)
            prev_head.prev = self.head
        self._count += 1

    def pop(self):
        '''Remove current node at the tail and return its value'''
        if not self.tail and not self.head:
            return None
        res = self.tail.value
        self.tail = self.tail.prev
        try:
            self.tail.next = None
        except AttributeError: # Reached NoneType, only 1 node in list
            self.head = self.tail = None

        self._count -= 1
        return res

    def unshift(self):
        '''Remove current node at head and return its value'''
        if not self.head and not self.tail:
            return None
        res = self.head.value
        self.head = self.head.next
        try:
            self.head.prev = None
        except AttributeError: # Reached NoneType
            self.head = self.tail = None

        self._count -= 1
        return res

    def remove(self, obj):
        '''Remove a node and return its index'''
        i = 0
        current = self.head
        while current:
            if current.value == obj:
                if current is self.head:
                    self.unshift()
                elif current is self.tail:
                    self.pop()
                else:
                    prev_node, next_node = current.prev, current.next
                    # Link the two nodes next to current node together
                    prev_node.next = next_node
                    next_node.prev = prev_node
                    self._count -= 1
                return i
            current = current.next
            i += 1

    def get(self, index):
        '''Get the value of the node at the given index.
        Returns None if value isn't in any of the nodes

        Can probably rewrite this function to take an object like remove
        and implement it like so:

        current = self.head
        while current and current.value is not obj:
            current = current.next
        return current.value
        '''
        i = 0
        current = self.head
        res = None
        while current:
            if i == index:
                res = current.value
                break
            i += 1
            current = current.next
        return res


    def first(self):
        '''Return the head value'''
        return self.head.value

    def last(self):
        '''Return the tail value'''
        return self.tail.value

    @property
    def count(self):
        return self._count

    def _check_invariant(self):
        if self.count == 0:
            assert self.head is None and self.tail is None
        elif self.count == 1:
            assert self.head is self.tail
        else:
            assert self.head.prev is None and self.tail.next is None

    def dump(self):
        '''Get list current state'''
        if self.count == 0:
            return None

        output = ''
        current = self.head
        while current:
            output += repr(current)
            current = current.next

        return output
