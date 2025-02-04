# Insertion sort
#           Worst   Best
# Time      O(n^2)  O(n)
# Aux Space O(1)    O(1)
# Incremental if appending to end
# Invariant: sorted sublist at start, though not necessarily in final positions
# Is stable since only shuffling strictly larger items to the right

def insertion_sort(vals: list[int]) -> list[int]:
    for i in range(1, len(vals)):
        saved = vals[i]
        j = i - 1
        while j >= 0 and vals[j] > saved:
            vals[j + 1] = vals[j]
            j -= 1
        vals[j + 1] = saved
    return vals
