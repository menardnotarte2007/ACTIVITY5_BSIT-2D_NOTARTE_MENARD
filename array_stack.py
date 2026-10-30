# array_stock.py
# Implementation of a fixed-size Stack using a Python list as the underlying array.
# Completed as part of Module 5: Fundamental Data Structures.

class ArrayStack:
    def __init__(self, capacity: int):
        """
        Initializes an empty stack with a fixed capacity.
        The top pointer starts at -1 to represent an empty state.
        """
        self.data = [None] * capacity
        self.top = -1

    def is_empty(self) -> bool:
        """Returns True if the stack has no elements, False otherwise."""
        return self.top == -1

    def is_full(self) -> bool:
        """Returns True if the array stack is at capacity, False otherwise."""
        return self.top == len(self.data) - 1

    def push(self, value):
        """
        Inserts an element at the top of the stack.
        Raises an OverflowError if the stack is already full.
        """
        if self.is_full():
            raise OverflowError("Stack overflow")
        self.top = self.top + 1
        self.data[self.top] = value

    def pop(self):
        """
        Removes and returns the top element of the stack.
        Raises an IndexError if the stack is empty (Underflow).
        """
        if self.is_empty():
            raise IndexError("Stack underflow")
        value = self.data[self.top]  # Read the top value first
        self.data[self.top] = None   # Clean up reference
        self.top = self.top - 1      # Move top down
        return value

    def peek(self):
        """
        Returns the top element without removing it.
        Raises an IndexError if the stack is empty.
        """
        if self.is_empty():
            raise IndexError("Stack is empty")
        return self.data[self.top]
