# Activity: Stacks and Queues (Array vs. Linked List)

This repository contains data structure implementations completed for **Module 5: Fundamental Data Structures**. The objective of this activity is to build and evaluate linear data structures (Stacks and Queues) from first principles using both static fixed-size arrays and dynamic singly linked lists.

## 📂 Project Structure

The project consists of the following individual source files:

*   `main.py`: The primary interactive, menu-driven command-line program that serves as the test driver for all implementations.
*   `applications.py`: Contains individual exercises leveraging these data structures to solve specific programmatic problems (Balanced Parentheses and a FIFO Print Queue Simulation).
*   `analysis.md`: Detailed written analysis answering foundational questions about algorithmic complexity and structural trade-offs.

### Core Data Structure Implementations
1.  **`ArrayStack`**: A stack implementation bound by a fixed capacity tracking state through a linear index.
2.  **`LinkedStack`**: A dynamic stack managed strictly from the head node to guarantee optimal time performance.
3.  **`ArrayQueue`**: A circular queue utilizing a modulo buffer calculation to completely bypass array item shifts.
4.  **`LinkedQueue`**: A queue managed via concurrent front (head) and rear (tail) entry references.

---

## 🚀 How to Run the Implementation

Ensure you have **Python 3.x** installed on your workstation. Run the scripts individually via your command-line interface.

### 1. Interactive Structure Testing
To open the menu-driven system and interactively execute `push`, `pop`, `enqueue`, or `dequeue` routines while monitoring the structure state visually, run:
```bash
python main.py
```

### 2. Application Exercises
To execute the modular solution tasks (validating matching structural brackets or processing consecutive simulated print streams), run:
```bash
python applications.py
```

---

## 🧪 Expected Error Handling

The classes are built to throw explicit Python runtime violations under illegal operations instead of failing silently:

*   **Stack Overflow / Queue Overflow:** Encountered if you push/enqueue an item into a fixed-size array structure that has reached maximum capacity. Throws an `OverflowError`.
*   **Stack Underflow / Queue Underflow:** Encountered if you attempt to pop/dequeue/peek from an empty instance. Throws an `IndexError`.

---

## 🛠️ Common Implementation Pitfalls Avoided

*   **Linear Shifting Penalty Avoided:** Avoided using native Python operations like `insert(0, x)` or `pop(0)` which run in $O(n)$ time. All custom queue modifications run in $O(1)$.
*   **Circular Buffer Fullness Resolution:** Maintained a dedicated integer element counter (`size`) inside the circular queue tracking routines instead of comparing indices to clear up ambiguity between fully populated and empty states.
*   **Dangling Memory Reference Cleanup:** Designed explicit pointer clearings ensuring `rear` and `front` components zero out to `None` if a list-backed queue layout drops down to zero remaining elements.
