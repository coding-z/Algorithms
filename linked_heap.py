"""Heap data structure implemented using linked nodes."""

class MaxHeap:
    """A max heap which stores the largest value at the root."""

    def __init__(self):
        self.root = None
    
    def add(self, value):
        """Adds an item to the heap."""
        
