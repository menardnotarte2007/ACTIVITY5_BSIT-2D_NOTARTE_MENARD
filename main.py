# main.py
# Interactive, menu-driven test driver program for the custom stack and queue classes.
# Completed as part of Module 5 Laboratory Activity deliverables.

import sys

# Import custom implementations from independent workspace source files
from array_stock import ArrayStack
from linked_stack import LinkedStack
from circular_array_queue import ArrayQueue
from linked_queue import LinkedQueue


def display_stack_state(stack, mode: str):
    """Prints a clean, visual representation of the stack contents."""
    if stack.is_empty():
        print("\n[Stack Status]: Empty")
        return
        
    print("\n[Stack Status]:")
    if mode == "array":
        # Traverses from the top element down to index 0
        for i in range(stack.top, -1, -1):
            marker = " <- (Top)" if i == stack.top else ""
            print(f" | {stack.data[i]} |{marker}")
        print(" +---+ (Bottom)")
    else:
        # Traverses node elements from head downwards
        current = stack.top
        is_first = True
        while current is not None:
            marker = " <- (Top)" if is_first else ""
            print(f" | {current.value} |{marker}")
            current = current.next
            is_first = False
        print(" +---+ (Bottom)")


def display_queue_state(queue, mode: str):
    """Prints a sequential layout of the queue from front to rear."""
    if queue.is_empty():
        print("\n[Queue Status]: Empty")
        return

    print("\n[Queue Status]: ", end="")
    if mode == "array":
        # Extract active circular elements using modulo wrap-around tracking
        elements = []
        for i in range(queue.size):
            idx = (queue.front + i) % len(queue.data)
            elements.append(str(queue.data[idx]))
        print(" -> ".join(elements) + " [Front to Rear]")
        print(f" (Underlying Array Storage: {queue.data} | Front Index Pointer: {queue.front})")
    else:
        # Traverse list from front to rear
        elements = []
        current = queue.front
        while current is not None:
            elements.append(str(current.value))
            current = current.next
        print(" -> ".join(elements) + " [Front to Rear]")


def run_stack_menu(stack, mode: str):
    """Handles operational sub-routines for testing stack data structures."""
    while True:
        print(f"\n--- Stack Sub-Menu ({mode.upper()}) ---")
        print("1. Push Element")
        print("2. Pop Element")
        print("3. Peek Top")
        print("4. Verify if Empty")
        if mode == "array":
            print("5. Verify if Full")
        print("0. Back to Main Directory")
        
        choice = input("Select an operation: ").strip()
        
        try:
            if choice == "1":
                val = input("Enter value to push: ")
                stack.push(val)
                display_stack_state(stack, mode)
            elif choice == "2":
                popped = stack.pop()
                print(f"\nRemoved element: {popped}")
                display_stack_state(stack, mode)
            elif choice == "3":
                print(f"\nCurrent Top Element: {stack.peek()}")
            elif choice == "4":
                print(f"\nIs empty? {stack.is_empty()}")
            elif choice == "5" and mode == "array":
                print(f"\nIs full? {stack.is_full()}")
            elif choice == "0":
                break
            else:
                print("Invalid input selection. Please choose an operation from the options.")
        except (IndexError, OverflowError) as e:
            print(f"\n[ERROR EXCEPTION]: {e}")


def run_queue_menu(queue, mode: str):
    """Handles operational sub-routines for testing queue data structures."""
    while True:
        print(f"\n--- Queue Sub-Menu ({mode.upper()}) ---")
        print("1. Enqueue Element")
        print("2. Dequeue Element")
        print("3. Peek Front")
        print("4. Verify if Empty")
        if mode == "array":
            print("5. Verify if Full")
        print("0. Back to Main Directory")
        
        choice = input("Select an operation: ").strip()
        
        try:
            if choice == "1":
                val = input("Enter value to enqueue: ")
                queue.enqueue(val)
                display_queue_state(queue, mode)
            elif choice == "2":
                dequeued = queue.dequeue()
                print(f"\nRemoved element: {dequeued}")
                display_queue_state(queue, mode)
            elif choice == "3":
                print(f"\nCurrent Front Element: {queue.peek_front()}")
            elif choice == "4":
                print(f"\nIs empty? {queue.is_empty()}")
            elif choice == "5" and mode == "array":
                print(f"\nIs full? {queue.is_full()}")
            elif choice == "0":
                break
            else:
                print("Invalid input selection. Please choose an operation from the options.")
        except (IndexError, OverflowError) as e:
            print(f"\n[ERROR EXCEPTION]: {e}")


def main():
    """Main application runtime selection routing."""
    while True:
        print("\n=============================================")
        print(" MODULE 5 INTERACTIVE TESTING ENVIRONMENT")
        print("=============================================")
        print("1. Initialize Array-Based Fixed Stack")
        print("2. Initialize Linked-List Dynamic Stack")
        print("3. Initialize Circular Array-Based Queue")
        print("4. Initialize Linked-List Dynamic Queue")
        print("0. Exit Testing Suite")
        
        main_choice = input("Select a structure configuration: ").strip()
        
        if main_choice == "1":
            capacity = int(input("Define static stack storage capacity limits: "))
            stack = ArrayStack(capacity)
            run_stack_menu(stack, "array")
        elif main_choice == "2":
            stack = LinkedStack()
            run_stack_menu(stack, "linked")
        elif main_choice == "3":
            capacity = int(input("Define static circular queue capacity limits: "))
            queue = ArrayQueue(capacity)
            run_queue_menu(queue, "array")
        elif main_choice == "4":
            queue = LinkedQueue()
            run_queue_menu(queue, "linked")
        elif main_choice == "0":
            print("\nExiting program execution loop. Laboratory simulation terminated.")
            sys.exit()
        else:
            print("Invalid initialization selection. Please specify a value between 0 and 4.")

if __name__ == "__main__":
    main()
