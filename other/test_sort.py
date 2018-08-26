from merge_sort import sort
from random import choice

def test_sort(amt=100):
    for _ in range(amt):
        length = choice(range(100,10000))
        arr = [choice(range(10000)) for _ in range(length)]
        assert sort(arr) == sorted(arr)
test_sort()
