def is_palindrome(word):
    word = word.lower()
    left = 0
    right = len(word)-1
    while left <= right:
        if word[left] != word[right]:
            return False
        left += 1
        right -= 1
    return True
    
# with python sequence slicing
def is_pali(word):
    word = word.lower()
    return word == word[::-1]
