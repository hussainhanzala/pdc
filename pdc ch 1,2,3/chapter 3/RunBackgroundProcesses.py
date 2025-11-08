# daemon_vs_non_daemon.py
import multiprocessing
import time
from dosomething import do_something

def foo():
    """
    Worker process that executes CPU-bound tasks using do_something().
    Behavior differs for daemon and non-daemon processes.
    """
    process_name = multiprocessing.current_process().name
    print(f"[{process_name}] Starting...\n")

    # Shared list via Manager (optional if collecting results)
    results = multiprocessing.Manager().list()

    # Different workloads for demonstration
    if process_name == 'background_process':
        do_something(5, results)
    else:
        do_something(10, results)

    # Simulate some processing delay
    time.sleep(1)

    print(f"[{process_name}] Exiting...\n")


if __name__ == '__main__':
    print("🔹 Demonstrating daemon vs non-daemon processes...\n")

    # Create a daemon process (terminates with main program)
    background_process = multiprocessing.Process(
        name='background_process',
        target=foo
    )
    background_process.daemon = True

    # Create a normal (non-daemon) process
    normal_process = multiprocessing.Process(
        name='NO_background_process',
        target=foo
    )
    normal_process.daemon = False

    # Start processes
    background_process.start()
    normal_process.start()

    # Join processes (with timeout for daemon demonstration)
    background_process.join(timeout=2)  # daemon may terminate if main exits
    normal_process.join()               # non-daemon completes fully

    print("✅ Daemon vs Non-Daemon demonstration completed.")
