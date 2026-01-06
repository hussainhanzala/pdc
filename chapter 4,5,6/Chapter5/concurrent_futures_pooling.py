import math
import concurrent.futures
import time

# -------------------------
# Mensuration Calculations
# -------------------------
def mensuration_calculations():
    """Calculate various 2D and 3D shapes measurements"""
    
    # Define dimensions
    r = 7.5      # radius
    l, b, h = 12, 8, 5  # length, breadth, height
    a = 6        # side length
    
    # 2D Shapes Calculations
    area_circle = math.pi * r ** 2            
    peri_circle = 2 * math.pi * r             
    
    area_rect = l * b                         
    peri_rect = 2 * (l + b)                   
    
    area_square = a ** 2                      
    peri_square = 4 * a                       
    
    area_triangle = 0.5 * b * h               
    
    # 3D Shapes Calculations
    sa_cube = 6 * a ** 2                      
    vol_cube = a ** 3                         

    sa_cuboid = 2 * (l*b + b*h + h*l)         
    vol_cuboid = l * b * h                    

    sa_cylinder = 2 * math.pi * r * (r + h)   
    vol_cylinder = math.pi * r ** 2 * h       

    # Calculate total sum of all measurements
    total = (
        area_circle + peri_circle + area_rect + peri_rect +
        area_square + peri_square + area_triangle +
        sa_cube + vol_cube + sa_cuboid + vol_cuboid +
        sa_cylinder + vol_cylinder
    )
    
    return total

# -------------------------
# Concurrent Computations
# -------------------------
number_list = list(range(1, 11))

def count(number):
    for i in range(0, 10000000):
        i += 1
    return i * number

def evaluate(item):
    result_item = count(item)
    print(f'Item {item}, result {result_item}')

# -------------------------
# Main Execution
# -------------------------
if __name__ == "__main__":
    # Mensuration calculation
    result = mensuration_calculations()
    print(f"\nMensuration calculation total: {result:.2f}\n")
    
    # Sequential Execution
    start_time = time.perf_counter()
    for item in number_list:
        evaluate(item)
    print('Sequential Execution in {:.2f} seconds\n'.format(time.perf_counter() - start_time))

    # Thread Pool Execution
    start_time = time.perf_counter()
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        for item in number_list:
            executor.submit(evaluate, item)
    print('Thread Pool Execution in {:.2f} seconds\n'.format(time.perf_counter() - start_time))

    # Process Pool Execution
    start_time = time.perf_counter()
    with concurrent.futures.ProcessPoolExecutor(max_workers=5) as executor:
        for item in number_list:
            executor.submit(evaluate, item)
    print('Process Pool Execution in {:.2f} seconds\n'.format(time.perf_counter() - start_time))
