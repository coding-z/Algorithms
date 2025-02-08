# Bubble Sort Algorithms

def bubble_sort_naive(list):
    """Naive unoptimised bubble sort.
    
    Complexity  Best    Worst
    Time        O(n^2)  O(n^2)
    Aux Space   O(1)    O(1)

    Incremental if prepending.
    Stable with strict comparison.
    """
    for _ in range(len(list) - 1):
        for i in range(len(list) - 1):
            if list[i] > list[i + 1]:
                list[i], list[i + 1] = list[i + 1], list[i]

def bubble_sort_marked(list):
    """Bubble sort without searching sorted items.
    
    Complexity  Best    Worst
    Time        O(n^2)  O(n^2)
    Aux Space   O(1)    O(1)
    
    Incremental if prepending.
    Stable with strict comparison.

    In each iteration the largest unsorted item is moved to it's correct
    place. This item can be avoided in the next iteration as it is
    already correctly in place.
    """
    for mark in range(len(list) - 1, 0, -1):
        for i in range(mark):
            if list[i] > list[i + 1]:
                list[i], list[i + 1] = list[i + 1], list[i]

def bubble_sort_optimised(list):
    """Bubble sort optimised to linear best-case time.
    
    Complexity  Best    Worst
    Time        O(n)    O(n^2)
    Aux Space   O(1)    O(1)
    
    Incremental if prepending.
    Stable with strict comparison.

    If no swaps occur in the unsorted sublist, then they are already in sorted
    order. No more iterations are needed afterwards.
    """
    for mark in range(len(list) - 1, 0, -1):
        swapped = False
        for i in range(mark):
            if list[i] > list[i + 1]:
                list[i], list[i + 1] = list[i + 1], list[i]
                swapped = True
        if not swapped:
            break
