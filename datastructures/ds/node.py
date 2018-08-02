class SingleLinkedNode:
    '''Node'''
    def __init__(self, value, nxt):
        self.value = value
        self.next = nxt

    def __repr__(self):
        # Better using ternary operator and makes more sense to read too
        next_val = self.next.value if self.next else None
        return f"[{self.value}:{repr(next_val)}]"

class DoubleLinkedNode:
    def __init__(self, value, prev, nxt):
        self.value = value
        self.prev = prev
        self.next = nxt

    def __repr__(self):
        prev_val = self.prev.value if self.prev else None
        next_val = self.next.value if self.next else None

        return f"[{prev_val}:{self.value}:{next_val}]"
