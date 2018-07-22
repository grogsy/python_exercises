'''Attempt to implement Single Linked List without using built-in structures
   Commented out code is my interpretation of the implementation
   Actual code surrounding my commented out code is the desired specification
   for implementing the single linked list.
'''

class Node:
    def __init__(self, value, nxt):
        self.value = value
        self.next = nxt

    def __repr__(self):
                  # Using 'and' in conjunction with 2 truthy values
                  # always evaluates to the latter value
        next_val = self.next and self.next.value or None
        return f"[{self.value}:{repr(next_val)}]"


class SingleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self._count = 0

    def push(self, obj):
        """Appends a new value to the head of the list"""
        if not self.head:
            self.tail = Node(obj, None)
            self.head = self.tail
        else:
            self.head = Node(obj, self.head)
        self._count += 1

    def pop(self):
        """Removes the head and returns it"""
        # Alternatively, can test if self.head is None:
        if self.count() == 0:
            res = None
        else:
            res = self.head.value
            self.head = self.head.next
        self._count -= 1
        return res

    def remove(self, obj):
        """Finds a matching item and removes it from the list"""
        # Tail is the 0th index
        i = self.count() - 1
        cur = self.head
        prev = None
        while cur:
            if cur.value == obj:
                if not prev:
                    self.head = cur.next
                else:
                    prev.next = cur.next
                break
            # Reached the tail
            elif cur.value is None:
                return -1
            prev = cur
            cur = cur.next
            i -= 1
        self._count -= 1
        return i

    def shift(self, obj):
        """Like push but places the value at the tail"""
        if not self.head:
            self.tail = Node(obj, None)
            self.head = self.tail
        else:
            self.tail.next = Node(obj, None)
            self.tail = self.tail.next
        self._count += 1

    def unshift(self):
        """Removes the item at tail and returns it"""
        if self.count() == 0:
            res = None
        if self.count() == 1:
            res = self.head.value
            self.head = None
            self.tail = None
        else:
            cur = self.head
            prev = None
            while cur:
                if cur is self.tail:
                    res = cur.value
                    prev.next = None
                    self.tail = prev
                    break
                prev = cur
                cur = cur.next
        self._count -= 1
        return res

    # Turn this into a property
    def count(self):
        """Count the number of elements in the list"""
        return self._count

    def get(self, i):
        """Get the value at a given index"""
        # zero-based index
        # Also so for this implementation, we consider the tail to be the 0th index..
        j = self.count() - 1
        cur = self.head
        while True:
            # Reached the end of the list
            if j < 0:
                # raise IndexError
                return None
            if j == i:
                return cur.value
            j -= 1
            cur = cur.next

    def first(self):
        """Get the left-most(tail) value"""
        # very confusing
        # One way to interpret it better is to think of
        # The tail as the 0-th(first) item
        return self.tail.value

    def last(self):
        """Get the right-most(head) value"""
        # And the head to be the highest-indexed item
        return self.head.value

    def dump(self):
        """Get current list state"""
        if self.count() == 0:
            return "List currently empty"
        cur = self.head
        while cur:
            if cur is self.tail:
                print(cur.value)
            else:
                print(cur.value, end='->')

            '''if cur.next is None:
                contents.append(repr(cur.value))
                break
            else:
                contents.append(repr(cur.value))
            cur = cur.next
        return '->'.join(contents)''' # trying to use no built-ins data structures here

