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
        node = self.head
        while node:
            if obj == node.value:
                return node.value
            node = node.next
        return None

    def remove(self, obj):
        node = self.head
        while node:
            if node.value == obj:
                if node is self.head:
                    self.unshift()
                elif node is self.tail:
                    self.pop()
                else:
                    prev_node, next_node = node.prev, node.next
                    prev_node.next, next_node.prev = next_node, prev_node
                break
            node = node.next
        return None

    @property
    def count(self):
        node = self.head
        i = 0
        while node:
            i += 1
            node = node.next
        return i

    def __len__(self):
        return self.count

    def __bool__(self):
        return self.count > 0


class BucketList(LinkedList):
    def _get_id(self, bucket_id):
        node = self.head
        while node:
            bucket = node.value
            if bucket.id == bucket_id:
                return bucket
            node = node.next
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
        node = self.head
        while node:
            if node.key == key:
                return node.value
            node = node.next
        raise KeyError(key)

    def remove(self, key):
        node = self.head
        while node:
            if node.key == key:
                if node is self.head:
                    self.unshift()
                elif node is self.tail:
                    self.pop()
                else:
                    prev_node, next_node = node.prev, node.next
                    prev_node.next, next_node.prev = next_node, prev_node
                break
            node = node.next
        return None

    def __contains__(self, key):
        node = self.head
        while node:
            if key == node.key:
                return True
            node = node.next
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
        bucket = self.buckets.get(hashed_key)
        bucket.remove(key)

    def __contains__(self, key):
        hashed_key = self._naive_hash(key)
        bucket = self.buckets.get(hashed_key)
        return key in bucket

    def __bool__(self):
        return bool(self.buckets)

    def __len__(self):
        bucket_node = self.buckets.head
        i = 0
        while bucket_node:
            bucket = bucket_node.value
            i += len(bucket)
            bucket_node = bucket_node.next
        return i

    def __repr__(self):
        bucket_node = self.buckets.head
        output = '{'
        while bucket_node:
            bucket = bucket_node.value
            node = bucket.head
            while node:
                output += '%r: %r, '% (node.key, node.value)
                node = node.next
            bucket_node = bucket_node.next
        output = output[:-2]
        output += '}'
        return output

