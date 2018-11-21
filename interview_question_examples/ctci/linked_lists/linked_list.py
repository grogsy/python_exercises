class Node:
    '''Implementation without a linked list controller'''
    def __init__(self, data):
        self.data = data
        self.next = None

    def append(self, data):
        end = Node(data)
        node = self
        while node.next is not None:
            node = node.next

        node.next = end

    def delete(self, data):
        node = self

        # head case
        if self.data == data:
            if self.count() > 1:
                self.data = self.next.data
                self.next = self.next.next
                return self
            else:
                return "Cannot delete head, no implementation for Node containing None"

        while node.next is not None:
            if node.next.data == data:
                node.next = node.next.next
                return self
            node = node.next

        return self

    def count(self):
        node = self
        if not self or self.data is None:
            return 0
        count = 1
        while node.next is not None:
            count += 1
            node = node.next

        return count

    def __repr__(self):
        next_val = self.next.data if self.next else None
        return "Node<data:{0} next:{1}>".format(self.data, next_val)
