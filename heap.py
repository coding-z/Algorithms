"""Heap data structure implemented using an array."""

class MaxHeap:
    """A max heap which stores the largest value at the root."""

    def __init__(self):
        self.array = []
    
    def add(self, value):
        """Adds an item to the heap."""
        self.array.append(value)
        index = len(self.array - 1)
        parent = (index - 1) // 2

        while parent >= 0 and value > self.array[parent]:
            buffer = self.array[parent]
            self.array[parent] = self.array[index]
            self.array[index] = buffer
            index = parent
            parent = (index - 1) // 2
