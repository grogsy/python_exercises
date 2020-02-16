# https://leetcode.com/problems/remove-outermost-parentheses/

def removeOuterParentheses(S):
    paren_count = 0
    output = []

    for char in S:
        if char == '(':
            paren_count += 1
            if paren_count != 1:
               output.append(char) 
        if char == ')':
            paren_count -= 1
            if paren_count != 0:
                output.append(char)

    return ''.join(output)
