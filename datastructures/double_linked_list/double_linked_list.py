class Node:
    def __init__(self, prev, value, nxt):
        self.prev = prev
        self.value = value
        self.next = nxt

    def __repr__(self):
        prev_val = self.prev.value if self.prev else None
        next_val = self.next.value if self.next else None

        return f"[{prev_val}:{self.value}:{next_val}]"


class DoubleLinkedList:
    def __init__(self):
        self.head = self.tail = None
        self._count = 0

    def push(self, obj):
        '''Place a node at the tail of the list'''
        if not self.head:
            self.head = self.tail = Node(None, obj, None)
        else:
            current_tail = self.tail
            self.tail = Node(current_tail, obj, None)
            current_tail.next = self.tail
        self._count += 1

    def shift(self, obj):
        '''Place a node at the head of the list'''
        if not self.head:
            self.head = self.tail = Node(None, obj, None)
        else:
            current_head = self.head
            self.head = Node(None, obj, current_head)
            current_head.prev = self.head
        self._count += 1

    def pop(self):
        '''Remove current node at the tail and return its value'''
        if not self.tail or not self.head:
            return None
        res = self.tail.value
        if self.count == 1:
            self.head = self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None

        self._count -= 1
        return res

    def unshift(self):
        '''Remove current node at head and return its value'''
        if not self.head or not self.tail:
            return None
        res = self.head.value
        if self.count == 1:
            self.head = self.tail = None
        else:
            res = self.head.value
            self.head = self.head.next
            self.head.prev = None

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
                    current.prev.next = current.next
                    self._count -= 1
                return i
            current = current.next
            i += 1

    def get(self, index):
        '''Get the value of the node at the given index.
        Returns None if value isn't in any of the nodes'''
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
