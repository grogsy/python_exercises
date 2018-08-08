'''Put in debug statements to help understand whats happening'''
def memoize(f):
    memo = {}
    def helper(x):
        input('In helper function for fib(%d)' % x)
        if x not in memo:
            input('%d not in memo. Setting memo[%d] = fib(%d)' % (x, x, x))
            input('Calling fib(%d):\n\n' % x)
            memo[x] = f(x)
            input('memo[%d] set to %d\n\n' % (x, memo[x]))
        else:
            input('fib(%d) in memo already as memo[%d] = %d\n\n' % (x, x, memo[x]))

        return memo[x]
    return helper


def fib(n):
    input('In function fib(%d)' % n)
    if n == 0:
        input('Reached 0. Going up')
        return 0
    elif n == 1:
        input('Reached 1. Going up')
        return 1
    else:
        input('Calculating fib(%d) + fib(%d)' % (n-1, n-2))

        input('First calling fib(%d)\n\n' % (n-1))
        f1 = fib(n-1)
        input('Calculating fib(%d) done. Back in fib(%d). Now calling fib(%d)\n\n' % (n-1, n, n-2))

        f2 = fib(n-2)
        input('Calculating fib(%d) done. Back in fib(%d) with fib(%d)=%d, and fib(%d)=%d. Therefore, fib(%d) + fib(%d) = %d' % (n-2, n, n-1, f1, n-2, f2, n-1, n-2, f1+f2))

        input('Finished with fib(%d). Setting memo[%d] = %d' % (n, n, f1+f2))
        return f1 + f2

fib = memoize(fib)
fib(10)
