# do_something.py  (Enhanced CPU-bound version)
import math
import time

def do_something(task_size, output_list):
    """
    Simulates a CPU-bound operation by performing repeated 
    mathematical computations and appending results to a shared list.
    """
    for i in range(task_size):
        # Simulate CPU-intensive calculations
        val = 0
        for j in range(1000):  # inner loop to add more CPU work
            val += math.sqrt(i + j) * math.sin(j % 10) ** 2
        
        # Final computed value (rounded to avoid floating point noise)
        result = round(val, 4)
        output_list.append(result)

    # Optional: slight delay to simulate realistic processing time
    # time.sleep(0.05)
