# https://leetcode.com/problems/generate-parentheses/submissions/

def generate_parenthesis(n):
    braces = []
    def _generate_parenthesis(l_count, r_count, brace):
        def _generate_parenthesis(l_count, r_count, brace):
            if l_count < 0 or r_count < 0 or l_count > r_count:
                return 
            if l_count == 0 and r_count == 0:
                braces.append(brace)
                return
            _generate_parenthesis(l_count - 1, r_count, brace + '(')
            _generate_parenthesis(l_count, r_count - 1, brace + ')')

    _generate_parenthesis(n, n, '')
        
    return braces
