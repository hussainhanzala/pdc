from mpi4py import MPI
import numpy as np
import math

# Direction constants
UP = 0
DOWN = 1
LEFT = 2
RIGHT = 3

neighbour_processes = [0, 0, 0, 0]

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
        area_circle + peri_circle + area_rect + peri_rect +
        area_square + peri_square + area_triangle +
        sa_cube + vol_cube + sa_cuboid + vol_cuboid +
        sa_cylinder + vol_cylinder
    )

    return total


if __name__ == "__main__":

    # MPI initialization
    comm = MPI.COMM_WORLD
    rank = comm.rank
    size = comm.size

    # Create grid topology
    grid_row = int(np.floor(np.sqrt(size)))
    grid_column = size // grid_row

    if grid_row * grid_column > size:
        grid_column -= 1
    if grid_row * grid_column > size:
        grid_row -= 1

    if rank == 0:
        print(f"Building a {grid_row} x {grid_column} grid topology\n")

    cartesian_communicator = comm.Create_cart(
        dims=(grid_row, grid_column),
        periods=(True, True),
        reorder=True
    )

    my_mpi_row, my_mpi_col = cartesian_communicator.Get_coords(
        cartesian_communicator.rank
    )

    neighbour_processes[UP], neighbour_processes[DOWN] = \
        cartesian_communicator.Shift(0, 1)

    neighbour_processes[LEFT], neighbour_processes[RIGHT] = \
        cartesian_communicator.Shift(1, 1)

    print(f"""
Process = {rank}
Row = {my_mpi_row}, Column = {my_mpi_col}
Neighbours:
UP = {neighbour_processes[UP]}
DOWN = {neighbour_processes[DOWN]}
LEFT = {neighbour_processes[LEFT]}
RIGHT = {neighbour_processes[RIGHT]}
""")

    # 🔢 Mensuration calculation on each process
    local_total = mensuration_calculations()

    # ➕ Reduce (sum) all values to Rank 0
    global_total = comm.reduce(local_total, op=MPI.SUM, root=0)

    if rank == 0:
        print(f"Final Mensuration Total (Summed from all processes): {global_total:.2f}")
