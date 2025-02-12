"""Merge sort algorithm and associated functions."""

def merge(seq_a, seq_b):
    """Merges together two sequences in stable order."""
    i, j = 0, 0
    result = []

    while i < len(seq_a) or j < len(seq_b):
        if j >= len(seq_b) or i < len(seq_a) and seq_a[i] <= seq_b[j]:
            result.append(seq_a[i])
            i += 1
        else:
            result.append(seq_b[j])
            j += 1
    
    return result

def merge_sort(seq, start=0, stop=None):
    """Sorts sequence using merge sort."""
    if stop is None:
        stop = len(seq)
    
    if start < stop - 1:
        mid = (start + stop) // 2
        merge_sort(seq, start, mid)
        merge_sort(seq, mid, stop)
        seq[start:stop] = merge(seq[start:mid], seq[mid:stop])
