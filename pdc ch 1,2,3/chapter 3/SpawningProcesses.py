# spawning_processes_demo.py
import multiprocessing
from dosomething import do_something

def my_func(index: int):
    """
    Worker process that executes a CPU-bound task with workload proportional to index.
    
    Args:
        index (int): Determines the task size.
    """
    process_name = multiprocessing.current_process().name
    print(f"[{process_name}] Starting process {index}...")

    # Shared list to collect results
    results = multiprocessing.Manager().list()
    do_something(index * 1000, results)

    print(f"[{process_name}] Process {index} finished with {len(results)} results.\n")


if __name__ == '__main__':
    print("🔹 Spawning multiple processes dynamically...\n")

    num_processes = 6
    processes = []

    # Create and start processes
    for i in range(num_processes):
        p = multiprocessing.Process(target=my_func, args=(i,))
        processes.append(p)
        p.start()

    # Wait for all processes to finish
    for p in processes:
        p.join()

    print("✅ All processes completed successfully.")
