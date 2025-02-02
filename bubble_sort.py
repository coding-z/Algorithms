# Naive bubble sort

def naive_bubble_sort(vals: list[int]) -> list[int]:
    for _ in range(len(vals) - 1):
        for i in range(len(vals) - 1):
            if vals[i] > vals[i + 1]:
                vals[i], vals[i + 1] = vals[i + 1], vals[i]
    
    return vals
