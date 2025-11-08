# parallel_process_demo.py
import multiprocessing
import time
from dosomething import do_something

def run_parallel_processes(task_size=1000):
    """
    Run two separate processes performing CPU-bound computations
    simultaneously and measure execution time.
    """
    manager = multiprocessing.Manager()
    results_a = manager.list()
    results_b = manager.list()

    # Create two processes
    process1 = multiprocessing.Process(name='Process-1', target=do_something, args=(task_size, results_a))
    process2 = multiprocessing.Process(name='Process-2', target=do_something, args=(task_size, results_b))

    print("🔹 Starting parallel processes...\n")
    start_time = time.time()

    # Start processes
    process1.start()
    process2.start()

    # Wait for processes to finish
    process1.join()
    process2.join()

    end_time = time.time()

    print("✅ Processes completed successfully!")
    print(f"Process 1 output length: {len(results_a)}")
    print(f"Process 2 output length: {len(results_b)}")
    print(f"Total execution time: {end_time - start_time:.2f} seconds\n")


if __name__ == "__main__":
    run_parallel_processes(task_size=1000)
