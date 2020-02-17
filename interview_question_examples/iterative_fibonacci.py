def fib(N):
    prev = 1
    accumulation = 0

    for _ in range(1, N + 1):
        accumulation += prev
        prev = accumulation - prev

    return accumulation
