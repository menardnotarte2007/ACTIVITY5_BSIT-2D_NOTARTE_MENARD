# Module 5: Sample Runs and Error Handling Verification

This document logs the terminal outputs for the menu-driven test suite (`main.py`) and the application utilities (`applications.py`). It explicitly demonstrates correct structural mutations, circular queue wrap-around behaviors, and active exception handling for underflow and overflow states.

---

## 1. Array-Based Stack (`ArrayStack`) Verification

### Stack Overflow Test
* **Action:** Initialize an `ArrayStack` with a fixed capacity of 2, push 2 elements, and then attempt a 3rd push.
* **Result:** Triggers an explicit `OverflowError`.

```text
=============================================
 MODULE 5 INTERACTIVE TESTING ENVIRONMENT
=============================================
1. Initialize Array-Based Fixed Stack
2. Initialize Linked-List Dynamic Stack
3. Initialize Circular Array-Based Queue
4. Initialize Linked-List Dynamic Queue
0. Exit Testing Suite
Select a structure configuration: 1
Define static stack storage capacity limits: 2

--- Stack Sub-Menu (ARRAY) ---
1. Push Element
2. Pop Element
3. Peek Top
4. Verify if Empty
5. Verify if Full
0. Back to Main Directory
Select an operation: 1
Enter value to push: A

[Stack Status]:

 | A | <- (Top)
 +---+ (Bottom)

--- Stack Sub-Menu (ARRAY) ---
Select an operation: 1
Enter value to push: B

[Stack Status]:

 | B | <- (Top)
 | A |
 +---+ (Bottom)

--- Stack Sub-Menu (ARRAY) ---
Select an operation: 1
Enter value to push: C

[ERROR EXCEPTION]: Stack overflow
```

### Stack Underflow Test
* **Action:** Perform consecutive `pop` adjustments on the stack until empty, then attempt another removal.
* **Result:** Triggers an explicit `IndexError`.

```text
--- Stack Sub-Menu (ARRAY) ---
Select an operation: 2
Removed element: B

[Stack Status]:

 | A | <- (Top)
 +---+ (Bottom)

--- Stack Sub-Menu (ARRAY) ---
Select an operation: 2
Removed element: A

[Stack Status]: Empty

--- Stack Sub-Menu (ARRAY) ---
Select an operation: 2

[ERROR EXCEPTION]: Stack underflow
```

---

## 2. Circular Array-Based Queue (`ArrayQueue`) Verification

### Wrap-Around and Buffer Recycling Demonstration
* **Action:** Initialize an `ArrayQueue` with a capacity of 3. Populate completely, remove the front item to advance pointers, and insert a new item past the physical boundary to trigger modulo optimization.
* **Result:** Demonstrates functional linear index wrap-around.

```text
=============================================
 MODULE 5 INTERACTIVE TESTING ENVIRONMENT
=============================================
Select a structure configuration: 3
Define static circular queue capacity limits: 3

--- Queue Sub-Menu (ARRAY) ---
Select an operation: 1
Enter value to enqueue: A
[Queue Status]: A [Front to Rear]
 (Underlying Array Storage: ['A', None, None] | Front Index Pointer: 0)

--- Queue Sub-Menu (ARRAY) ---
Select an operation: 1
Enter value to enqueue: B
[Queue Status]: A -> B [Front to Rear]
 (Underlying Array Storage: ['A', 'B', None] | Front Index Pointer: 0)

--- Queue Sub-Menu (ARRAY) ---
Select an operation: 1
Enter value to enqueue: C
[Queue Status]: A -> B -> C [Front to Rear]
 (Underlying Array Storage: ['A', 'B', 'C'] | Front Index Pointer: 0)

--- Queue Sub-Menu (ARRAY) ---
Select an operation: 2
Removed element: A
[Queue Status]: B -> C [Front to Rear]
 (Underlying Array Storage: [None, 'B', 'C'] | Front Index Pointer: 1)

--- Queue Sub-Menu (ARRAY) ---
Select an operation: 1
Enter value to enqueue: D
[Queue Status]: B -> C -> D [Front to Rear]
 (Underlying Array Storage: ['D', 'B', 'C'] | Front Index Pointer: 1)
```
*Note: As shown above, `'D'` cleanly wrapped around to fill index `0` because index `1` was flagged as the current logical front.*

### Queue Overflow Test
* **Action:** Enqueue another item while the circular structure is at capacity size limits.
* **Result:** Triggers an explicit `OverflowError`.

```text
--- Queue Sub-Menu (ARRAY) ---
Select an operation: 1
Enter value to enqueue: E

[ERROR EXCEPTION]: Queue overflow
```

---

## 3. Dynamic Structures Underflow Verification

Both `LinkedStack` and `LinkedQueue` possess flexible capacities but enforce direct defensive boundaries against unlawful removals from unpopulated links.

### Linked-List Stack Underflow
```text
--- Stack Sub-Menu (LINKED) ---
Select an operation: 2

[ERROR EXCEPTION]: Stack underflow
```

### Linked-List Queue Underflow
```text
--- Queue Sub-Menu (LINKED) ---
Select an operation: 2

[ERROR EXCEPTION]: Queue underflow
```

---

## 4. Application Exercise Verification (`applications.py`)

Executing `applications.py` performs diagnostic tests evaluating bracket string balances alongside active system task print sequencing.

```text
\$ python applications.py

--- Testing Parentheses Balance Checker ---
Is '{[()]}' balanced? True
Is '{[(])}' balanced? False

--- Testing Print Queue Simulation ---

--- Enqueuing Print Jobs ---
Job [Lab5_Draft.pdf] with 8 pages added to the queue.
Job [Receipt_1092.png] with 1 pages added to the queue.
Job [Thesis_Final_v2.docx] with 45 pages added to the queue.

--- Processing Jobs (FIFO Order) ---
Processing Order #1: Printing Job [Lab5_Draft.pdf] (8 pages)
Processing Order #2: Printing Job [Receipt_1092.png] (1 pages)
Processing Order #3: Printing Job [Thesis_Final_v2.docx] (45 pages)
All print jobs successfully processed.
```
