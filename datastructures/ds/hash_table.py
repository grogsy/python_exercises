'''Python hash table that acts like built-in dict using only linked lists'''
from .node import DoubleLinkedNode as Node

class HashNode(Node):
    def __init__(self, key, **kwargs):
        super().__init__(**kwargs)
        self.key = key


class LinkedList:
    def __init__(self):
        self._node = Node
        self.head = self.tail = None

    def _reset(self):
        self.head = self.tail = None

    def _init_insert(self, value):
        self.head = self.tail = self._node(value, prev=None, nxt=None)

    def push(self, value):
        if not self.head:
            self._init_insert(value)
        else:
            self.tail = self._node(value, prev=self.tail, nxt=None)
            self.tail.prev.next = self.tail

    def pop(self):
        node = self.tail
        self.tail = node.prev
        try:
            self.tail.next = None
        except AttributeError:
            self._reset()

    def unshift(self):
        node = self.head
        self.head = node.next
        try:
            self.head.prev = None
        except AttributeError:
            self._reset()

    def get(self, obj):
        for node in self:
            if obj == node.value:
                return node.value
        return None

    def remove(self, obj):
        for node in self:
            if node.value == obj:
                if node is self.head:
                    self.unshift()
                elif node is self.tail:
                    self.pop()
                else:
                    prev_node, next_node = node.prev, node.next
                    prev_node.next, next_node.prev = next_node, prev_node
                break
        return None

    @property
    def count(self):
        i = 0
        for node in self:
            i += 1
        return i

    # Implementing iterator for control structure makes coding and reading
    # easier
    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = next(node)
        return

    def __len__(self):
        return self.count

    def __bool__(self):
        return self.count > 0


class BucketList(LinkedList):
    '''A linked-list that holds other linked-lists(buckets)'''
    def _get_id(self, bucket_id):
        for bucket_node in self:
            bucket = bucket_node.value
            if bucket.id == bucket_id:
                return bucket
        return None

    def get(self, bucket_id):
        bucket = self._get_id(bucket_id)
        if not bucket:
            raise NoBucket
        return bucket


class Bucket(LinkedList):
    def __init__(self, bucket_id=None):
        super().__init__()
        self.id = bucket_id
        self._node = HashNode

    def _init_insert(self, key, value):
        self.head = self.tail = self._node(key=key, value=value, prev=None, nxt=None)

    def push(self, key, value):
        if not self.head:
            self._init_insert(key, value)
        else:
            self.tail = self._node(key=key, value=value, prev=self.tail, nxt=None)
            self.tail.prev.next = self.tail

    def get(self, key):
        for node in self:
            if node.key == key:
                return node.value
        raise KeyError(key)

    def remove(self, key):
        for node in self:
            if node.key == key:
                if node is self.head:
                    self.unshift()
                elif node is self.tail:
                    self.pop()
                else:
                    prev_node, next_node = node.prev, node.next
                    prev_node.next, next_node.prev = next_node, prev_node
                break
        return None

    def __contains__(self, key):
        for node in self:
            if key == node.key:
                return True
        return False


class NoBucket(KeyError):
    pass


class HashTable:
    def __init__(self):
        self.buckets = BucketList()

    def get(self, key, default=None):
        hashed_key = self._naive_hash(key)
        try:
            bucket = self.buckets.get(hashed_key)
            out = bucket.get(key)
        except KeyError:
            return default
        return out

    def items(self):
        for bucket_node in self.buckets:
            bucket = bucket_node.value
            for node in bucket:
                yield (node.key, node.value)

    def keys(self):
        for key, _ in self.items():
            yield key

    def values(self):
        for _, value in self.items():
            yield value

    def _naive_hash(self, key):
        return sum((ord(c)*7**i) for i, c in enumerate(str(key), 1)) % 257

    def __setitem__(self, key, value):
        hashed_key = self._naive_hash(key)
        try:
            bucket = self.buckets.get(hashed_key)
            if key in bucket:
                bucket.remove(key)
            bucket.push(key, value)
        except NoBucket:
            new_bucket = Bucket(bucket_id=hashed_key)
            new_bucket.push(key, value)
            self.buckets.push(new_bucket)

    def __getitem__(self, key):
        hashed_key = self._naive_hash(key)
        try:
            bucket = self.buckets.get(hashed_key)
        except KeyError:
            return "KeyError: %s" % key
        return bucket.get(key)

    def __delitem__(self, key):
        hashed_key = self._naive_hash(key)
        try:
            bucket = self.buckets.get(hashed_key)
        except KeyError:
            return "KeyError: %s" % key
        bucket.remove(key)

    def __contains__(self, key):
        hashed_key = self._naive_hash(key)
        try:
            bucket = self.buckets.get(hashed_key)
        except NoBucket:
            return False
        return key in bucket

    def __bool__(self):
        return bool(self.buckets)

    def __len__(self):
        bucket_node = self.buckets.head
        i = 0
        for bucket_node in self.buckets:
            bucket = bucket_node.value
            i += len(bucket)
        return i

    def __iter__(self):
        for bucket_node in self.buckets:
            bucket = bucket_node.value
            for node in bucket:
                yield node.key

    def __repr__(self):
        bucket_node = self.buckets.head
        output = '{'
        for bucket_node in self.buckets:
            bucket = bucket_node.value
            for node in bucket:
                output += '%r: %r, ' % (node.key, node.value)
        output = output[:-2]
        output += '}'
        return output
