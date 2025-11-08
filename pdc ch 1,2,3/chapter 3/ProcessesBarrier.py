# barrier_lock_demo_full.py
import multiprocessing
from time import time
from datetime import datetime
from dosomething import do_something

def task_with_barrier(semaphore, lock, task_load=2):
    """
    Task executed by a process using a semaphore as a barrier-like mechanism
    and a Lock to serialize console output.
    """
    process_name = multiprocessing.current_process().name

    # Wait for semaphore permit (simulate barrier)
    semaphore.acquire()
    
    now = time()
    with lock:
        print(f"[{process_name}] ----> {datetime.fromtimestamp(now)}")
        results = []
        do_something(task_load, results)
        print(f"[{process_name}] results: {results}\n")
    
    # Release semaphore so others can proceed
    semaphore.release()

def task_without_barrier(task_load=2):
    """
    Task executed by a process without any synchronization.
    """
    process_name = multiprocessing.current_process().name
    now = time()
    print(f"[{process_name}] ----> {datetime.fromtimestamp(now)}")
    results = []
    do_something(task_load, results)
    print(f"[{process_name}] results: {results}\n")

if __name__ == '__main__':
    print("🔹 Starting Barrier and Lock demonstration...\n")

    # Synchronization primitives
    lock = multiprocessing.Lock()
    semaphore = multiprocessing.Semaphore(2)  # Simulate barrier for 2 processes

    # Create processes
    processes = [
        multiprocessing.Process(name='P1 - with_barrier', target=task_with_barrier, args=(semaphore, lock)),
        multiprocessing.Process(name='P2 - with_barrier', target=task_with_barrier, args=(semaphore, lock)),
        multiprocessing.Process(name='P3 - without_barrier', target=task_without_barrier),
        multiprocessing.Process(name='P4 - without_barrier', target=task_without_barrier)
    ]

    # Start all processes
    for p in processes:
        p.start()

    # Wait for all processes to finish
    for p in processes:
        p.join()

    print("\n✅ Barrier and Lock demonstration completed.")
