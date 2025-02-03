# Selection sort

def selection_sort(vals: list[int]) -> list[int]:
    for i in range(len(vals) - 1):
        min_index = i
        for j in range(i + 1, len(vals)):
            if vals[j] < vals[min_index]:
                min_index = j
        vals[i], vals[min_index] = vals[min_index], vals[i]
    return vals
