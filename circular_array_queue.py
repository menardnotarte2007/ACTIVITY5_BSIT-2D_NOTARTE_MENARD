# circular_array_queue.py
# Implementation of a Queue using a Python list as a circular buffer with modulo arithmetic.
# Completed as part of Module 5: Fundamental Data Structures.

class ArrayQueue:
    def __init__(self, capacity: int):
        """
        Initializes an empty queue with a fixed capacity.
        Tracks front pointer and element size to eliminate fullness ambiguity.
        """
        self.data = [None] * capacity
        self.front = 0
        self.size = 0

    def is_empty(self) -> bool:
        """Returns True if the queue contains no elements, False otherwise."""
        return self.size == 0

    def is_full(self) -> bool:
        """Returns True if the queue size reaches its maximum capacity, False otherwise."""
        return self.size == len(self.data)

    def enqueue(self, value):
        """
        Inserts an element at the rear of the queue using modulo wrap-around.
        Raises an OverflowError if the queue is full.
        """
        if self.is_full():
            raise OverflowError("Queue overflow")
        
        # Calculate the rear index using the modulo operator to enable wrap-around
        rear = (self.front + self.size) % len(self.data)
        self.data[rear] = value
        self.size = self.size + 1

    def dequeue(self):
        """
        Removes and returns the element at the front of the queue.
        Advances the front index with modulo wrap-around and checks for underflow.
        """
        if self.is_empty():
            raise IndexError("Queue underflow")
            
        value = self.data[self.front]
        self.data[self.front] = None  # Clean up reference to allow garbage collection
        
        # Advance the front index using the modulo operator to enable wrap-around
        self.front = (self.front + 1) % len(self.data)
        self.size = self.size - 1
        return value

    def peek_front(self):
        """
        Returns the element at the front of the queue without removing it.
        Raises an IndexError if the queue is empty.
        """
        if self.is_empty():
            raise IndexError("Queue is empty")
        return self.data[self.front]
