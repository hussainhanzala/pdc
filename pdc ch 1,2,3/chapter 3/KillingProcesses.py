# multiprocessing_demo.py
import multiprocessing
import time
from dosomething import do_something

def run_task(task_size=10):
    """Worker process performs a CPU-bound computation."""
    print(f"[Child PID={multiprocessing.current_process().pid}] Process started...")
    shared_list = multiprocessing.Manager().list()

    do_something(task_size, shared_list)

    print(f"[Child PID={multiprocessing.current_process().pid}] Process finished with {len(shared_list)} results.")

if __name__ == '__main__':
    print("🔹 Initializing multiprocessing demo...\n")

    process = multiprocessing.Process(target=run_task, args=(10,))
    print("Before start:", process, "| Alive:", process.is_alive())

    process.start()
    print("After start:", process, "| Alive:", process.is_alive())

    # Allow process to run for a short time
    time.sleep(2)

    # Terminate the process to demonstrate lifecycle control
    print("\nAttempting to terminate process...")
    process.terminate()
    print("Terminated:", process, "| Alive:", process.is_alive())

    process.join()
    print("Joined:", process, "| Alive:", process.is_alive())
    print("Exit code:", process.exitcode)

    print("\n✅ Multiprocessing lifecycle demonstration completed.")
