import random

def binsearch(arr, target):
    return _binsearch(0, len(arr), arr, target)

def _binsearch(start, end, arr, target):

    midpoint = (end + start) // 2   

    if arr[midpoint] == target:
        return midpoint
    elif arr[midpoint] < target:
        return binsearch(midpoint, end, arr, target)
    elif arr[midpoint] > target:
        return binsearch(start, midpoint, arr, target)
        
        
arr = sorted([random.randint(1, 10000) for _ in range(40)])
print(arr)

target = random.choice(arr)

print(binsearch(arr, target))
