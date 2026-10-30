# node.py
# Shared Node class implementation for linked list data structures.
# Reused across both LinkedStack and LinkedQueue implementations.

class Node:
    def __init__(self, value):
        """
        Initializes a standalone node holding a data value 
        and an empty reference pointer to the next consecutive node.
        """
        self.value = value
        self.next = None
