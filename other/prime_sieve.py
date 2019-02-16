'''Implementation of Eratosthenes prime sieve
    Gives all primes from 2 to a given number'''

def sieve(high):
    table = {i: True for i in range(2, high)}
    for i in range(2, high):
        if table[i]:
            k = 0
            j = i**2 + (i*k)
            while j < high:
                table[j] = False
                k += 1
                j = i**2 + (i*k)
    return [num for num in table if table[num]]


# This works(faster?) too
def sieve2(n):
    table = {i: True for i in range(2, n)}
    
    for i in range(2, n):
        if table[i]:
            for j in range(2, n+1):
                if i * j > len(table):
                    break
                table[i * j] = False

    return [num for num in table if table[num]]
            

if __name__ == '__main__':
    import sys
    print(sieve(int(sys.argv[1])))
