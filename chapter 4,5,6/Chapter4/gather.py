import math
from mpi4py import MPI

def mensuration_calculations():
    """Calculate various 2D and 3D shapes measurements"""

    # Define dimensions
    r = 7.5                  # radius
    l, b, h = 12, 8, 5        # length, breadth, height
    a = 6                    # side length

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
        area_circle + peri_circle + area_rect + peri_rect +
        area_square + peri_square + area_triangle +
        sa_cube + vol_cube + sa_cuboid + vol_cuboid +
        sa_cylinder + vol_cylinder
    )

    return total


# ================= MPI PART =================

comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()

# Each process performs mensuration calculation
mensuration_result = mensuration_calculations()

# Send results to root process
data = comm.gather(mensuration_result, root=0)

# Root process prints received data
if rank == 0:
    print(f"Rank {rank} receiving mensuration results from other processes\n")
    for i in range(size):
        print(f"Process {i} result: {data[i]:.2f}")
