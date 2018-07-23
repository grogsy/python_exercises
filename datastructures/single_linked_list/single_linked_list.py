'''
old implementation: last val<-n<-...<-4<-3<-2<-first val

new implementation: first val<-2<-3<-4<-...<-n<-last val

In the first implementation the 0-th index was on the right side of the list
and the max index would be on the left side. This was due to a confusing
interpretation of the spec to implement the sll. For example in the old version,
pushing a value into the list would push all existing values to the right,
similarly to how list.insert(value, 0) works, and that can be really confusing.
If anything, it should be more like list.append(value)

This implementation attempts to remedy confusion by making the the leftmost value
the 0th index and the rightmost index to be the max-index, as is with
conventional array/list-based structures. The methods should still work
fundamentally the same way as the old version; theyre more or less the same thing.
The only real difference is that this new implementation reconciles the chosen
vocabulary for the method names; using and reading the code for the methods should
seem more intuitive now and less confusing. Its less of a pain in the ass.
'''


class Node:
    '''Node'''
    def __init__(self, value, nxt):
        self.value = value
        self.next = nxt

    def __repr__(self):
        # Better using ternary operator and makes more sense to read too
        next_val = self.next.value if self.next else None
        return f"[{self.value}:{repr(next_val)}]"


class SingleLinkedList:
    '''Single-Linked-List'''
    def __init__(self):
        self.head = None
        self.tail = None
        self._count = 0

    def push(self, obj):
        '''Place item at tail, extending the list'''
        if not self.head:
            self.head = Node(obj, None)
            self.tail = self.head
        else:
            # This set of operations does not
            # dereference the current tail.
            # The name "self.tail" now simply
            # points to the whatever value is
            # contained in self.tail.next.
            self.tail.next = Node(obj, None)
            self.tail = self.tail.next
        self._count += 1

    def shift(self, obj):
        '''Place item at head shifting everything else to the right'''
        if not self.head:
            self.head = Node(obj, None)
            self.tail = self.head
        else:
            current_head = self.head
            self.head = Node(obj, current_head)
        self._count += 1

    def pop(self):
        '''Remove the current tail and return its value'''
        if self.count == 0:
            res = None
        if self.count == 1:
            res = self.head.value
            self.head = self.tail = None
        else:
            current = self.head
            prev = None
            while current:
                if current is self.tail:
                    res = current.value
                    prev.next = None
                    self.tail = prev
                    break
                prev = current
                current = current.next
        self._count -= 1
        return res

    def unshift(self):
        '''Remove the current head and return its value'''
        if self.count == 0:
            res = None
        else:
            res = self.head.value
            self.head = self.head.next
        self._count -= 1
        return res

    def remove(self, obj):
        '''Finds a matching item and removes it from the list. Returns it's index'''
        i = 0
        current = self.head
        prev = None
        while current:
            if current.value == obj:
                if not prev:
                    self.head = current.next
                else:
                    prev.next = current.next
                self._count -= 1
                break
            elif current.next is None:
                i = -1
                break
            prev = current
            current = current.next
            i += 1
        return i

    def get(self, index):
        '''Get the value at a given index'''
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
        '''Return the value at the 0-th index'''
        return self.head.value

    def last(self):
        '''Return the value at the max index'''
        return self.tail.value

    @property
    def count(self):
        '''Get the length of the list'''
        return self._count

    def dump(self):
        '''Get the list's current state'''
        if self.count == 0:
            return None
        output = ''
        current = self.head
        while current:
            if current.next is None:
                output += current.value
                break
            else:
                output += current.value
                output += '->'
            current = current.next
        return output

    def __repr__(self):
        output = self.dump()
        return output
