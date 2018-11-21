'''
1 is not a prime
All primes except 2 are odd
All primes greater than 3 can be written in the form 6*k +/- 1
For any number n, there is only one prime facter greater than root(n)
The consequence for prime testing n this way is: if we cannot find
an integer f less than or equal to root(n) that divides n, then n is prime
'''


from math import floor, sqrt

def is_prime(n):
    if n is 2 or n is 3:
        return True
    if n is 1 or n % 2 == 0 or n % 3== 0:
        return False
    if n < 9:
        return True
    else:
        r = floor(sqrt(n))
        f = 5
        while f <= r:
            if n % f == 0 or n % (f+2) == 0:
                return False
            f = f+6
        return True
