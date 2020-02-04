# https://leetcode.com/problems/excel-sheet-column-number/submissions/

def titleToNumber(s):
    output = 0
    weight = len(s) - 1

    for char in s:
        output += (ord(char) - 64) * (26 ** weight)
        weight -= 1

    return output
