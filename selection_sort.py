# Selection Sort Algorithm

def selection_sort(list):
    """Sorts list in ascending order with selection sort.
    
    Complexity  Best    Worst
    Time        O(n^2)  O(n^2)
    Aux Space   O(1)    O(1)

    Invariant: Sorted sublist at front which is smaller than remaining list.

    Not incremental as appending or prepending breaks invariant.
    Unstable as swapping of non-adjacent items occurs.
    """
    for i in range(len(list) - 1):
        min_index = i
        for j in range(i + 1, len(list)):
            if list[j] < list[min_index]:
                min_index = j
        list[i], list[min_index] = list[min_index], list[i]
