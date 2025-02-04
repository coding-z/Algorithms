# Selection sort
#           Worst   Best
# Time      O(n^2)  O(n^2)
# Aux Space O(1)    O(1)
# Not incremental as appending or prepending breaks invariant
# Invariant: sorted sublist at front which is all smaller than unsorted sublist
# Unstable as swapping non-adjacent elements

def selection_sort(vals: list[int]) -> list[int]:
    for i in range(len(vals) - 1):
        min_index = i
        for j in range(i + 1, len(vals)):
            if vals[j] < vals[min_index]:
                min_index = j
        vals[i], vals[min_index] = vals[min_index], vals[i]
    return vals
