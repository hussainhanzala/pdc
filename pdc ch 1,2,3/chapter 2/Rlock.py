import threading
import time
from dosomething import do_something

def worker_task(worker_id, items_to_process, shared_data, rlock):
    """
    Each thread performs a CPU-bound task while safely re-acquiring the same RLock.
    Demonstrates the reentrant behavior of RLock (nested locking by the same thread).
    """
    print(f"[Worker-{worker_id}] Starting execution...")

    with rlock:
        print(f"[Worker-{worker_id}] Acquired first lock.")
        # Nested lock acquisition (safe re-entry)
        with rlock:
            print(f"[Worker-{worker_id}] Re-acquired lock (reentrant). Performing computation...")
            do_something(items_to_process, shared_data)
        print(f"[Worker-{worker_id}] Released inner lock.")

    print(f"[Worker-{worker_id}] Task completed and lock released.\n")


if __name__ == "__main__":
    shared_results = []
    reentrant_lock = threading.RLock()

    num_threads = 3
    task_per_thread = 7

    # Prepare worker threads
    threads = [
        threading.Thread(
            target=worker_task,
            args=(i + 1, task_per_thread, shared_results, reentrant_lock)
        )
        for i in range(num_threads)
    ]

    print("\n=== Starting RLock Demonstration ===")
    start_time = time.perf_counter()

    # Launch threads with slight delay for clear sequencing
    for thread in threads:
        thread.start()
        time.sleep(0.3)

    # Wait for all threads to finish
    for thread in threads:
        thread.join()

    end_time = time.perf_counter()

    print("\n✅ All worker threads have finished successfully!")
    print(f"📊 Total items processed (RLock): {len(shared_results)}")
    print(f"⏱️ Total execution time: {end_time - start_time:.3f} seconds")
