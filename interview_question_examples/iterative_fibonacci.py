def fib(N):
    prev = 0
    accumulation = 1

    for _ in range(1, N):
        accumulation += prev
        prev = accumulation - prev

    return accumulation
