import numpy as np

def multiply_matrices(size, output_list):
    """Generates two random matrices and multiplies them using NumPy."""
    
    # Generate random matrices
    matrix_a = np.random.random((size, size))
    matrix_b = np.random.random((size, size))
    
    # Perform matrix multiplication
    product = matrix_a @ matrix_b   # equivalent to np.dot(matrix_a, matrix_b)
    
    # Compute a summarized metric (e.g., total sum)
    total_sum = float(np.sum(product))
    
    # Store result summary (not the full matrix)
    output_list.append(total_sum)

    # Optional: print small progress indicator for debugging
    # print(f"Matrix of size {size}x{size} multiplied. Sum = {total_sum:.2f}")
