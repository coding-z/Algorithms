# Naive bubble sort
#           Worst   Best
# Time      O(n^2)  O(n^2)
# Aux Space O(1)    O(1)
# Incremental if prepend
# Stable

def naive_bubble_sort(vals: list[int]) -> list[int]:
    for _ in range(len(vals) - 1):
        for i in range(len(vals) - 1):
            if vals[i] > vals[i + 1]:
                vals[i], vals[i + 1] = vals[i + 1], vals[i]
    
    return vals

# Bubble sort with marker for sorted sublist
#           Worst   Best
# Time      O(n^2)  O(n^2)
# Aux Space O(1)    O(1)
# Incremental if prepend
# Stable


def marked_bubble_sort(vals: list[int]) -> list[int]:
    for mark in range(len(vals) - 1, 0, -1):
        for i in range(mark):
            if vals[i] > vals[i + 1]:
                vals[i], vals[i + 1] = vals[i + 1], vals[i]
        mark -= 1
    
    return vals

# Bubble sort with detection for when there are no more swaps
#           Worst   Best
# Time      O(n^2)  O(n)
# Aux Space O(1)    O(1)
# Incremental if prepend
# Stable


def bubble_sort_2(vals: list[int]) -> list[int]:
    for mark in range(len(vals) - 1, 0, -1):
        swapped = False
        for i in range(mark):
            if vals[i] > vals[i + 1]:
                vals[i], vals[i + 1] = vals[i + 1], vals[i]
                swapped = True
        if not swapped:
            break
    return vals
