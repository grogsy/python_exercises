def digital_root(n):
    def digits(n):
        return [int(i) for i in list(str(n))]
        
    dig_sum = sum(digits(n))
    if len(digits(dig_sum)) == 1:
        return dig_sum
    
    return digital_root(dig_sum)
