def fib(n):
    prev = 0
    s = 1
    
    for _ in range(n):
        s += prev
        prev = s - prev
        print(s)
