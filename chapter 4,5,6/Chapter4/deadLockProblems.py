import math
from mpi4py import MPI

# ---------------- Mensuration Function ----------------
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

# ---------------- MPI Code ----------------
comm = MPI.COMM_WORLD
rank = comm.rank
print(f"My rank is {rank}")

# Each process computes mensuration
mensuration_result = mensuration_calculations()
print(f"Rank {rank} mensuration total: {mensuration_result:.2f}")

# Rank 1 logic
if rank == 1:
    data_send = "a"
    destination_process = 5
    source_process = 5

    data_received = comm.recv(source=source_process)
    comm.send(data_send, dest=destination_process)

    print(f"Rank 1 sending data '{data_send}' to process {destination_process}")
    print(f"Rank 1 received data = '{data_received}'")

# Rank 5 logic
if rank == 5:
    data_send = "b"
    destination_process = 1
    source_process = 1

    comm.send(data_send, dest=destination_process)
    data_received = comm.recv(source=source_process)

    print(f"Rank 5 sending data '{data_send}' to process {destination_process}")
    print(f"Rank 5 received data = '{data_received}'")
