# Module 5 Analysis: Architectural Design Decisions

This document contains the structural analysis regarding implementation choices for stacks and queues as required by the Module 5 Laboratory Activity guidelines.

---

## 1. Linked-List Stack: Operating at the Head vs. the Tail

### Design Choice
In the `LinkedStack` implementation, all insertion (`push`) and removal (`pop`) operations are explicitly anchored at the **head** of the singly linked list rather than the tail.

### Operational Efficiency Analysis
* **Head-Based Operations ($O(1)$):** Manipulating the head node allows us to insert or remove elements in constant time. A new node is simply linked to point to the current head, and the head pointer is updated. This directly preserves the required $O(1)$ efficiency for primitive stack operations.
* **Tail-Based Operations ($O(n)$):** In a standard singly linked list, a reference pointer only moves forward. If we were to `pop` from the tail, we would have to traverse the entire list from the head down to find the *second-to-last* node to update its `.next` pointer to `None`. This sequential traversal introduces a performance bottleneck that scales linearly with the size of the structure, changing the time complexity to $O(n)$. 

---

## 2. Array Queue: The Necessity of a Circular Buffer

### Design Choice
The `ArrayQueue` implementation utilizes the modulo operator (`%`) to treat a static, fixed-size Python list as a **circular buffer** rather than a linear array.

### Operational Efficiency Analysis
* **The Naive Array Problem:** In a non-circular queue, elements are removed from the front index, meaning the `front` pointer progressively moves forward down the list. Once the `rear` reaches the last physical slot of the array, no more elements can be enqueued—even if multiple `dequeue` calls have left completely empty, wasted slots at the front of the list.
* **Alternative Linear Pitfalls ($O(n)$):** To avoid wasting space in a naive array, you would be forced to shift every remaining item leftward by one slot after every single `dequeue()` call. Shifting elements involves a linear array copy operation, which severely penalizes performance by changing a standard queue operation from $O(1)$ to a costly $O(n)$ time complexity.
* **The Circular Solution ($O(1)$):** By implementing wrap-around mechanics using the modulo operator (`%`), the `rear` and `front` pointers smoothly cycle back to index `0` after passing the physical end boundary of the underlying list. This design recycles previously emptied indexes at the front of the array automatically, maximizing memory usage while maintaining a true $O(1)$ run-time execution for both `enqueue` and `dequeue` routines.
