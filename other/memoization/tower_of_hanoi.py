# This example(and other recursive examples in general) seem to benefit from memoization

def hanoi(n):
    '''calculate the number of moves it costs to move disks among three needles in such a way that larger disks cannot be placed on top of smaller disks'''
    if n == 0:
        return 0
    else:
        return 2 * hanoi(n-1) + 1
