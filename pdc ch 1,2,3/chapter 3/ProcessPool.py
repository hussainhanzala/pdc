# multiprocessing_pool_demo.py
import multiprocessing
from dosomething import do_something

def compute_square(number: int) -> int:
    """
    Simulates a CPU-bound task and returns the square of the input number.
    
    Args:
        number (int): Input number to square.
    
    Returns:
        int: Square of the input number.
    """
    # Simulate some CPU work
    results = []
    do_something(2, results)

    # Return the squared value
    return number * number

if __name__ == '__main__':
    # Input data
    input_numbers = list(range(10))

    print("🔹 Starting multiprocessing pool demo...")

    # Create a pool of 4 worker processes
    with multiprocessing.Pool(processes=4) as pool:
        # Map the function across the input data
        output_numbers = pool.map(compute_square, input_numbers)

    print("\n✅ Pool computation completed.")
    print(f"Inputs: {input_numbers}")
    print(f"Outputs (squared): {output_numbers}")
