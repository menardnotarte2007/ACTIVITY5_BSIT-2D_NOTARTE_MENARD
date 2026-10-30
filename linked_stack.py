# linked_stack.py
# Implementation of a dynamic Stack data structure using a Singly Linked List.
# Operations are locked at the head of the list to preserve O(1) constraints.

class Node:
    def __init__(self, value):
        """Initializes a standalone node holding data and a next reference pointer."""
        self.value = value
        self.next = None


class LinkedStack:
    def __init__(self):
        """Initializes an empty stack. The head node acts as the top of the stack."""
        self.top = None  # head of the list = top of the stack

    def is_empty(self) -> bool:
        """Returns True if the stack has no nodes, False otherwise."""
        return self.top is None

    def push(self, value):
        """Inserts an item at the top (head) of the stack in O(1) time complexity."""
        node = Node(value)
        node.next = self.top  # New node points to the old top node
        self.top = node       # New node officially becomes the new top anchor

    def pop(self):
        """
        Removes and returns the top item from the stack in O(1) time complexity.
        Raises an IndexError if the stack is completely empty (Underflow condition).
        """
        if self.is_empty():
            raise IndexError("Stack underflow")
        
        value = self.top.value
        self.top = self.top.next  # Move the top pointer down to the consecutive node
        return value

    def peek(self):
        """
        Returns the top value without modifying the stack structure.
        Raises an IndexError if the stack is empty.
        """
        if self.is_empty():
            raise IndexError("Stack is empty")
        return self.top.value
