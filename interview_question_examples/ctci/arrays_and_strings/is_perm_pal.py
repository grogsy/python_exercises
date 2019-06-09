def is_perm_pal(string):
    odds = [char for char in string if string.count(char) % 2 == 1]
    
    return True if len(odds) <= 1 else False
