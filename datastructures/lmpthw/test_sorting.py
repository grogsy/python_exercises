from random import choice
from pkg.structures.double_linked_list import DoubleLinkedList as Array

# Try to make all the sorting functions return a new object
# instead of modifying the existing one
def test_sort(sort_func):
    for _ in range(500):
        length = choice(range(10, 100))
        arr = Array()
        for _ in range(length):
            arr.push(choice(range(10000)))
        sorted_arr = sort_func(arr)
        for node in sorted_arr:
            nxt  = node.next
            prev = node.prev
            try:
                assert prev.value <= node.value <= nxt.value
            except (TypeError, AttributeError):
                try:
                    # Is it the head?
                    assert node.value <= nxt.value
                except (TypeError, AttributeError):
                    # Must be the tail
                    assert prev.value <= node.value



def test_bubblesort():
    from pkg.sorts.bubblesort import sort
    test_sort(sort)


def test_bubblesort2():
    from pkg.sorts.bubblesort2 import sort
    test_sort(sort)


def test_mergesort():
    from pkg.sorts.merge_sort import merge_sort
    test_sort(merge_sort)

def test_quicksort():
    from pkg.sorts.quicksort import quicksort
    test_sort(quicksort)

def test_quicksort2():
    from pkg.sorts.hoare_quicksort import quicksort
    test_sort(quicksort)

def test_insertion_sort():
    from pkg.sorts.insertion_sort import insertion_sort
    test_sort(insertion_sort)

if __name__ == '__main__':
    #test_bubblesort()
    #test_bubblesort2()
    #test_mergesort()
    test_quicksort()
    #test_quicksort2()
    #test_insertion_sort()
#if __name__ == '__main__':
#    import timeit
#    amt = 500
#    fmt = '{:>15}: {}'
#    print(fmt.format('quicksort', timeit.timeit("test_quicksort()", setup="from __main__ import test_quicksort", number=amt)))
#    print(fmt.format('hoare_quicksort', timeit.timeit("test_quicksort2()", setup="from __main__ import test_quicksort2", number=amt)))
#    print(fmt.format('mergesort', timeit.timeit("test_mergesort()", setup="from __main__ import test_mergesort", number=amt)))





