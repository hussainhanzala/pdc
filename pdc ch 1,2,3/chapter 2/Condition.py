import threading
import time
from dosomething import do_something

def worker_task(worker_id, task_size, shared_results, condition_lock):
    """Each worker performs a CPU-heavy operation and signals progress."""
    print(f"[Worker-{worker_id}] Started with {task_size} items to process.")
    do_something(task_size, shared_results)
    
    with condition_lock:
        print(f"[Worker-{worker_id}] Completed work. Notifying monitor...")
        condition_lock.notify_all()
    
    print(f"[Worker-{worker_id}] Finished execution.")


def monitor_progress(shared_results, condition_lock, total_expected):
    """Monitor thread observes progress of the worker threads."""
    print("[Monitor] Monitoring started...")
    
    with condition_lock:
        while len(shared_results) < total_expected:
            condition_lock.wait()
            print(f"[Monitor] Progress update: {len(shared_results)} of {total_expected} items done.")
    
    print("[Monitor] All tasks completed.")


if __name__ == "__main__":
    start_time = time.perf_counter()

    results = []
    threads_to_run = 3
    items_per_thread = 7
    total_expected = threads_to_run * items_per_thread
    condition = threading.Condition()

    # Create worker threads
    workers = [
        threading.Thread(
            target=worker_task,
            args=(i + 1, items_per_thread, results, condition)
        )
        for i in range(threads_to_run)
    ]

    # Create a monitor thread
    monitor = threading.Thread(
        target=monitor_progress,
        args=(results, condition, total_expected)
    )

    print("\n=== Starting Threads ===")
    monitor.start()

    # Stagger worker starts slightly
    for worker in workers:
        worker.start()
        time.sleep(0.3)

    # Wait for all threads to finish
    for worker in workers:
        worker.join()

    monitor.join()

    end_time = time.perf_counter()

    print("\n✅ All threads completed successfully!")
    print(f"📊 Total items processed: {len(results)}")
    print(f"⏱️ Execution time: {end_time - start_time:.3f} seconds")
