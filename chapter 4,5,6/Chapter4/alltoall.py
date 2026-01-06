import math
import numpy
from mpi4py import MPI


comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()


def mensuration_calculations():
    """Calculate various 2D and 3D shapes measurements"""

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


local_result = mensuration_calculations()

# Each process prepares data to send
senddata = (rank + 1) * numpy.full(size, int(local_result))
recvdata = numpy.empty(size, dtype=int)

# All-to-all communication
comm.Alltoall(senddata, recvdata)


print(f"Process {rank}")
print(f"  Mensuration total: {local_result:.2f}")
print(f"  Sending: {senddata}")
print(f"  Receiving: {recvdata}\n")
