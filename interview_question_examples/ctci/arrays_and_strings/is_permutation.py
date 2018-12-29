# ctci 1.2


# Using python things

from collections import Counter

class CounterPermutationChecker(Counter):
    def __eq__(self, other):
        return all(self[counter] == other[other_counter]
                   for counter, other_counter in zip(sorted(self.keys()), sorted(other.keys())))
