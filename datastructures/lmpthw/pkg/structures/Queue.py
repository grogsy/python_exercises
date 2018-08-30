'''
Along with implementing this as a child class of DoubleLinkedList, should consider
defining it's __slots__ to = 'shift', 'unshift', 'count', 'dump', 'empty'
(maybe have dll define an empty property?)

Another thing to keep in mind is that the dll implements shift differently;
that is, dll.shift() places nodes to the head of the list, whereas
queue.shift() places those elements in the back of the list.

Summary of changes to make:
    -Consider making Queue inherit from DoubleLinkedList
    -Remove unshift() method from Queue as it is the same as DLL unshift()
    -Remove count() property from Queue() as it is the smae as DLL count()
    -Consider making the empty property of Queue a property of DLL instead
     because it would be useful to DLL as well
    -Implement __slots__ for Queue and hope that I'm doing it right

'''
from .node import DoubleLinkedNode as Node
#from .double_linked_list import DoubleLinkedList

class QueueFull(BaseException):
    '''raised by instances of Queue() if the user defines a max length'''
    pass

class Queue:
    '''uppercase module and class because 'queue' already exists'''

    #__slots__ = 'shift', 'unshift', 'count', 'dump', 'empty'

    def __init__(self, m=None):
        self.head = self.tail = None
        self.max = m

    def shift(self, value):
        '''push a value to the back of the queue. Different from DoubleLinkedList.shift()
           If anything, functionally similar to DoubleLinkedList.push()'''
        if self.max and self.count == self.max:
            raise QueueFull
            #return "Queue full"
        if not self.head:
            self.head = Node(value, prev=None, nxt=None)
            self.tail = self.head
        else:
            prev_tail, self.tail = self.tail, Node(value, prev=self.tail, nxt=None)
            prev_tail.next = self.tail

    def unshift(self):
        '''remove the current front of queue and return its value'''
        if not self.head and not self.tail:
            return None

        res = self.head.value
        self.head = self.head.next
        try:
            self.head.prev = None
        except AttributeError:
            self.head = self.tail = None

        return res

    def dump(self):
        '''debug function'''
        node = self.head
        output = '|--Front--| '
        while node:
            output += repr(node)
            node = node.next
        output += ' |--Back--|'
        return output

    @property
    def count(self):
        '''slow count'''
        node = self.head
        i = 0
        while node:
            i += 1
            node = node.next
        return i

    @property
    def empty(self):
        '''do we contain elements or not'''
        return self.count == 0
