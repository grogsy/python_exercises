// https://leetcode.com/problems/letter-combinations-of-a-phone-number/
 
_m = {
    1: '',
    2: 'abc',
    3: 'def',
    4: 'ghi',
    5: 'jkl',
    6: 'mno',
    7: 'pqrs',
    8: 'tuv',
    9: 'wxyz',
    0: ''
}

m = lambda d: _m[int(d)]

def recurse(solutions, remaining_digits):
    if not remaining_digits:
        return solutions
    
    output = []
    current_digit = remaining_digits[0]
    for comb in solutions:
        for ch in m(current_digit):
            output.append(comb + ch)
    
    return recurse(output, remaining_digits[1:])

def letterCombinations(digits):
    if not digits:
        return []
    
    output = [letter for letter in m(digits[0])]
    
    return recurse(output, digits[1:])
