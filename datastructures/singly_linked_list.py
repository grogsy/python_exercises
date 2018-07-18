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
            return
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
        cur = self.head
        while True:
            if cur.next.value == obj:
                res = cur.next.value
                cur.next = cur.next.next
                self._count -= 1
                return res
            # Reached the tail
            elif cur.value is None:
                return -1
            cur = cur.next

    def unshift(self):
        """Removes the item at tail and returns it"""
        if self.count() == 1:
            return "Cannot unshift if there is only one item in the list"
        cur = self.head
        while True:
            if cur.next is self.tail:
                res = self.tail
                cur.next = None
                self.tail = cur
                self._count -= 1
                return res
            cur = cur.next

    def count(self):
        """Count the number of elements in the list"""
        return self._count

    def get(self, i):
        """Get the value at a given index"""


    def dump(self):
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

