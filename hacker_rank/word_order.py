# Problem desc: https://www.hackerrank.com/challenges/word-order/problem

from collections import OrderedDict

num = int(input())
word_count = OrderedDict()

for _ in range(num):
    word = str(input())
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1
        
unique_words = list(word_count.keys())
occurrences = []

for value in word_count.values():
    occurrences.append(str(value))
    
print(len(unique_words))
print(' '.join(occurrences))
