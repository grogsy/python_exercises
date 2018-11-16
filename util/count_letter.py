# or just use collections.Counter

def count_letters(string):
    return {c: string.count(c) for c in set(string)}
