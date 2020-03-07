# https://leetcode.com/problems/sort-integers-by-the-number-of-1-bits

from collections import defaultdict

def sortByBits(arr):
    d = defaultdict(list)
    count = lambda num: bin(num).count('1')
    for num in arr:
        d[count(num)].append(num)

    output = []
    for c in sorted(d.keys()):
        output += sorted(d[c])

    return output
