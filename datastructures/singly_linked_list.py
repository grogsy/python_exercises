# All thats left to do is implement functions for getting first(head) and last(tail)

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
            self._count += 1
        else:
            self.head = Node(obj, self.head)
            self._count += 1

    def pop(self):
        """Removes the most recently inserted item and returns it"""
        res = self.head.value
        self.head = self.head.next
        self._count -= 1
        return res

    def remove(self, obj):
        """Finds a matching item and removes it from the list"""
        i = self.count() - 1
        cur = self.head
        while True:
            if cur.next.value == obj:
                # res = cur.next.value
                cur.next = cur.next.next
                self._count -= 1
                # return res
                # for some reason we will return the index at which the val is stored instead
                return i
            # Reached the tail
            elif cur.value is None:
                return -1
            cur = cur.next
            i -= 1

    def shift(self, obj):
        """Like push but places the value at the tail"""
        if not self.head:
            self.tail = Node(obj, None)
            self.head = self.tail
            self._count += 1
        else:
            cur = self.head
            while True:
                if cur is self.tail:
                    cur.next = Node(obj, None)
                    self.tail = cur.next
                    self._count += 1
                    break
                cur = cur.next

    def unshift(self):
        """Removes the item at tail and returns it"""
        if self.count() == 0:
            return None
        if self.count() == 1:
            res = self.head.value
            self.head = None
            self.tail = None
            self._count -= 1
            return res

        cur = self.head
        while True:
            if cur.next is self.tail:
                res = cur.next.value
                cur.next = None
                self.tail = cur
                self._count -= 1
                return res
            cur = cur.next

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
                raise IndexError
            if j == i:
                return cur.value

            j -= 1
            cur = cur.next

    def first(self):
        """Get the head value"""
        return self.head.value

    def last(self):
        """Get the tail value"""
        return self.tail.value

    def dump(self):
        """Get current list state"""
        if self.count() == 0:
            return "List currently empty"
        contents = []
        cur = self.head
        while True:
            if cur.next is None:
                contents.append(repr(cur.value))
                break
            else:
                contents.append(repr(cur.value))
            cur = cur.next
        return '->'.join(contents)

