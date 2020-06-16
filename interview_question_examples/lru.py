# https://leetcode.com/problems/lru-cache/

# class LRUCache:

#     def __init__(self, capacity: int):
#         self.cache = {}
#         self.queue = []
#         self.cap = capacity

#     def get(self, key: int) -> int:
#         val = self.cache.get(key, -1)
        
#         if val >= 0:
#             for i, k in enumerate(self.queue):
#                 if k == key:
#                     self.queue.pop(i)
#                     self.queue.append(k)
#                     break
        
#         return val
        
#     def put(self, key: int, value: int) -> None:
#         if key in self.cache:
#             self.cache[key] = value
#             for i, k in enumerate(self.queue):
#                 if k == key:
#                     self.queue.pop(i)
#                     break
#         elif len(self.cache) >= self.cap:
#             least = self.queue.pop(0)
#             del self.cache[least]
        
#         self.queue.append(key)
#         self.cache[key] = value

# using OrderedDict

from collections import OrderedDict

class LRUCache:
    def __init__(self, capacity):
        self.cache = OrderedDict()
        self.cap = capacity
        
    def get(self, key):
        val = self.cache.get(key, -1)
        if val >= 0:
            del self.cache[key]
            self.cache[key] = val
            
        return val
    
    def put(self, key, value):
        if key in self.cache:
            del self.cache[key]
        elif len(self.cache) >= self.cap:
            self.cache.popitem(last=False)

        self.cache[key] = value
