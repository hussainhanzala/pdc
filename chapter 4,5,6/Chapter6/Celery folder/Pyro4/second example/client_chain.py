from __future__ import print_function
import math
import Pyro4


def mensuration_calculations():
    """Calculate various 2D and 3D shapes measurements"""

    # Define dimensions
    r = 7.5                # radius
    l, b, h = 12, 8, 5     # length, breadth, height
    a = 6                  # side length

    # 2D Shapes Calculations

    # Circle
    area_circle = math.pi * r ** 2
    peri_circle = 2 * math.pi * r

    # Rectangle
    area_rect = l * b
    peri_rect = 2 * (l + b)

    # Square
    area_square = a ** 2
    peri_square = 4 * a

    # Triangle
    area_triangle = 0.5 * b * h

    # 3D Shapes Calculations

    # Cube
    sa_cube = 6 * a ** 2
    vol_cube = a ** 3

    # Cuboid
    sa_cuboid = 2 * (l*b + b*h + h*l)
    vol_cuboid = l * b * h

    # Cylinder
    sa_cylinder = 2 * math.pi * r * (r + h)
    vol_cylinder = math.pi * r ** 2 * h

    # Total of all calculations
    total = (
        area_circle + peri_circle + area_rect + peri_rect +
        area_square + peri_square + area_triangle +
        sa_cube + vol_cube + sa_cuboid + vol_cuboid +
        sa_cylinder + vol_cylinder
    )

    return total


if __name__ == "__main__":
    # Calculate mensuration result
    result = mensuration_calculations()
    print(f"Mensuration calculation total: {result:.2f}")

    # Send result to Pyro object
    obj = Pyro4.core.Proxy("PYRONAME:example.chainTopology.1")
    pyro_result = obj.process([result])

    print("Result from Pyro =", pyro_result)
