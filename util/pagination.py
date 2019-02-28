'''bare pagination mechanism i might use in the future'''

class PaginationContext:
    def __init__(self, iterable, size):
        self.iterable = self.make_chunks(iterable, size)
        self.max_size = len(self.iterable)
        self.current_index = 1 
        
    def make_chunks(self, iterable, size):
        return [iterable[x:x+size] for x in range(0, len(iterable), size)]
    
    @property
    def current(self):
        return self.iterable[self.current_index - 1]
    
    def __call__(self):
        return self.current
    
    @property
    def has_next(self):
        return self.current_index < self.max_size
    
    @property
    def has_prev(self):
        return self.current_index > 1
    
    @property
    def next_num(self):
        if not self.has_next:
            return "No next number"
        return self.current_index + 1
    
    @property
    def prev_num(self):
        if not self.has_prev:
            return "Already at 1"
        return self.current_index - 1
    
    # maybe don't use this yet
    def get(self):
        if self.current_index >= self.max_size or self.current_index < 1:
            return []
        else:
            return self.iterable[self.current_index-1]
        
    def get_next(self):
        if not self.has_next:
            return []
        res = self.iterable[self.next_num]
        self.current_index += 1
        return res
    
    def get_prev(self):
        if not self.has_prev:
            return []
        res = self.iterable[self.prev_num]
        self.current_index -= 1
        return res
    
    def __repr__(self):
        return str(self.iterable[self.current_index - 1])

