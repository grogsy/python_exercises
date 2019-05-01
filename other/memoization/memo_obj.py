'''memoization/decorating a function as an object instance'''

class memoize:
    def __init__(self, func):
        self.func = func
        self.cache = {}
        
    def __call__(self, arg):
        if value in self.cache:
            return self.cache[arg]
        
        res = self.func(arg)
        self.cache[arg] = res
        return res


def fib(n):
    if n <= 1:
        return 1
    
    return fib(n - 1) + fib(n - 2)
    

fib = memoize(fib)

print(fib(40))
