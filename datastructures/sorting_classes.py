'''sorting algorithms implemented as a class'''

class SortAlgorithm:

    @staticmethod
    def check_valid_input(arr):
        '''helper function'''
        assert hasattr(arr, '__iter__')
        assert all(isinstance(element, type(arr[0])) for element in arr)


    def sort(self, arr):
        '''base sort method, all sorting methods should return a new array object'''
        raise NotImplementedError


    def __call__(self, arr):
        try:
            SortAlgorithm.check_valid_input(arr)
        except AssertionError:
            return "Can't perform sort: Either arg is not iterable(does not have __iter__ method) or not all items of arg are of the same type"

        return self.sort(arr)

class InsertionSort(SortAlgorithm):
    '''Insertion Sort'''
    def sort(self, arr):
        i = 0
        while i < len(arr):
            j = i
            while j > 0 and arr[j-1] > arr[j]:
                arr[j], arr[j-1] = arr[j-1], arr[j]
                j -= 1
            i += 1

        return arr

from random import choice
a = [choice(range(1000)) for _ in range(30)]

print("Before: ", a)
insertion_sort = InsertionSort()
print("After: ", insertion_sort(a))
