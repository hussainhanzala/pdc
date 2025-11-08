import threading
import time
from dosomething import do_something

def worker_task(worker_id, items_to_process, shared_results, lock):
    """
    Each thread performs a CPU-bound operation within a locked section.
    Ensures thread-safe access to the shared results list.
    """
    print(f"[Worker-{worker_id}] Starting computation...")
    
    # Lock ensures one thread modifies shared resource at a time
    with lock:
        do_something(items_to_process, shared_results)
        print(f"[Worker-{worker_id}] Work completed and results updated.")
    
    print(f"[Worker-{worker_id}] Thread exiting.\n")


if __name__ == "__main__":
    results = []
    mutex_lock = threading.Lock()

    total_threads = 3
    workload_per_thread = 7

    # Create worker threads
    threads = [
        threading.Thread(
            target=worker_task,
            args=(i + 1, workload_per_thread, results, mutex_lock)
        )
        for i in range(total_threads)
    ]

    print("\n=== Starting Locked Multithreading Execution ===")
    start_time = time.perf_counter()

    # Start threads with small delay for visibility
    for thread in threads:
        thread.start()
        time.sleep(0.3)

    # Wait for all threads to complete
    for thread in threads:
        thread.join()

    end_time = time.perf_counter()

    print("\n✅ All worker threads finished successfully!")
    print(f"📊 Total items processed (with lock): {len(results)}")
    print(f"⏱️ Total execution time: {end_time - start_time:.3f} seconds")
