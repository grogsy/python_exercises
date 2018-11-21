# https://www.hackerrank.com/challenges/capitalize/problem
def solve(s):
    res = []
    inseq = False
    for c in s:
        if not inseq and c.isalnum():
            res.append(c.capitalize())
            inseq = True
        elif c == " ":
            inseq = False
            res.append(c)
        else:
            res.append(c)
        
    return ''.join(res)
            
        
