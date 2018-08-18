'''Implementation of Eratosthenes prime sieve
    Gives all primes from 2 to a given number'''

def sieve(high):
    table = {i: True for i in range(high)}
    for i in range(2, high):
        if table[i]:
            k = 0
            j = i**2 + (i*k)
            while j < high:
                j = i**2 + (i*k)
                table[j] = False
                k += 1
    return [num for num in table if table[num]]

sieve(121)
