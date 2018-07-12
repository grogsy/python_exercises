def fizzbuzz(n):
    res = ''
    if n % 3 == 0 or n % 5 == 0:
        if n % 3 == 0:
            res += 'Fizz'
        if n % 5 == 0:
            res += 'Buzz'
    else:
        res += str(n)
    return res
for i in range(1, 100):
    print(fizzbuzz(i))
