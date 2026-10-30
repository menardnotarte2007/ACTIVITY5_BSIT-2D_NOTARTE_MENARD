# linked_queue.py
# Implementation of a dynamic Queue data structure using a Singly Linked List.
# Dual anchor references (front & rear) are maintained to provide constant O(1) execution.

class Node:
    def __init__(self, value):
        """Initializes a standalone node holding data and a next reference pointer."""
        self.value = value
        self.next = None


class LinkedQueue:
    def __init__(self):
        """Initializes an empty queue tracking both the front and rear anchors."""
        self.front = None  # Dequeue elements from the head pointer
        self.rear = None   # Enqueue elements at the tail pointer

    def is_empty(self) -> bool:
        """Returns True if the queue contains no nodes, False otherwise."""
        return self.front is None

    def enqueue(self, value):
        """Inserts an element at the rear (tail) of the queue in O(1) time complexity."""
        node = Node(value)
        if self.is_empty():
            self.front = node  # If empty, the first node is both the front and rear
        else:
            self.rear.next = node  # Link the new node immediately after the old tail
        self.rear = node  # Re-assign the rear pointer to track the new end boundary

    def dequeue(self):
        """
        Removes and returns the front item from the queue in O(1) time complexity.
        Safely clears structural references to avoid stale dangling pointers.
        Raises an IndexError if the queue is empty (Underflow condition).
        """
        if self.is_empty():
            raise IndexError("Queue underflow")
            
        value = self.front.value
        self.front = self.front.next  # Shift front reference forward down the chain
        
        # Avoid structural leaks: clear the rear tracker if the queue is now empty
        if self.front is None:
            self.rear = None
            
        return value

    def peek_front(self):
        """
        Returns the item at the front of the queue without removing it.
        Raises an IndexError if the queue is empty.
        """
        if self.is_empty():
            raise IndexError("Queue is empty")
        return self.front.value
