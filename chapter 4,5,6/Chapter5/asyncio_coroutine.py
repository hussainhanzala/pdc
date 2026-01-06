import math
import asyncio
from random import randint

# ---------------- Mensuration Calculations ----------------
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
    
    # Total sum of all measurements
    total = (
        area_circle + peri_circle + area_rect + peri_rect +
        area_square + peri_square + area_triangle +
        sa_cube + vol_cube + sa_cuboid + vol_cuboid +
        sa_cylinder + vol_cylinder
    )
    
    return total

# ---------------- Asynchronous Finite State Machine ----------------
async def start_state():
    print('Start State called\n')
    input_value = randint(0, 1)
    await asyncio.sleep(1)

    if input_value == 0:
        result = await state2(input_value)
    else:
        result = await state1(input_value)

    print('Resume of the Transition : \nStart State calling ' + result)


async def state1(transition_value):
    output_value = f'State 1 with transition value = {transition_value}\n'
    input_value = randint(0, 1)
    await asyncio.sleep(1)

    print('...evaluating...')
    if input_value == 0:
        result = await state3(input_value)
    else:
        result = await state2(input_value)

    return output_value + f'State 1 calling {result}'


async def state2(transition_value):
    output_value = f'State 2 with transition value = {transition_value}\n'
    input_value = randint(0, 1)
    await asyncio.sleep(1)

    print('...evaluating...')
    if input_value == 0:
        result = await state1(input_value)
    else:
        result = await state3(input_value)

    return output_value + f'State 2 calling {result}'


async def state3(transition_value):
    output_value = f'State 3 with transition value = {transition_value}\n'
    input_value = randint(0, 1)
    await asyncio.sleep(1)

    print('...evaluating...')
    if input_value == 0:
        result = await state1(input_value)
    else:
        result = await end_state(input_value)

    return output_value + f'State 3 calling {result}'


async def end_state(transition_value):
    output_value = f'End State with transition value = {transition_value}\n'
    print('...stop computation...')
    return output_value


# ---------------- Main Execution ----------------
if __name__ == "__main__":
    # Run mensuration calculations
    result = mensuration_calculations()
    print(f"Mensuration calculation total: {result:.2f}\n")
    
    # Run finite state machine
    print('Finite State Machine simulation with Asyncio Coroutine\n')
    asyncio.run(start_state())
