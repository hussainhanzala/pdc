import math
from mpi4py import MPI

# MPI setup
comm = MPI.COMM_WORLD
rank = comm.rank

print("My rank is:", rank)

def mensuration_calculations():
    """Calculate various 2D and 3D shapes measurements"""
    
    # Define dimensions
    r = 7.5
    l, b, h = 12, 8, 5
    a = 6
    
    # 2D Shapes
    area_circle = math.pi * r ** 2
    peri_circle = 2 * math.pi * r
    
    area_rect = l * b
    peri_rect = 2 * (l + b)
    
    area_square = a ** 2
    peri_square = 4 * a
    
    area_triangle = 0.5 * b * h
    
    # 3D Shapes
    sa_cube = 6 * a ** 2
    vol_cube = a ** 3
    
    sa_cuboid = 2 * (l*b + b*h + h*l)
    vol_cuboid = l * b * h
    
    sa_cylinder = 2 * math.pi * r * (r + h)
    vol_cylinder = math.pi * r ** 2 * h
    
    total = (
        area_circle + peri_circle +
        area_rect + peri_rect +
        area_square + peri_square +
        area_triangle +
        sa_cube + vol_cube +
        sa_cuboid + vol_cuboid +
        sa_cylinder + vol_cylinder
    )
    
    return total

# Rank 0: calculate mensuration and send
if rank == 0:
    result = mensuration_calculations()
    destination_process = 4
    comm.send(result, dest=destination_process)
    print(f"Sending mensuration result {result:.2f} to process {destination_process}")

# Rank 1: send message
if rank == 1:
    destination_process = 8
    data = "hello"
    comm.send(data, dest=destination_process)
    print(f"Sending data '{data}' to process {destination_process}")

# Rank 4: receive mensuration result
if rank == 4:
    data = comm.recv(source=0)
    print(f"Mensuration result received = {data:.2f}")

# Rank 8: receive message
if rank == 8:
    data1 = comm.recv(source=1)
    print(f"Data received = {data1}")
