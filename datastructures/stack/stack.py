class Node:
    def __init__(self, value, nxt):
        self.value = value
        self.next = nxt

class Stack:
    def __init__(self):
        self.top = None

    def push(self, obj):
        '''Pushes a new value to the top of the stack'''
        if not self.top:
            self.top = Node(obj, None)
        else:
            self.top = Node(obj, self.top)

    def pop(self):
        '''Removes the current top of the stack'''
        if not self.top:
            return None
        else:
            value = self.top.value
            self.top = self.top.next
            return value

    def count(self):
        node = self.top
        i = 0
        while node:
            i += 1
            node = node.next
        return i

    def dump(self):
        output = ''
        node = self.top
        while node:
            value = node.value
            if not node.next:
                output += value
                break
            output += '%s->' % value
            node = node.next
        return output
