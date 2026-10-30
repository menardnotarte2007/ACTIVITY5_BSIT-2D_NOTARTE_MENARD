 Module 5: Fundamental Data Structures – Stacks and Queues

Welcome to the documentation for Module 5: Fundamental Data Structures. This module covers the core theoretical concepts, behavioral principles, implementations, and real-world applications of two foundational linear data structures: Stacks and Queues.

1.0 Learning Outcomes

By the end of this module, you should be able to:
• Explain the LIFO principle and implement stack operations (push, pop, peek).
• Explain the FIFO principle and implement queue operations (enqueue, dequeue).
• Implement stacks and queues using both static arrays and dynamic linked lists.
• Describe real-world applications of stacks (e.g., function calls, undo systems).
• Describe real-world applications of queues (e.g., task scheduling, buffering).

 The Stack


2.1 The LIFO Principle

A stack is a linear data structure where elements are added and removed from a single end, known as the top. It operates under the LIFO (Last In, First Out) principle: the most recently added item is always the first one to be removed.
• Analogy: A stack of plates in a cafeteria. You add new plates to the top and pull clean plates from the top. To reach the bottom plate, every plate above it must be cleared.

2.2 Core Operations & Complexities

All primitive stack operations execute with a time complexity of \(O(1)\):

Operation	Description	Precondition	Time Complexity
push(x)	Inserts element x at the top of the stack.	Stack is not full (for array-based structures).	\(O(1)\)
pop()	Removes and returns the top element.	Stack is not empty.	\(O(1)\)
peek()	Returns the top element without removing it.	Stack is not empty.	\(O(1)\)
is_empty()	Returns True if the stack contains no elements.	None.	\(O(1)\)
is_full()	Returns True if an array-backed stack is at capacity.	Array-based only.	\(O(1)\)


2.3 Boundary Conditions

• Stack Underflow: Triggered when attempting to execute pop() or peek() on an empty stack.
• Stack Overflow: Triggered when attempting to execute push() on a fixed-size array implementation that has reached capacity.

3.0 The Queue


3.1 The FIFO Principle

A queue is a linear data structure where elements are inserted at one end (rear/tail) and removed from the opposite end (front/head). It operates under the FIFO (First In, First Out) principle: the element that has been waiting the longest is processed first.
• Analogy: A line at a store cashier counter. New customers join at the back, and the person at the front is served first.

3.2 Core Operations & Complexities

All primitive queue operations execute with a time complexity of \(O(1)\):

Operation	Description	Precondition	Time Complexity
enqueue(x)	Inserts element x at the rear of the queue.	Queue is not full (for array-based structures).	\(O(1)\)
dequeue()	Removes and returns the front element.	Queue is not empty.	\(O(1)\)
peek_front()	Returns the front element without removing it.	Queue is not empty.	\(O(1)\)
is_empty()	Returns True if the queue contains no elements.	None.	\(O(1)\)
is_full()	Returns True if an array-backed queue is at capacity.	Array-based only.	\(O(1)\)


4.0 Stacks vs. Queues at a Glance


Aspect	Stack	Queue
Principle	LIFO (Last In, First Out)	FIFO (First In, First Out)
Access Points	Same end (top)	Opposite ends (front / rear)
Core Operations	push, pop, peek	enqueue, dequeue, peek_front
Array Architecture	Single tracking index (top)	Circular buffer using front + size pointers
Linked List Architecture	Single anchor reference (head only)	Dual anchor references (head and tail)
Key Applications	Function call stacks, Undo systems, DFS, expression evaluation	OS scheduling, data buffering, BFS, print spooling


5.0 Core Applications


5.1 Real-World Stack Applications

1. The System Call Stack: Manages function execution. Every function call creates an activation record (stack frame) containing parameters and local variables. Frames are popped off when the function terminates. Excessive recursion triggers a RecursionError when this memory space overflows.
2. Undo/Redo Mechanics: Text editors preserve user actions on an undo stack. Popping a state moves it onto a secondary redo stack.
3. Algorithmic Utilities: Balanced parenthesis validation, infix-to-postfix conversion, browser back-button history, and Depth-First Search (DFS) traversals.

5.2 Real-World Queue Applications

1. Task & Process Scheduling: OS ready-queues hold processes waiting for CPU cycles under round-robin schedulers. Print spoolers queue printable document blocks in their order of arrival.
2. Data Streaming & Buffering: Reconciles speed discrepancies between production and consumption. Examples include hardware keyboard line-buffers, network packet streaming pools, and asynchronous disk I/O handling.
3. Distributed Solutions: Breadth-First Search (BFS) graphs, customer service ticketing queues, and enterprise message broker networks.

6.0 Common Pitfalls & Implementation Guidelines

Avoid these common engineering issues when writing your code implementations:
• Off-by-One Bounds Errors: Do not initialize an array-backed stack pointer top to 0. It must initialize to -1 to correctly match standard pre-increment push mechanics.
• Circular Queue Fullness Ambiguity: Never check if front == rear to see if a circular queue is full. This condition is identical to an empty queue status. Track an independent size variable to guarantee accurate calculations.
• Dangling References: Ensure your linked-list queue explicitly clears out its rear or front pointers to None if a dequeue() statement empties the container entirely. Leaving stale pointers causes bad enqueues later.
• Sub-Optimal Node Targeting: In a singly-linked stack, always insert and remove elements at the head (\(O(1)\)). Targeting the tail requires complete list traversal, degrading performance to \(O(n)\).
• Misusing Native Structures: Avoid running insert(0, x) or pop(0) on standard Python lists to emulate linear abstract data types. These routines trigger global memory shifts that result in costly \(O(n)\) performance bottlenecks.
