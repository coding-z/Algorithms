# Insertion Sort Algorithm

def insertion_sort(list):
    """Insertion sort of list in ascending order.
    
    Complexity  Best    Worst
    Time        O(n)    O(n^2)
    Aux Space   O(1)    O(1)
    
    Invariant: Sorted sublist at list start.
    
    Incremental if appending at end.
    Stable when only shifting strictly larger items.
    """
    for i in range(1, len(list)):
        saved = list[i]
        j = i - 1
        while j >= 0 and list[j] > saved:
            list[j + 1] = list[j]
            j -= 1
        list[j + 1] = saved
