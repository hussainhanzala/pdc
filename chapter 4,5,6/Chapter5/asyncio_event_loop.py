import math
import asyncio
import random

# Mensuration Calculations
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
    
    total = (
        area_circle + peri_circle + area_rect + peri_rect +
        area_square + peri_square + area_triangle +
        sa_cube + vol_cube + sa_cuboid + vol_cuboid +
        sa_cylinder + vol_cylinder
    )
    
    return total


# Async tasks
async def task_A(end_time):
    while asyncio.get_running_loop().time() < end_time:
        print("task_A called")
        await asyncio.sleep(random.randint(0, 5))
        await task_B(end_time)

async def task_B(end_time):
    while asyncio.get_running_loop().time() < end_time:
        print("task_B called")
        await asyncio.sleep(random.randint(0, 5))
        await task_C(end_time)

async def task_C(end_time):
    while asyncio.get_running_loop().time() < end_time:
        print("task_C called")
        await asyncio.sleep(random.randint(0, 5))
        # loop back to A
        await task_A(end_time)


# Main execution
if __name__ == "__main__":
    # Mensuration
    result = mensuration_calculations()
    print(f"Mensuration calculation total: {result:.2f}")
    
    # Async tasks for 60 seconds
    loop = asyncio.get_event_loop()
    end_loop = loop.time() + 60  # run tasks for 60 seconds
    try:
        loop.run_until_complete(task_A(end_loop))
    finally:
        loop.close()
