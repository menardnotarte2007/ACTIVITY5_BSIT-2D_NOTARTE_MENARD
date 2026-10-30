# print_queue.py
# Simulates a First-In, First-Out (FIFO) print queue environment.
# Completed as part of Module 5 Laboratory Activity (Exercise 6b).

from linked_queue import LinkedQueue

def simulate_print_queue(jobs_list):
    """
    Simulates printing system jobs using a FIFO LinkedQueue structure.
    Each job element in jobs_list should be a dictionary:
    e.g., {'id': 'Document.pdf', 'pages': 5}
    """
    print_queue = LinkedQueue()
    
    print("\n--- Enqueuing Print Jobs ---")
    for job in jobs_list:
        print_queue.enqueue(job)
        print(f"Job [{job['id']}] with {job['pages']} pages added to the queue.")
        
    print("\n--- Processing Jobs (FIFO Order) ---")
    wait_order = 1
    while not print_queue.is_empty():
        current_job = print_queue.dequeue()
        print(f"Processing Order #{wait_order}: Printing Job [{current_job['id']}] ({current_job['pages']} pages)")
        wait_order += 1
        
    print("All print jobs successfully processed.")


if __name__ == "__main__":
    # Sample run dataset to demonstrate and test functionality directly
    sample_jobs = [
        {'id': 'Lab5_Draft.pdf', 'pages': 8},
        {'id': 'Receipt_1092.png', 'pages': 1},
        {'id': 'Thesis_Final_v2.docx', 'pages': 45}
    ]
    simulate_print_queue(sample_jobs)
