# Naive bubble sort

def naive_bubble_sort(vals: list[int]) -> list[int]:
    for _ in range(len(vals) - 1):
        for i in range(len(vals) - 1):
            if vals[i] > vals[i + 1]:
                vals[i], vals[i + 1] = vals[i + 1], vals[i]
    
    return vals

# Bubble sort with marker for sorted sublist

def marked_bubble_sort(vals: list[int]) -> list[int]:
    for mark in range(len(vals) - 1, 0, -1):
        for i in range(mark):
            if vals[i] > vals[i + 1]:
                vals[i], vals[i + 1] = vals[i + 1], vals[i]
        mark -= 1
    
    return vals
