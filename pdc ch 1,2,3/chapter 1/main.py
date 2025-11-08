from matrix_multiplication import multiply_matrices
import time
import multiprocessing
import threading

def run_multiprocessing(matrix_size, num_processes):
    """Run matrix multiplication using multiprocessing."""
    processes = []
    print("\n--- Starting Multiprocessing Execution ---")
    start = time.perf_counter()

    for _ in range(num_processes):
        result_holder = []
        proc = multiprocessing.Process(target=multiply_matrices, args=(matrix_size, result_holder))
        processes.append(proc)
        proc.start()

    # Wait for all processes to finish
    for proc in processes:
        proc.join()

    elapsed = time.perf_counter() - start
    print(f"[Multiprocessing] Completed in {elapsed:.3f} seconds\n")
    return elapsed


def run_multithreading(matrix_size, num_threads):
    """Run matrix multiplication using multithreading."""
    threads = []
    print("--- Starting Multithreading Execution ---")
    start = time.perf_counter()

    for _ in range(num_threads):
        result_container = []
        th = threading.Thread(target=multiply_matrices, args=(matrix_size, result_container))
        th.start()
        threads.append(th)

    # Wait for all threads to complete
    for th in threads:
        th.join()

    elapsed = time.perf_counter() - start
    print(f"[Multithreading] Completed in {elapsed:.3f} seconds\n")
    return elapsed


if __name__ == "__main__":
    MATRIX_SIZE = 500
    NUM_TASKS = 20

    time_mp = run_multiprocessing(MATRIX_SIZE, NUM_TASKS)
    time_mt = run_multithreading(MATRIX_SIZE, NUM_TASKS)

    print("=== Summary ===")
    print(f"Multiprocessing Time: {time_mp:.3f} sec")
    print(f"Multithreading Time: {time_mt:.3f} sec")
    print("Performance difference:", round(time_mp - time_mt, 3), "seconds")
