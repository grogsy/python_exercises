# ctci 1.2


# Using python things

from collections import Counter

class CounterPermutationChecker(Counter):
    def __eq__(self, other):
        return all(self[counter] == other[other_counter]
                   for counter, other_counter in zip(sorted(self.keys()), sorted(other.keys())))
    
# woops there's actually a much simple approach
def is_permutation(word1, word2):
    return sorted(word1) == sorted(word2)
