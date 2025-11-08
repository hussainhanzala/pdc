# daemon_vs_non_daemon_demo.py
import multiprocessing
import time
from dosomething import do_something

def worker_task():
    """
    Demonstrates the behavior of daemon and non-daemon processes.
    Daemon processes may exit when the main program exits.
    """
    process_name = multiprocessing.current_process().name
    print(f"[{process_name}] Starting...\n")

    if process_name == 'background_process':
        # Simulate short repetitive work for daemon process
        for i in range(5):
            print(f"[{process_name}] --> Step {i}")
            time.sleep(0.3)
    else:
        # CPU-bound work for non-daemon process
        results = []
        do_something(3, results)
        print(f"[{process_name}] results: {results}")
        time.sleep(1)

    print(f"[{process_name}] Exiting...\n")


if __name__ == '__main__':
    print("🔹 Demonstrating Daemon vs Non-Daemon Processes\n")

    # Create a daemon process (terminates if main program exits)
    background_process = multiprocessing.Process(
        name='background_process',
        target=worker_task
    )
    background_process.daemon = True

    # Create a normal non-daemon process
    normal_process = multiprocessing.Process(
        name='normal_process',
        target=worker_task
    )
    normal_process.daemon = False

    # Start both processes
    background_process.start()
    normal_process.start()

    # Wait for processes to complete
    background_process.join(timeout=2)  # daemon may exit early
    normal_process.join()               # non-daemon completes fully

    print("✅ Daemon vs Non-Daemon demonstration finished.")
