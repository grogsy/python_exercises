# CtCi problem 1.1

def is_unique(string):
    '''test if all characters are unique, i.e. the string does not have duplicate characters'''
    for i, c in enumerate(string):
        for j in range(i+1, len(string)):
            if c == string[j]:
                return False
