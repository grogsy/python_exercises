# https://www.hackerrank.com/challenges/anagram/problem

def anagram(s):
    if len(s) % 2 == 1:
        return -1
    
    # get first half of string
    a = s[:len(s)//2]
    
    # get latter half of string
    b = s[len(s)//2:]

    change_count = 0
    counter = {letter: 0 for letter in 'abcdefghijklmnopqrstuvwxyz'}

    for letter in a:
        counter[letter] += 1
    
    for letter in b:
        counter[letter] -= 1
        if counter[letter] < 0:
            change_count += 1

    return change_count
