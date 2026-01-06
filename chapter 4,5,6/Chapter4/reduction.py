import math
import numpy as np
from mpi4py import MPI

# MPI setup
comm = MPI.COMM_WORLD
size = comm.size
rank = comm.rank


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


# Each process computes mensuration result
local_result = mensuration_calculations()

# Create send & receive buffers
senddata = np.array(local_result, dtype=np.float64)
recvdata = np.array(0.0, dtype=np.float64)

print(f"Process {rank} sending mensuration total = {senddata:.2f}")

# Reduce (sum) all processes' results to root (rank 0)
comm.Reduce(senddata, recvdata, op=MPI.SUM, root=0)

# Only root prints final result
if rank == 0:
    print("\nFinal Reduced Result (Sum from all processes):")
    print(f"Total Mensuration Sum = {recvdata:.2f}")
    print(f"Number of Processes = {size}")
