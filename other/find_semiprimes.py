from prime_sieve import sieve


def get_semiprimes(n):
    '''find all possible semiprime numbers up n'''

    primes = sieve(n)

    semiprimes = []

    for i in range(len(primes)):
        for j in range(i, len(primes)):
            semiprimes.append(primes[i]*primes[j])

    return semiprimes

if __name__ == '__main__':
    import sys
    print(get_semiprimes(int(sys.argv[1])))
