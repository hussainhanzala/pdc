# do_something.py  — Enhanced CPU-bound computation example
import math
import time

def do_something(task_size, output_list):
    """
    Performs a simulated CPU-bound computation by running
    mathematical operations in a loop and appending results
    to a shared output list.
    """
    for i in range(task_size):
        # Simulate heavier CPU work with multiple math operations
        val = math.sqrt(i + 1) * math.sin(i % 10) + math.log1p(i + 1)
        result = round(val, 5)
        output_list.append(result)

if __name__ == "__main__":
    results = []
    start_time = time.perf_counter()

    do_something(10_000, results)

    end_time = time.perf_counter()
    print(f"✅ Computed {len(results)} results successfully.")
    print(f"⏱️ Execution time: {end_time - start_time:.3f} seconds")
