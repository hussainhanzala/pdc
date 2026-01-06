import math
import asyncio
import sys

# ------------------ Mensuration Function ------------------

def mensuration_calculations():
    """Calculate various 2D and 3D shapes measurements"""

    r = 7.5
    l, b, h = 12, 8, 5
    a = 6

    # 2D shapes
    area_circle = math.pi * r ** 2
    peri_circle = 2 * math.pi * r

    area_rect = l * b
    peri_rect = 2 * (l + b)

    area_square = a ** 2
    peri_square = 4 * a

    area_triangle = 0.5 * b * h

    # 3D shapes
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

# ------------------ Async Coroutines ------------------

async def first_coroutine(num):
    count = 0
    for i in range(1, num + 1):
        count += 1
    await asyncio.sleep(4)
    return f"First coroutine (sum of N ints) result = {count}"


async def second_coroutine(num):
    count = 1
    for i in range(2, num + 1):
        count *= i
    await asyncio.sleep(4)
    return f"Second coroutine (factorial) result = {count}"


async def mensuration_coroutine():
    await asyncio.sleep(2)
    result = mensuration_calculations()
    return f"Mensuration calculation total = {result:.2f}"

# ------------------ Main Event Loop ------------------

async def main(num1, num2):
    results = await asyncio.gather(
        first_coroutine(num1),
        second_coroutine(num2),
        mensuration_coroutine()
    )

    for res in results:
        print(res)


if __name__ == "__main__":
    num1 = int(sys.argv[1])
    num2 = int(sys.argv[2])

    asyncio.run(main(num1, num2))
