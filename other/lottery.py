'''
Inspired by the tombola example from Fluent Python
'''


import random


class LotteryBox:
    def __init__(self):
        self.seed = [random.randint(1, 1000) for _ in range(10000)]
        
        
    def __call__(self):
        return self.seed.pop(random.choice(range(len(self.seed))))
