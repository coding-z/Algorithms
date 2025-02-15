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
    
    def pop_max(self):
        """Removes and returns the largest heap item."""
        # Swap the max and last items
        buffer = self.array[0]
        self.array[0] = self.array[-1]
        self.array[-1] = buffer

        value = self.array.pop()

        index = 0
        child1 = 2 * index + 1
        child2 = child1 + 1

        if child2 < len(self.array) and self.array[child1] > self.array[child2]:

        while self.array[index] < max(self.array[child1], self.array[child2]):
            if self.array[child1] > self.array[child2]:

