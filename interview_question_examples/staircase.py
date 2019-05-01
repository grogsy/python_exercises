def staircase(n):
    rjust = n

    for i in range(1, n+1):
        out = '#' * i
        print(out.rjust(rjust, ' '))
        
        
def st2(n):
    '''a solution that doesn't use rjust. useful for implementing in a diff language'''
    rjust = n
    
    mark = 1
    padding = rjust - 1
    
    j = 0
    while j < rjust:
        out = ''
        out += (' ' * padding)
        out += ('#' * mark)
        padding -= 1
        mark += 1
        j += 1
        print(out)
